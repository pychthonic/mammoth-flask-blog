from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from mammothflaskblog.config import Config


db = SQLAlchemy()

bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    db.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)


    from mammothflaskblog.users.routes import users
    from mammothflaskblog.posts.routes import posts
    from mammothflaskblog.main.routes import main
    from mammothflaskblog.linux_for_you.routes import issues
    from mammothflaskblog.submit_info.routes import submit_info
    from mammothflaskblog.about.routes import about_the_project
    from mammothflaskblog.image_text_display.routes import image_text_display
    from mammothflaskblog.carousel_slider.routes import carousel_slider
    from mammothflaskblog.nba_stat.routes import nba_stat


    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(issues)
    app.register_blueprint(submit_info)
    app.register_blueprint(about_the_project)
    app.register_blueprint(image_text_display)
    app.register_blueprint(carousel_slider)
    app.register_blueprint(nba_stat)

    with app.app_context():
        db.create_all()

    return app