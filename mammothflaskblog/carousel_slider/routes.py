from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_required
from mammothflaskblog import db
from mammothflaskblog.models import CarouselSlider
from mammothflaskblog.carousel_slider.forms import CarouselForm
import os


carousel_slider = Blueprint('carousel_slider', __name__)


@carousel_slider.route(
        "/carousel-slider/new-slide",
        methods=['GET', 'POST'])
@login_required
def new_carousel_slide():
    form = CarouselForm()
    if form.validate_on_submit():
        carousel_slider = CarouselSlider(caption=form.caption.data)
        db.session.add(carousel_slider)
        db.session.commit()

        carousel_slider = db.session.query(
                CarouselSlider).order_by(
                CarouselSlider.id.desc()).first()
        image_file = form.image_file.data
        filename = "carousel_image_"
                 + str(carousel_slider.id)
                 + os.path.splitext(image_file.filename)[1]
        path_plus_filename = os.path.join(
                'mammothflaskblog/static/images/carousel-images',
                filename)
        image_file.save(path_plus_filename)
        image_file_filename_for_db = os.path.join(
                'images/carousel-images',
                filename)
        carousel_slider.image_filename = image_file_filename_for_db

        db.session.add(carousel_slider)
        db.session.commit()

        flash("Carousel Slide Added! :)", 'success')
        return redirect(url_for('main.home'))
    return render_template('add_slide_to_carousel.html',
                           title='Add Slide to Carousel',
                           form=form,
                           legend='New Slide for Carousel')


@carousel_slider.route("/carousel-slider/view-slides")
@login_required
def view_carousel_slides():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    return render_template(
            'edit_carousel_slider.html',
            carousel_slides=carousel_slides)


@carousel_slider.route("/carousel-slider/<int:slide_id>/update",
                       methods=['GET', 'POST'])
@login_required
def update_carousel_slide(slide_id):
    carousel_slide = CarouselSlider.query.get_or_404(slide_id)

    form = CarouselForm()

    if form.validate_on_submit():
        carousel_slide.caption = form.caption.data
        db.session.commit()

        flash('Carousel slide has been updated :)', 'success')
        return redirect(url_for(
                'carousel_slider.view_carousel_slides'))

    elif request.method == 'GET':
        form.caption.data = carousel_slide.caption

    return render_template('update_carousel_slide.html',
                           title='Update Carousel Slide',
                           form=form,
                           carousel_slide=carousel_slide,
                           legend='Update Carousel Slide')


@carousel_slider.route("/carousel-slider/<int:slide_id>/delete",
                       methods=['POST', 'GET'])
@login_required
def delete_slide(slide_id):
    carousel_slide = CarouselSlider.query.get_or_404(slide_id)

    file_path_to_delete = "mammothflaskblog/static/" 
                        + carousel_slide.image_filename
    if os.path.isfile(file_path_to_delete):
        os.remove(file_path_to_delete)

    db.session.delete(carousel_slide)
    db.session.commit()

    flash('Slide has been deleted.', 'success')
    return redirect(url_for('main.home'))