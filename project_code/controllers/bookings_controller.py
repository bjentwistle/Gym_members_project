from flask import render_template, redirect, request

from flask import Blueprint
from models.booking import *

import repositories.member_repo as member_repo
import repositories.booking_repo as booking_repo 
import repositories.session_repo as session_repo 

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def show_all_bookings():
    bookings = booking_repo.select_all()
    return render_template("/bookings/bookings.jinja", bookings = bookings)