from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mammothflaskblog import db, bcrypt
from mammothflaskblog.models import User, Post, CarouselSlider
from mammothflaskblog.users.forms import LoginForm


users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
	carousel_slides = CarouselSlider.query.order_by(CarouselSlider.id.desc())
	carousel_slides1 = enumerate(carousel_slides)
	carousel_slides2 = enumerate(carousel_slides)
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:	
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)

@users.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('main.home'))

@users.route("/account")
@login_required
def account():
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file)


@users.route("/user/<string:username>")
def user_posts(username):
	carousel_slides = CarouselSlider.query.order_by(CarouselSlider.id.desc())
	carousel_slides1 = enumerate(carousel_slides)
	carousel_slides2 = enumerate(carousel_slides)
	page = request.args.get('page', 1, type=int)
	user = User.query.filter_by(username=username).first_or_404()
	posts = Post.query.filter_by(author=user)\
    		.order_by(Post.date_posted.desc())\
    		.paginate(page=page, per_page=3)
	return render_template('user_posts.html', posts=posts, user=user, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)