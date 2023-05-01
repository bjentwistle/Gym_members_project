from flask import render_template, redirect, request
from flask import Blueprint
from models.member import *

import repositories.member_repo as member_repo
import repositories.booking_repo as booking_repo 
import repositories.session_repo as session_repo 

sessions_blueprint = Blueprint("sessions", __name__)


# @sessions_blueprint.route("/home")
# def home():
#     return render_template('index.jinja', title = "Home Page")