from flask import render_template, request, Blueprint
from mammothflaskblog.models import NBAStat, CarouselSlider
from mammothflaskblog.config import Config
from mammothflaskblog.nba_stat.forms import NBAStatForm

nba_stat = Blueprint('nba_stat', __name__)




@nba_stat.route("/nba-stats", methods=['GET', 'POST'])
def search_nba_stats():
    carousel_slides = CarouselSlider.query.order_by(CarouselSlider.id.desc())
    carousel_slides1 = enumerate(carousel_slides)
    carousel_slides2 = enumerate(carousel_slides)

    form = NBAStatForm()

    if form.validate_on_submit():
        players_found = NBAStat.query.order_by(NBAStat.id)
        if form.name.data:
            players_found = players_found.filter_by(name=form.name.data.split(', ')[0])
            players_found = players_found.filter_by(team=form.name.data.split(', ')[1])
        if form.position.data:
            players_found = players_found.filter_by(position=form.position.data)
        if form.team.data:
            players_found = players_found.filter_by(team=form.team.data)

        if form.age.data:
            if form.age_range.data == ">=":
                players_found = players_found.filter(NBAStat.age >= form.age.data)
            elif form.age_range.data == "<=":
                players_found = players_found.filter(NBAStat.age <= form.age.data)
            else:
                players_found = players_found.filter_by(age=form.age.data)

        if form.games.data:
            if form.games_range.data == ">=":
                players_found = players_found.filter(NBAStat.games >= form.games.data)
            elif form.games_range.data == "<=":
                players_found = players_found.filter(NBAStat.games <= form.games.data)
            else:
                players_found = players_found.filter_by(games=form.games.data)

        if form.games_started.data:
            if form.games_started_range.data == ">=":
                players_found = players_found.filter(NBAStat.games_started >= form.games_started.data)
            elif form.games_started_range.data == "<=":
                players_found = players_found.filter(NBAStat.games_started <= form.games_started.data)
            else:
                players_found = players_found.filter_by(games_started=form.games_started.data)

        if form.minutes_played.data:
            if form.minutes_range.data == ">=":
                players_found = players_found.filter(NBAStat.minutes_played >= form.minutes_played.data)
            elif form.minutes_range.data == "<=":
                players_found = players_found.filter(NBAStat.minutes_played <= form.minutes_played.data)
            else:
                players_found = players_found.filter_by(minutes_played=form.minutes_played.data)

        if form.points.data:
            if form.points_range.data == ">=":
                players_found = players_found.filter(NBAStat.points >= form.points.data)
            elif form.points_range.data == "<=":
                players_found = players_found.filter(NBAStat.points <= form.points.data)
            else:
                players_found = players_found.filter_by(points=form.points.data)

        if form.field_goals.data:
            if form.field_goal_range.data == ">=":
                players_found = players_found.filter(NBAStat.field_goals >= form.field_goals.data)
            elif form.field_goal_range.data == "<=":
                players_found = players_found.filter(NBAStat.field_goals <= form.field_goals.data)
            else:
                players_found = players_found.filter_by(field_goals=form.field_goals.data)

        if form.field_goal_attempts.data:
            if form.field_goal_attempts_range.data == ">=":
                players_found = players_found.filter(NBAStat.field_goal_attempts >= form.field_goal_attempts.data)
            elif form.field_goal_attempts_range.data == "<=":
                players_found = players_found.filter(NBAStat.field_goal_attempts <= form.field_goal_attempts.data)
            else:
                players_found = players_found.filter_by(field_goal_attempts=form.field_goal_attempts.data)


        return render_template('nba_stat_search_results.html', title=Config.SITE_NAME, players_found=players_found, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)

    return render_template('nba_stat_search.html', title=Config.SITE_NAME, form=form, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)




"""
    name = StringField('Name', validators=[Length(max=50)])
    position = StringField('Position', validators=[Length(max=2)])
    age = IntegerField('Age')
    team = StringField('Team', validators=[Length(max=3)])
    games = IntegerField('Games Played')
    games_started = IntegerField('Games Started')
    minutes_played = IntegerField('Minutes Played')
    field_goals = IntegerField('Points')
    field_goals = IntegerField('Field Goals')
    field_goal_attempts = IntegerField('Field Goal Attempts')
    field_goal_percentage = DecimalField('Field Goal Percentage', places=3)
    three_point_shots_made = IntegerField('Three Point Shots Made')
    three_point_attempts = IntegerField('Three Point Attempts')
    three_point_percentage = DecimalField('Three Point Percentage', places=3)
    two_point_shots_made = IntegerField('Two Point Shots Made')
    two_point_attempts = IntegerField('Two Point Attempts')
    two_point_percentage = DecimalField('Two Point Percentage', places=3)
    free_throws_made = IntegerField('Free Throws Made')
    free_throw_attempts = IntegerField('Free Throw Attempts')
    free_throw_percentage = DecimalField('Free Throw Percentage', places=3)
    offensive_rebounds = IntegerField('Offensive Rebounds')
    defensive_rebounds = IntegerField('Defensive Rebounds')
    total_rebounds = IntegerField('Total Rebounds')
    assists = IntegerField('Assists')
    steals = IntegerField('Steals')
    blocks = IntegerField('Blocks')
    turnovers = IntegerField('Turnovers')
    personal_fouls = IntegerField('Personal Fouls')
"""