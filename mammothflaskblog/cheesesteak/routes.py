from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_mail import Message

from mammothflaskblog import mail
from mammothflaskblog.models import CarouselSlider
from mammothflaskblog.cheesesteak.forms import CheesesteakForm
from mammothflaskblog.config import Config

from math import sqrt

from geopy.geocoders import Nominatim

import requests

cheesesteaks = Blueprint('cheesesteak', __name__)


class Cheesesteak:
    """User inputs address and how far they're willing to go. App
    returns a list of all places to get a cheesesteak within that area.
    """
    def __init__(self,
                 full_street_addy,
                 city,
                 state,
                 how_many_blocks,
                 max_results):
        self.full_street_addy = full_street_addy
        self.city = city
        self.state = state
        self.how_many_blocks = how_many_blocks
        self.max_results = max_results
        self.endpoint = "https://api.yelp.com/v3/businesses/search"
        self.get_api_verification()
        self.get_search_parameters()
        self.get_geocoordinates()
        if self.location:
            self.headers = {
                    'Authorization': 'bearer {}'.format(self.yelp_api_key)}
            self.parameters = {
                    'term': 'cheesesteak',
                    'limit': self.max_results,
                    'latitude': self.latitude,
                    'longitude': self.longitude,
                    'radius': self.radius_meters,
                    'location': self.city_state}
            response = requests.get(
                url=self.endpoint,
                params=self.parameters,
                headers=self.headers)
            response_data = sorted(
                    response.json()['businesses'],
                    key=lambda x: x['distance'])
            self.results_list = []
            for biz in response_data:
                if biz['distance'] < self.radius_meters:
                    result_dict_entry = dict()
                    distance_to_cheesesteak = self.convert_meters_to_blocks(
                            biz['distance'])

                    if distance_to_cheesesteak > 1:
                        result_dict_entry['distance_to_cheesesteak'] = (
                            f"About {distance_to_cheesesteak + 1} blocks away")
                    elif distance_to_cheesesteak == 0:
                        result_dict_entry['distance_to_cheesesteak'] = (
                            f"Less than a block away")
                    else:
                        result_dict_entry['distance_to_cheesesteak'] = (
                            f"About {distance_to_cheesesteak} block away")
                    result_dict_entry['name'] = biz['name']
                    result_dict_entry['address'] = biz['location']['address1']
                    if biz['phone']:
                        result_dict_entry['phone'] = biz['phone']
                    else:
                        result_dict_entry['phone'] = 'Not Listed'
                    self.results_list.append(result_dict_entry)

    def get_search_parameters(self):
        """Get address from user and store it within instance variables.
        Find out how large an area will be searched.
        """
        self.city_state = "{}, {}".format(self.city, self.state)
        self.full_address = "{} {}".format(
                self.full_street_addy, self.city_state)

        self.distance_meters = self.how_many_blocks * 120
        self.radius_meters = (int(
            sqrt(
                (self.distance_meters // 2) ** 2 
              + (self.distance_meters // 2) ** 2 ))
              + 1)

    def get_geocoordinates(self):
        """Use geopy module to determine coordinates of address to 
        anchor the search for cheesesteak.
        """
        self.geolocator = Nominatim(user_agent="philly_cheesesteak_finder")
        self.location = self.geolocator.geocode(self.full_address)
        if self.location:
            self.latitude = self.location.latitude
            self.longitude = self.location.longitude



    def get_api_verification(self):
        """Looks in config.py for the API key and the client id, so
        that we can use the API.
        """
        self.yelp_api_key = Config.YELP_API_KEY
        self.yelp_client_id = Config.YELP_CLIENT_ID

    def convert_meters_to_blocks(self, distance_meters):
        """Meter to block conversion method."""
        distance_blocks = distance_meters // 120
        return int(distance_blocks)


@cheesesteaks.route("/cheesesteak/", methods=['GET', 'POST'])
def new_cheesesteak_search():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)

    form = CheesesteakForm()
    if form.validate_on_submit():

        street_address = form.street_address.data
        full_street_addy = street_address.strip()
        city = form.city.data.strip()
        state = form.state.data
        how_many_blocks = form.how_many_blocks.data
        max_results = form.max_results.data

        cheesesteak_search = Cheesesteak(full_street_addy,
                                         city,
                                         state,
                                         how_many_blocks,
                                         max_results)
        if not cheesesteak_search.location:
            flash(f'{full_street_addy}, {city} {state} not found. Check spelling or try choosing a nearby address', 'success')
            return redirect('/cheesesteak')

        msg = Message('Cheesesteak search', 
                      sender=Config.MFB_EMAIL,
                      recipients=[Config.MFB_EMAIL])
        message_string = f"""<h4>Address: {full_street_addy}<br>
City, State: {city}, {state}<br>
# of blocks: {how_many_blocks}<br>
max results: {max_results}<br><br>"""
        message_string += "</h4>"
        msg.html = message_string
        mail.send(msg)

        return render_template('cheesesteak_results.html',
                title=Config.SITE_NAME,
                results=cheesesteak_search.results_list,
                carousel_slides1=carousel_slides1,
                carousel_slides2=carousel_slides2)

    return render_template('cheesesteak_search.html',
                           title='Find Cheesesteak',
                           form=form,
                           carousel_slides1=carousel_slides1,
                           carousel_slides2=carousel_slides2)