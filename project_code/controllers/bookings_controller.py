from flask import flash, render_template, redirect, request
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
    return render_template("/bookings/bookings.jinja", title = "All bookings", bookings = bookings, sessions= sessions)

@bookings_blueprint.route("/bookings/new")
def add_new_booking_to_session():
    sessions = session_repo.select_all()
    members = member_repo.select_all()
    return render_template('bookings/new.jinja', title = "New booking", members = members , sessions = sessions)

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
            #print("booking id", booking.member.id)
            if booking.member.id == int(member_id) and booking.session.id == int(session_id):
                #print("Booking, booking id", booking.member.id)
                return redirect("/bookings/new")

    # booking not found in any existing booking, save the new booking.
    booking_repo.save(member, session)
    return redirect("/bookings")


@bookings_blueprint.route("/bookings/<id>")
def show_booking_index(id):
    booking = booking_repo.select(id)
    if booking is None:
        # Handle the case where the booking doesn't exist
        return redirect("/bookings")  # Redirect back to bookings page or show an error

    # Fetch member and session details for the booking
    # member = member_repo.select(booking.members_id)
    # session = session_repo.select(booking.sessions_id)

    return render_template("/bookings/single_booking.jinja", title = "Booking details", booking=booking)


# New route to handle booking deletion
@bookings_blueprint.route("/bookings/delete/<int:booking_id>", methods=["GET"])
def delete_booking(booking_id):
    # Find the booking by its ID
    booking = booking_repo.select(booking_id)

    if booking is None:
        # Handle the case where the booking doesn't exist
        flash("Booking not found", "error")
        return redirect("/bookings")  # Redirect back to bookings page or show an error

    # Delete the booking
    booking_repo.delete(booking_id)

    # Redirect to the bookings page (or any other appropriate page)
   
    return redirect("/bookings")

