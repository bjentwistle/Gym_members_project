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
    session = session_repo.select(session_id)
    member_id = request.form['member_id']
    member = member_repo.select(member_id)
    #check if premium session, don't allow nome premium members to be booked.
    if session.premium_session and not member.premium_member: #refactored to reduce lines of code
        return redirect("/bookings/new")
    
    bookings = booking_repo.select_all()
    if bookings != None:
        for booking in bookings:
            #print("Member id", booking.member.id)
            if booking.member.id == int(member_id) and booking.session.id == int(session_id):
                #print("Booking, member id", booking.member.id)
                return redirect("/bookings/new")

    # Member not found in any existing booking, save the new booking.
    booking_repo.save(member, session)
    return redirect("/bookings")