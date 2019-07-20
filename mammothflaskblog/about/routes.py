
from flask import render_template
from flask import url_for
from flask import Blueprint
from mammothflaskblog.models import CarouselSlider

about_the_project = Blueprint('about_the_project', __name__)


@about_the_project.route("/about-the-project")
def project_description():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    return render_template('about_the_project.html',
                           title="Project Description",
                           carousel_slides1=carousel_slides1,
                           carousel_slides2=carousel_slides2)