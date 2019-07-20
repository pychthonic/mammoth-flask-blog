from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_mail import Message
from mammothflaskblog import mail
from mammothflaskblog.config import Config
from mammothflaskblog.models import CarouselSlider
from mammothflaskblog.submit_info.forms import EmailListForm
from mammothflaskblog.submit_info.forms import MemberForm
from mammothflaskblog.submit_info.forms import VolunteerForm


submit_info = Blueprint('submit_info', __name__)


@submit_info.route("/volunteer", methods=['GET', 'POST'])
def sign_up_to_volunteer():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    form = VolunteerForm()
    if form.validate_on_submit():
        msg = Message(
                'New volunteer form submitted from website!',
                sender=Config.MFB_EMAIL,
                recipients=[Config.MFB_EMAIL])
        message_string = f"""<h4>Name: {form.first_name.data} {form.last_name.data}<br>
Phone: {form.phone_number.data}<br>
Email: {form.volunteer_email.data}<br>
Address: {form.street_addy.data}<br>
Apt/Suite/Bldg: {form.apt_suite_bldg.data}<br>
City: {form.volunteer_city.data}<br>
State: {form.volunteer_state.data}<br>
Zip: {form.volunteer_zip.data}<br>
Country: {form.volunteer_country.data}<br><br>
Can help with:<br>"""
        if form.reporting.data:
            message_string += "<br>Reporting<br>"
        if form.project_leadership.data:
            message_string += "Project Leadership<br>"
        if form.writing_and_editing.data:
            message_string += "Writing and Editing<br>"
        if form.outreach.data:
            message_string += "Neighborhood Outreach<br>"
        if form.social_media.data:
            message_string += "Social Media<br>"
        if form.office_help.data:
            message_string += "Office Help<br>"
        if form.legal.data:
            message_string += "Legal<br>"
        if form.fundraising.data:
            message_string += "Fundraising<br>"
        if form.other_volunteering_deets.data:
            message_string += f"Other help not listed: {form.other_volunteering_deets.data}"
        message_string += "</h4>"
        msg.html = message_string
        mail.send(msg)

        flash('Thanks for signing up! We will be in touch soon :)',
              'success')
        return redirect(url_for('main.home'))
    return render_template(
            'volunteer.html',
            title='Sign Up To Help!',
            form=form,
            legend='Sign Up To Help!',
            carousel_slides1=carousel_slides1,
            carousel_slides2=carousel_slides2)

@submit_info.route("/submit-info")
def submit_info_main():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    return render_template(
            'submit_info.html',
            title="Take Action",
            carousel_slides1=carousel_slides1,
            carousel_slides2=carousel_slides2)

@submit_info.route("/become-a-member", methods=['GET', 'POST'])
def sign_up_for_membership():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    form = MemberForm()
    if form.validate_on_submit():
        msg = Message('New member form submitted from website!', 
                      sender=Config.MFB_EMAIL,
                      recipients=[Config.MFB_EMAIL])
        message_string = f"""<h4>Name: {form.first_name.data} {form.last_name.data}<br>
Phone: {form.phone_number.data}<br>
Email: {form.member_email.data}<br>
Address: {form.street_addy.data}<br>
Apt/Suite/Bldg: {form.apt_suite_bldg.data}<br>
City: {form.member_city.data}<br>
State: {form.member_state.data}<br>
Zip: {form.member_zip.data}<br>
Country: {form.member_country.data}<br><br>"""
        message_string += "</h4>"
        msg.html = message_string
        mail.send(msg)

        flash('Thanks for signing up! We will be in touch soon :)', 'success')
        return redirect(url_for('main.home'))
    return render_template(
            'become-a-member.html',
            title='Become a Member!',
            form=form,
            legend='Become a Member!',
            carousel_slides1=carousel_slides1,
            carousel_slides2=carousel_slides2)


@submit_info.route("/email-list-sign-up", methods=['GET', 'POST'])
def sign_up_for_email_list():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    form = EmailListForm()
    if form.validate_on_submit():

        msg = Message(
                'New email address submitted for Email Announcements!',
                sender=Config.MFB_EMAIL,
                recipients=[Config.MFB_EMAIL])
        message_string = f"""<h4>
Add this email to Email Announcements List: {form.email_address_to_add.data}<br>
<br><br>"""
        message_string += "</h4>"
        msg.html = message_string
        mail.send(msg)

        flash('Thanks! We will add your email to our Email Announcements List :)',
              'success')
        return redirect(url_for('main.home'))
    return render_template(
            'email_list_sign_up.html',
            title='Email Announcements List Sign-Up',
            form=form,
            legend='Email Announcements List Sign-Up',
            carousel_slides1=carousel_slides1,
            carousel_slides2=carousel_slides2)