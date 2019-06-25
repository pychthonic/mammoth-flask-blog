from flask import render_template, request, Blueprint
from mammothflaskblog.models import Post, Issue, CarouselSlider
from mammothflaskblog.config import Config

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    carousel_slides = CarouselSlider.query.order_by(CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', title=Config.SITE_NAME, posts=posts, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)


@main.route("/linux-for-you")
def linux_for_you():
    carousel_slides = CarouselSlider.query.order_by(CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    issue = Issue.query.order_by(Issue.issue_number.desc()).first()
    return render_template('linux_for_you.html', title="Linux For You", issue=issue, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)


@main.route("/links-of-interest")
def links_of_interest():
    carousel_slides = CarouselSlider.query.order_by(CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)
    return render_template('links_of_interest.html', title="Organizations of Interest", carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)

