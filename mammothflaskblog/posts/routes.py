from flask import abort
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from mammothflaskblog import db
from mammothflaskblog.models import CarouselSlider
from mammothflaskblog.models import Post
from mammothflaskblog.posts.forms import PostForm
import re
import os


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, 
                    content=form.content.data, 
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        post = db.session.query(Post).order_by(Post.id.desc()).first()

        if form.link_href.data:
            post.link_href = form.link_href.data
            post.link_description = form.link_description.data

        if form.main_photo.data:
            main_image = form.main_photo.data
            filename = (
                    "image"
                    + str(post.id)
                    + os.path.splitext(main_image.filename)[1])
            path_plus_filename = os.path.join(
                    'mammothflaskblog/static/images', filename)
            main_image.save(path_plus_filename)
            main_image_filename_for_db = os.path.join(
                    'images', filename)
            post.main_image_filename = main_image_filename_for_db

        if form.extra_photos.data != ['']:
            extra_images = form.extra_photos.data
            letters = 'ABCDEFGHIJ'
            extra_image_count = 0
            extra_image_list_string = ""
            for image in extra_images:
                filename = (
                        "image"
                        + str(post.id)
                        + letters[extra_image_count]
                        + os.path.splitext(image.filename)[1])
                path_plus_filename = os.path.join(
                        'mammothflaskblog/static/images', filename)
                image.save(path_plus_filename)
                if extra_image_count > 0:
                    extra_image_list_string += '|' + os.path.join(
                            'images', filename)
                else:
                    extra_image_list_string += os.path.join(
                            'images', filename)
                extra_image_count += 1
                if extra_image_count == 10:
                    break
            post.number_of_extra_images = extra_image_count
            post.extra_images_filenames = extra_image_list_string

        db.session.commit()
        flash("Add optional captions then hit submit at the bottom of the screen to create your post!",
                'success')
        return redirect(f"/post/{str(post.id)}/update")
    return render_template('create_post.html',
                           title='New Post',
                           form=form,
                           legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    carousel_slides = CarouselSlider.query.order_by(
            CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    post = Post.query.get_or_404(post_id)

    image_filename_caption_dict = dict()
    if post.extra_images_filenames:

        for item in enumerate(post.extra_images_filenames.split('|')):
            if "~" in item[1]:
                caption = item[1].split("~")[1]
                filename = item[1].split("~")[0]
            else:
                caption = "No caption"
                filename = item[1]

            image_filename_caption_dict[item[0]] = [caption, filename]

    facebook_share_link = "https://www.mammothflaskblog.org/post/" + str(post_id)

    return render_template(
            'post.html', title=post.title, post=post,
            image_filename_caption_dict=image_filename_caption_dict,
            facebook_share_link=facebook_share_link,
            carousel_slides1=carousel_slides1,
            carousel_slides2=carousel_slides2)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.main_image_caption = form.main_photo_caption.data
        post.link_href = form.link_href.data
        post.link_description = form.link_description.data
        db.session.commit()

        if form.main_photo.data:
            if post.main_image_filename:
                file_path_to_delete = (
                                       "mammothflaskblog/static/"
                                       + post.main_image_filename)
                if os.path.isfile(file_path_to_delete):
                    os.remove(file_path_to_delete)
            main_image = form.main_photo.data
            filename = (
                    "image"
                    + str(post.id)
                    + os.path.splitext(main_image.filename)[1])
            path_plus_filename = os.path.join(
                    'mammothflaskblog/static/images', filename)
            main_image.save(path_plus_filename)
            main_image_filename_for_db = os.path.join(
                    'images', filename)
            post.main_image_filename = main_image_filename_for_db
            db.session.commit()

        extra_files_submitted = False
        if form.extra_photos.data != ['']:
            if post.extra_images_filenames:
                filenames_to_delete = post.extra_images_filenames.split('|')
                for file_to_delete in filenames_to_delete:
                    if "~" in file_to_delete:
                        file_to_delete = file_to_delete.split("~")[0]
                    file_path_to_delete = (
                            "mammothflaskblog/static/"
                            + file_to_delete)
                    if os.path.isfile(file_path_to_delete):
                        os.remove(file_path_to_delete)

            extra_images = form.extra_photos.data
            letters = 'ABCDEFGHIJ'
            extra_image_count = 0
            extra_image_list_string = ""
            for image in extra_images:
                filename = (
                        "image"
                        + str(post.id)
                        + letters[extra_image_count]
                        + os.path.splitext(image.filename)[1])
                path_plus_filename = os.path.join(
                        'mammothflaskblog/static/images', filename)
                image.save(path_plus_filename)
                if extra_image_count > 0:
                    extra_image_list_string += '|' + os.path.join(
                            'images', filename)
                else:
                    extra_image_list_string += os.path.join(
                            'images', filename)
                extra_image_count += 1
                if extra_image_count == 10:
                    break
            post.number_of_extra_images = extra_image_count
            post.extra_images_filenames = extra_image_list_string
            db.session.commit()
            extra_files_submitted = True

        if form.extra_photos_captions.entries and not extra_files_submitted:
            extra_images = post.extra_images_filenames.split("|")
            for count in range(len(extra_images)):
                if "~" in extra_images[count]:
                    extra_images[count] = extra_images[count].split("~")[0]
            captions = form.extra_photos_captions.data
            image_caption_dict = dict()
            for count in range(len(extra_images)):
                image_caption_dict[count] = [
                        extra_images[count], captions[count]]

            letters = 'ABCDEFGHIJ'
            extra_image_count = 0
            extra_image_list_string = ""
            for count,image_caption_entry in image_caption_dict.items():
                filename = (
                        "image"
                         + str(post.id)
                         + letters[count]
                         + os.path.splitext(image_caption_entry[0])[1])
                if extra_image_count > 0:
                    extra_image_list_string += (
                            '|'
                            + os.path.join('images', filename)
                            + "~" + image_caption_entry[1])
                else:
                    extra_image_list_string += (
                            os.path.join('images', filename)
                            + "~"
                            + image_caption_entry[1])
                extra_image_count += 1
                if extra_image_count == 10:
                    break

            post.number_of_extra_images = extra_image_count
            post.extra_images_filenames = extra_image_list_string
            db.session.commit()

        flash('Your post has been updated :)', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.main_photo_caption.data = post.main_image_caption

    image_filename_caption_dict = dict()
    if post.extra_images_filenames:
        for item in enumerate(post.extra_images_filenames.split('|')):
            if "~" in item[1]:
                caption = item[1].split("~")[1]
                filename = item[1].split("~")[0]
            else:
                caption = "No caption"
                filename = item[1]
            image_filename_caption_dict[item[0]] = [caption, filename]

    return render_template('create_post.html', title='Update Post',
            form=form, post=post,
            image_filename_caption_dict=image_filename_caption_dict,
            legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    if post.main_image_filename:
        file_path_to_delete = ("mammothflaskblog/static/"
                             + post.main_image_filename)
        if os.path.isfile(file_path_to_delete):
            os.remove(file_path_to_delete)

    if post.extra_images_filenames:
        filenames_to_delete = post.extra_images_filenames.split('|')
        for count in range(len(filenames_to_delete)):
            if "~" in filenames_to_delete[count]:
                filenames_to_delete[count] = (
                        filenames_to_delete[count].split("~")[0])

        for file_to_delete in filenames_to_delete:

            file_path_to_delete = (
                    "mammothflaskblog/static/"
                   + file_to_delete)
            if os.path.isfile(file_path_to_delete):
                os.remove(file_path_to_delete)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.', 'success')
    return redirect(url_for('main.home'))