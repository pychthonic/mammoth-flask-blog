from flask import render_template, request, Blueprint
from mammothflaskblog.models import NBAStat, CarouselSlider
from mammothflaskblog.config import Config
from mammothflaskblog.nba_stat.forms import NBAStatForm

nba_stat = Blueprint('nba_stat', __name__)


team_name_dict = {"ATL": "Atlanta Hawks", "BOS": "Boston Celtics", "BRK": "Brooklyn Nets", "CHI": "Chicago Bulls", 
            "CHO": "Charlotte Hornets", "CLE": "Cleveland Cavaliers", "DAL": "Dallas Mavericks", "DEN": "Denver Nuggets", 
            "DET": "Detroit Pistons", "GSW": "Golden State Warriors", "HOU": "Houston Rockets", "IND": "Indiana Pacers",
            "LAC": "Los Angeles Clippers", "LAL": "Los Angeles Lakers", "MEM": "Memphis Grizzlies", "MIA": "Miami Heat",
            "MIL": "Milwaukee Bucks", "MIN": "Minnesota Timberwolves", "NOP": "New Orleans Pelicans", "NYK": "New York Knicks", 
            "OKC": "Oklahoma City Thunder", "ORL": "Orlando Magic", "PHI": "Philadelphia Seventy-Sixers", 
            "PHO": "Phoenix Suns", "POR": "Portland Trail Blazers", "SAC": "Sacramento Kings", "SAS": "San Antonio Spurs", 
            "TOR": "Toronto Raptors", "UTA": "Utah Jazz", "WAS": "Washington Wizards",
            "TOT": "Multiple Teams / Full season stats for player traded mid-season"}

position_dict = {"PG": "Point Guard", "SG": "Shooting Guard", "SF": "Small Forward", "PF": "Power Forward",
                 "C": "Center"}


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

        if form.field_goal_percentage.data:
            if form.field_goal_percentage_range.data == ">=":
                players_found = players_found.filter(NBAStat.field_goal_percentage >= form.field_goal_percentage.data/100)
            elif form.field_goal_percentage_range.data == "<=":
                players_found = players_found.filter(NBAStat.field_goal_percentage <= form.field_goal_percentage.data/100)

        if form.three_point_shots_made.data:
            if form.three_point_shots_made_range.data == ">=":
                players_found = players_found.filter(NBAStat.three_point_shots_made >= form.three_point_shots_made.data)
            elif form.three_point_shots_made_range.data == "<=":
                players_found = players_found.filter(NBAStat.three_point_shots_made <= form.three_point_shots_made.data)

        if form.three_point_attempts.data:
            if form.three_point_attempts_range.data == ">=":
                players_found = players_found.filter(NBAStat.three_point_attempts >= form.three_point_attempts.data)
            elif form.three_point_attempts_range.data == "<=":
                players_found = players_found.filter(NBAStat.three_point_attempts <= form.three_point_attempts.data)

        if form.three_point_percentage.data:
            if form.three_point_percentage_range.data == ">=":
                players_found = players_found.filter(NBAStat.three_point_percentage >= form.three_point_percentage.data/100)
            elif form.three_point_percentage_range.data == "<=":
                players_found = players_found.filter(NBAStat.three_point_percentage <= form.three_point_percentage.data/100)

        if form.two_point_shots_made.data:
            if form.two_point_shots_made_range.data == ">=":
                players_found = players_found.filter(NBAStat.two_point_shots_made >= form.two_point_shots_made.data)
            elif form.two_point_shots_made_range.data == "<=":
                players_found = players_found.filter(NBAStat.two_point_shots_made <= form.two_point_shots_made.data)

        if form.two_point_attempts.data:
            if form.two_point_attempts_range.data == ">=":
                players_found = players_found.filter(NBAStat.two_point_attempts >= form.two_point_attempts.data)
            elif form.two_point_attempts_range.data == "<=":
                players_found = players_found.filter(NBAStat.two_point_attempts <= form.two_point_attempts.data)

        if form.two_point_percentage.data:
            if form.two_point_percentage_range.data == ">=":
                players_found = players_found.filter(NBAStat.two_point_percentage >= form.two_point_percentage.data/100)
            elif form.two_point_percentage_range.data == "<=":
                players_found = players_found.filter(NBAStat.two_point_percentage <= form.two_point_percentage.data/100)

        if form.free_throws_made.data:
            if form.free_throws_made_range.data == ">=":
                players_found = players_found.filter(NBAStat.free_throws_made >= form.free_throws_made.data)
            elif form.free_throws_made_range.data == "<=":
                players_found = players_found.filter(NBAStat.free_throws_made <= form.free_throws_made.data)

        if form.free_throw_attempts.data:
            if form.free_throw_attempts_range.data == ">=":
                players_found = players_found.filter(NBAStat.free_throw_attempts >= form.free_throw_attempts.data)
            elif form.free_throw_attempts_range.data == "<=":
                players_found = players_found.filter(NBAStat.free_throw_attempts <= form.free_throw_attempts.data)

        if form.free_throw_percentage.data:
            if form.free_throw_percentage_range.data == ">=":
                players_found = players_found.filter(NBAStat.free_throw_percentage >= form.free_throw_percentage.data/100)
            elif form.free_throw_percentage_range.data == "<=":
                players_found = players_found.filter(NBAStat.free_throw_percentage <= form.free_throw_percentage.data/100)

        if form.offensive_rebounds.data:
            if form.offensive_rebounds_range.data == ">=":
                players_found = players_found.filter(NBAStat.offensive_rebounds >= form.offensive_rebounds.data)
            elif form.offensive_rebounds_range.data == "<=":
                players_found = players_found.filter(NBAStat.offensive_rebounds <= form.offensive_rebounds.data)

        if form.defensive_rebounds.data:
            if form.defensive_rebounds_range.data == ">=":
                players_found = players_found.filter(NBAStat.defensive_rebounds >= form.defensive_rebounds.data)
            elif form.defensive_rebounds_range.data == "<=":
                players_found = players_found.filter(NBAStat.defensive_rebounds <= form.defensive_rebounds.data)

        if form.total_rebounds.data:
            if form.total_rebounds_range.data == ">=":
                players_found = players_found.filter(NBAStat.total_rebounds >= form.total_rebounds.data)
            elif form.total_rebounds_range.data == "<=":
                players_found = players_found.filter(NBAStat.total_rebounds <= form.total_rebounds.data)

        if form.assists.data:
            if form.assists_range.data == ">=":
                players_found = players_found.filter(NBAStat.assists >= form.assists.data)
            elif form.assists_range.data == "<=":
                players_found = players_found.filter(NBAStat.assists <= form.assists.data)






        players_found_count = players_found.count()
        teams_count = []

        if players_found_count == 0:
            search_summary = "No players found"
        elif players_found_count == 1:
            search_summary = "Found 1 player"
        else:
            for player_found in players_found:
                if team_name_dict[player_found.team] not in teams_count:
                    teams_count.append(team_name_dict[player_found.team])
            if len(teams_count) == 1:
                search_summary = f"Found {players_found_count} players on {len(teams_count)} team"
            else:
                search_summary = f"Found {players_found_count} players on {len(teams_count)} teams"



        return render_template('nba_stat_search_results.html', title=Config.SITE_NAME, position_dict=position_dict, team_name_dict=team_name_dict, players_found=players_found, search_summary=search_summary, carousel_slides1=carousel_slides1, carousel_slides2=carousel_slides2)

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