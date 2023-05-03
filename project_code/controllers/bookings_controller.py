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
    sessions = session_repo.select_all()
    return render_template("/bookings/bookings.jinja", bookings = bookings, sessions= sessions)

@bookings_blueprint.route("/bookings/new")
def add_new_booking_to_session():
    sessions = session_repo.select_all()
    members = member_repo.select_all()

    return render_template('bookings/new.jinja', members = members , sessions = sessions)

@bookings_blueprint.route("/bookings/new", methods = ["POST"])
def submit_new_booking():
    session_id = request.form['session_id']
    member_id = request.form['member_id']
    
    member = member_repo.select(member_id)
    session = session_repo.select(session_id)

    booking_repo.save(member, session)
    return redirect("/bookings")

#to view all the bookings for one session  
# @bookings_blueprint.route("/bookings/booked_members")  
# #@bookings_blueprint.route("/bookings/<id>/booked_members")  
# def view_session_bookings():

#     session_id = request.form['session_id']
#     results = booking_repo.view_session(id)
#     session = session_repo.select(id)

#     return render_template("/bookings/booked_members.jinja", bookings = results, session = session)
