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
    sql = " SELECT bookings.id, members.first_name, members.last_name, sessions.name FROM ((bookings INNER JOIN members ON bookings.members_id = members.id) INNER JOIN sessions ON bookings.sessions_id = sessions.id)"
    results = run_sql(sql)
    print(results)
    # [[1, 'Sara', 'Cox', 'Muy Thai'], 
    # [2, 'John', 'Smith', 'Extreme Spin'], 
    # [3, 'David', 'Keen', 'Muy Thai']]
    if results:
        for result in results:
            booking = [result['first_name'], result['last_name'], result['name'], result['id']]
            #first_name = result["members.first_name"]
            bookings.append(booking)
    return bookings
    return results

#Delete all rows from the bookings table - used for tesing purposes only
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


#Show all members in one booking