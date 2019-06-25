from datetime import datetime
from mammothflaskblog import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	main_image_filename = db.Column(db.Text)
	main_image_caption = db.Column(db.String(150))
	number_of_extra_images = db.Column(db.Integer)
	extra_images_filenames = db.Column(db.Text)
	link_href = db.Column(db.String(150))
	link_description = db.Column(db.Text)
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

class Issue(db.Model):
	issue_number = db.Column(db.Integer, nullable=False, primary_key=True)
	year = db.Column(db.Integer, nullable=False)
	month = db.Column(db.Text, nullable=False)
	pdf_filename = db.Column(db.Text)
	thumbnail_filename = db.Column(db.Text)
	def __repr__(self):
		return f"Issue('{self.issue_number}', '{self.month}', '{self.year}')"

class TextAndImage(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	text_part = db.Column(db.Text)
	image_filename = db.Column(db.Text)
	def __repr__(self):
		return f"TextAndImage('{self.id}', '{self.image_filename}', '{self.text_part}')"

class CarouselSlider(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	caption = db.Column(db.String(500))
	image_filename = db.Column(db.String(300))
	def __repr__(self):
		return f"CarouselSlider('{self.id}', '{self.image_filename}', '{self.caption}')"


class NBAStat(db.Model):
	__tablename__ = "nba_stat"
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	name = db.Column(db.String(50))
	position = db.Column(db.String(2))
	age = db.Column(db.Integer, nullable=False)
	team = db.Column(db.String(3))
	games = db.Column(db.Integer, nullable=False)
	games_started = db.Column(db.Integer, nullable=False)
	minutes_played = db.Column(db.Integer, nullable=False)
	points = db.Column(db.Integer, nullable=False)
	field_goals = db.Column(db.Integer, nullable=False)
	field_goal_attempts = db.Column(db.Integer, nullable=False)
	field_goal_percentage = db.Column(db.NUMERIC(precision=4))
	three_point_shots_made = db.Column(db.Integer, nullable=False)
	three_point_attempts = db.Column(db.Integer, nullable=False)
	three_point_percentage = db.Column(db.NUMERIC(precision=4))
	two_point_shots_made = db.Column(db.Integer, nullable=False)
	two_point_attempts = db.Column(db.Integer, nullable=False)
	two_point_percentage = db.Column(db.NUMERIC(precision=4))
	free_throws_made = db.Column(db.Integer, nullable=False)
	free_throw_attempts = db.Column(db.Integer, nullable=False)
	free_throw_percentage = db.Column(db.NUMERIC(precision=4))
	offensive_rebounds = db.Column(db.Integer, nullable=False)
	defensive_rebounds = db.Column(db.Integer, nullable=False)
	total_rebounds = db.Column(db.Integer, nullable=False)
	assists = db.Column(db.Integer, nullable=False)
	steals = db.Column(db.Integer, nullable=False)
	blocks = db.Column(db.Integer, nullable=False)
	turnovers = db.Column(db.Integer, nullable=False)
	personal_fouls = db.Column(db.Integer, nullable=False)
	def __repr__(self):
		return f"NBAStat('{self.name}', '{self.team}', '{self.position}')"