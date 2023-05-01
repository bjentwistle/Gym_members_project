from db.run_sql import run_sql

from models.booking import Booking

#Need to be able to save gym sessions to the table
def save(member, session):
    member_id = member.id
    session_id = session.id
    sql = "INSERT INTO bookings (members_id, sessions_id) VALUES (%s, %s) RETURNING id"
    values = [member_id, session_id]
    results = run_sql(sql, values)
    booking_id = results[0]["id"] 
    return booking_id

#Need to be able to select booking by its ID
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s "
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        booking = Booking(result['members_id'], result['sessions_id'], result['id'])
    return booking

#Need a function to select all the rows in the table of bookings
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    if results:
        for result in results:
            booking = Booking(result['members_id'], result['sessions_id'], result['id'])
            bookings.append(booking)
            #print(booking)
    return bookings

#Delete all rows from the bookings table - used for tesing purposes only
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


#Show all members in one booking