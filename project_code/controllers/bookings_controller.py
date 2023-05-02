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

@bookings_blueprint.route("/bookings/new")
def add_session():
    members = member_repo.select_all()
    sessions = session_repo.select_all()
    return render_template('bookings/new.jinja', members = members, sessions = sessions)

@bookings_blueprint.route("/bookings/new", methods = ["POST"])
def submit_new_booking():
    session_id = request.form['session_id']
    member_id = request.form['member_id']
    premium_member = 'premium_member' in request.form
    
    member = member_repo.select(member_id)
    print(member)
    session = session_repo.select(session_id)
    print(session)
    if premium_member == session.premium_session:

        booking_repo.save(member, session)
        return redirect("/bookings")
    else:

        return redirect("/bookings/new")