from flask import render_template, redirect, request
from flask import Blueprint
from models.member import *

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
    return render_template("sessions/single_session.jinja", session = session)

