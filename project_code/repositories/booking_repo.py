from db.run_sql import run_sql

from models.booking import Booking

from repositories import member_repo
from repositories import session_repo

#Need to be able to save gym sessions to the table
def save(member, session):
    member_id = member.id
    session_id = session.id
    sql = "INSERT INTO bookings (members_id, sessions_id) VALUES (%s, %s) RETURNING id"
    values = [member_id, session_id]
    results = run_sql(sql, values)
    booking_id = results[0]["id"] 
    booking = Booking(member, session, booking_id)
    print(booking.member.first_name)
    return booking

#Need to be able to select booking by its ID
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s "
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        id = results[0]['id']
        member = member_repo.select(results['members_id'])
        session = session_repo.select(['sessions_id'])
        booking = Booking(member, session, id)
    return booking

#Need a function to select all the rows in the table of bookings
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    print("Here are your resulst:", results)

    for row in results:
        member_id = row['members_id']
        session_id = row['sessions_id']
        member = member_repo.select(member_id)
        session = session_repo.select(session_id)
        booking = Booking(member, session)
        bookings.append(booking)
    return bookings

#Delete all rows from the bookings table - used for tesing purposes only
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


#Show all members in one booking