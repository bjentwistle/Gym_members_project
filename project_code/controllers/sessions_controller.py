from flask import render_template, redirect, request
from flask import Blueprint
from models.session import *

import repositories.member_repo as member_repo
import repositories.booking_repo as booking_repo 
import repositories.session_repo as session_repo 

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def show_all_sessions():
    sessions = session_repo.select_all()
    return render_template('/sessions/sessions.jinja', title = "All sessions page", sessions = sessions)

@sessions_blueprint.route("/sessions/<id>")
def show_session_index(id):
    session = session_repo.select(id)
    members = member_repo.get_members_in_session(id)
    return render_template("sessions/single_session.jinja", id=id, session = session, members = members)

@sessions_blueprint.route('/sessions/new')
def add_session():
    return render_template('sessions/new.jinja')

@sessions_blueprint.route('/sessions/new', methods = ["POST"])
def submit_session():
    name = request.form['name']
    duration = request.form['duration']
    what_day = request.form['what_day']
    what_time = request.form['what_time']
    premium_session = True if 'premium_session' in request.form else False 
    new_session = Session(name, duration, premium_session, what_day, what_time)
    session_repo.save(new_session)
    return redirect("/sessions")

# EDIT - GET '/sessions/<id>/edit'
@sessions_blueprint.route('/sessions/<id>/edit')
def edit_session(id):
    edit_session = session_repo.select(id)
    return render_template('sessions/edit.jinja', session = edit_session)

# UPDATE - PUT '/sessions/<id>/edit'
@sessions_blueprint.route("/sessions/<id>/edit", methods=['POST'])
def update_session(id):
    session_repo.select(id)
    name = request.form['name']
    duration = request.form['duration']
    premium_session = request.form["premium_session"]
    what_day = request.form['what_day']
    what_time = request.form['what_time']
    edit_session = Session(name, duration, premium_session, what_day, what_time, id)
    session_repo.update(edit_session)
    return redirect('/sessions')

