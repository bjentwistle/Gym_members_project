from db.run_sql import run_sql

from models.session import Session

#Need to be able to save gym sessions to the table
def save(session):
    sql = "INSERT INTO sessions (name, duration, premium_session) VALUES (%s,%s,%s) RETURNING id"
    values = [session.name, session.duration, session.premium_session]
    results = run_sql(sql, values)
    session.id = results[0]["id"] 
    return session

#Need to be able to select members by their ID
def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s "
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        session = Session(result['name'], result['duration'], result['premium_session'], result['id'])
    return session

#Need a function to select all the rows in the table of members 
def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    if results:
        for result in results:
            session = Session(result['name'], result['duration'], result['premium_session'], result['id'])
            sessions.append(session)
        sessions.sort(key=lambda x: x.name) #from google 'sorting an object' so my sessions list stays in alphabetical order after updating. 
    return sessions

def update(session):
    sql = "UPDATE sessions SET (name, duration, premium_session) = (%s, %s, %s) WHERE id = %s"
    values = [session.name, session.duration, session.premium_session, session.id]
    run_sql(sql, values)

#Delete all rows from the sessions table - used for tesing purposes only
def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)