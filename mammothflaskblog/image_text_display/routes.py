
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_required
from mammothflaskblog import db
from mammothflaskblog.models import CarouselSlider
from mammothflaskblog.models import TextAndImage
from mammothflaskblog.image_text_display.forms import TextAndImageForm
import os


image_text_display = Blueprint('image_text_display', __name__)


@image_text_display.route("/display-text-and-images")
def view_text_and_images():
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    page = request.args.get('page', 1, type=int)
    text_and_images = TextAndImage.query.order_by(
            TextAndImage.id.desc()).paginate(page=page, per_page=3)
    return render_template('image_text_display.html',
                           text_and_images=text_and_images,
                           carousel_slides1=carousel_slides1,
                           carousel_slides2=carousel_slides2)


@image_text_display.route("/display-text-and-images/new",
                          methods=['GET', 'POST'])
@login_required
def new_text_and_image():
    form = TextAndImageForm()

    if form.validate_on_submit():
        text_and_image = TextAndImage()
        db.session.add(text_and_image)
        db.session.commit()

        if form.text_part.data:
            text_and_image = db.session.query(TextAndImage).order_by(
                    TextAndImage.id.desc()).first()
            text_and_image.text_part = form.text_part.data
            db.session.commit()

        if form.image_file.data:
            text_and_image = db.session.query(TextAndImage).order_by(
                    TextAndImage.id.desc()).first()
            image_file = form.image_file.data
            filename = "letter_image"
                     + str(text_and_image.id)
                     + os.path.splitext(image_file.filename)[1]
            path_plus_filename = os.path.join(
                    'mammothflaskblog/static/text_and_images',
                    filename)
            image_file.save(path_plus_filename)
            image_file_filename_for_db = os.path.join(
                    'text_and_images',
                    filename)
            text_and_image.image_filename = image_file_filename_for_db
            db.session.commit()

        flash("Text and/or Image has been uploaded!", 'success')
        return redirect(url_for(
                'image_text_display.view_text_and_images'))
    return render_template('new_text_and_image.html',
                           title='New Text and/or Image',
                           form=form,
                           legend='New Text and/or Image')


@image_text_display.route(
        "/text-and-image/<int:text_and_image_id>/update",
        methods=['GET', 'POST'])
@login_required
def update_text_and_image(text_and_image_id):

    text_and_image = TextAndImage.query.get_or_404(text_and_image_id)

    form = TextAndImageForm()

    if form.validate_on_submit():

        if form.text_part.data:
            text_and_image.text_part = form.text_part.data
            db.session.commit()

        if form.image_file.data:
            if text_and_image.image_filename:
                file_path_to_delete = "mammothflaskblog/static/"
                                    + text_and_image.image_filename
                if os.path.isfile(file_path_to_delete):
                    os.remove(file_path_to_delete)
            image_file = form.image_file.data
            filename = "letter_image" 
                     + str(text_and_image.id)
                     + os.path.splitext(image_file.filename)[1]
            path_plus_filename = os.path.join(
                    'mammothflaskblog/static/text_and_images',
                    filename)
            image_file.save(path_plus_filename)
            image_file_filename_for_db = os.path.join(
                    'text_and_images', filename)
            text_and_image.image_filename = image_file_filename_for_db
            db.session.commit()

        flash('Text and/or Image has been updated :)', 'success')
        return redirect(url_for(
                'image_text_display.view_text_and_images'))
    elif request.method == 'GET':
        if text_and_image.text_part:
            form.text_part.data = text_and_image.text_part

    return render_template('new_text_and_image.html',
                           title='Update Text and/or Image',
                           form=form,
                           text_and_image=text_and_image,
                           legend='Update Text and/or Image')


@image_text_display.route(
        "/text-and-image/<int:text_and_image_id>/delete",
        methods=['POST', 'GET'])
@login_required
def delete_text_and_image(text_and_image_id):
    text_and_image = TextAndImage.query.get_or_404(text_and_image_id)

    if text_and_image.image_filename:
        file_path_to_delete = "mammothflaskblog/static/"
                            + text_and_image.image_filename
        if os.path.isfile(file_path_to_delete):
            os.remove(file_path_to_delete)

    db.session.delete(text_and_image)
    db.session.commit()
    flash('Text and/or Image has been deleted.', 'success')
    return redirect(url_for(
            'image_text_display.view_text_and_images'))