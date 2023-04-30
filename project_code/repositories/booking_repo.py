from db.run_sql import run_sql

from models.booking import Booking

#Need to be able to save gym sessions to the table
def save(members_id, sessions_id):
    booking =[]
    sql = "INSERT INTO bookings (members_id, sessions_id) VALUES (%s,%s) RETURNING id"
    values = [members_id, sessions_id]
    results = run_sql(sql, values)
    booking_id = results[0]["id"] 
    booking = Booking[results[members_id], results[sessions_id], booking_id]
    return booking


# def users_for_location(location):
#     users = []

#     sql = "SELECT users.* FROM users INNER JOIN visits ON visits.user_id = users.id WHERE location_id = %s"
#     values = [location.id]
#     results = run_sql(sql, values)

#     for row in results:
#         user = User(row['name'], row['id'])
#         users.append(user)

#     return users

# #Need to be able to select members by theri ID
# def select(id):
#     session = None
#     sql = "SELECT * FROM sessions WHERE id = %s "
#     values = [id]
#     results = run_sql(sql, values)
    
#     if results:
#         result = results[0]
#         session = Session(result['name'], result['duration'], result['premium_session'], result['id'])
#     return session

# #Need a function to select all the rows in the table of members 
# def select_all():
#     sessions = []
#     sql = "SELECT * FROM sessions"
#     results = run_sql(sql)
#     if results:
#         for result in results:
#             session = Session(result['name'], result['duration'], result['premium_session'], result['id'])
#             sessions.append(session)
#     return sessions

#Delete all rows from the members table
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)