from flask import abort
from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_login import login_required
from mammothflaskblog import db
from mammothflaskblog.models import CarouselSlider
from mammothflaskblog.models import Issue
from mammothflaskblog.linux_for_you.forms import LinuxForYouForm
from pdf2image import convert_from_path

import os


issues = Blueprint('issues', __name__)


@issues.route("/linux-for-you/new", methods=['GET', 'POST'])
@login_required
def new_issue():

    form = LinuxForYouForm()
    if form.validate_on_submit():

        row_to_delete = Issue.query.filter_by(
                issue_number=form.issue_number.data).first()
        if row_to_delete:
            pdf_to_delete = row_to_delete.pdf_filename
            pdf_to_delete_with_path = os.path.join(
                    'mammothflaskblog/static', pdf_to_delete)
            os.remove(pdf_to_delete_with_path)

            thumbnail_to_delete = row_to_delete.thumbnail_filename
            thumbnail_to_delete_with_path = os.path.join(
                    'mammothflaskblog/static', thumbnail_to_delete)
            os.remove(thumbnail_to_delete_with_path)

            db.session.delete(row_to_delete)
            db.session.commit()

        issue = Issue(issue_number=str(form.issue_number.data), 
                    year=form.year.data, 
                    month=form.month.data)

        if form.linux_for_you_pdf.data:
            new_issue = form.linux_for_you_pdf.data
            filename_pdf = "linux_for_you_issue_" 
                         + str(issue.issue_number)
                         + "_"
                         + issue.month
                         + "_"
                         + str(issue.year)
                         + ".pdf"
            path_plus_filename_pdf = os.path.join(
                    'mammothflaskblog/static/pdfs', filename_pdf)
            new_issue.save(path_plus_filename_pdf)

            thumbnail_image = convert_from_path(
                    path_plus_filename_pdf,
                    output_folder='mammothflaskblog/static/pdfs',
                    first_page=1,
                    last_page=1,
                    fmt='jpg')

            filename_thumbnail = "linux_for_you_issue_"
                                + str(issue.issue_number)
                                + "_" + issue.month
                                + "_"
                                + str(issue.year)
                                + "_thumbnail"
                                + ".jpg"
            path_plus_filename_thumbnail = os.path.join(
                    'mammothflaskblog/static/pdfs',
                    filename_thumbnail)

            os.rename(thumbnail_image[0].filename,
                      path_plus_filename_thumbnail)

            new_issue_filename_pdf_for_db = os.path.join(
                    'pdfs', filename_pdf)
            issue.pdf_filename = new_issue_filename_pdf_for_db

            new_issue_filename_thumbnail_for_db = os.path.join(
                    'pdfs', filename_thumbnail)
            issue.thumbnail_filename = new_issue_filename_thumbnail_for_db

            db.session.add(issue)
            db.session.commit()

        flash('Your pdf has been uploaded!', 'success')
        return redirect(url_for('main.home'))

    return render_template('upload_linux_for_you.html',
                           title='Upload Linux For You',
                           form=form,
                           legend='Upload Linux For You')


@issues.route("/linux-for-you/<int:issue_number>")
def issue(issue_number):
    issue = Issue.query.filter_by(issue_number=issue_number).first()
    if not issue:
        abort(404)
    return render_template(
            'view_issue.html',
            title=f"View Linux For You Issue {issue_number}",
            issue=issue.pdf_filename)


@issues.route("/linux-for-you/back-issues")
def back_issues():

    issues = Issue.query.order_by(Issue.issue_number.desc())
    return render_template('back_issues.html',
                           title="Back Issues of Linux For You",
                           issues=issues)