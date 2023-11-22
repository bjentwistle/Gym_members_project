from db.run_sql import run_sql

#from models.session import Session
from models.member import Member

#Need to be able to save members to the table
def save(member):
    sql = "INSERT INTO members (first_name, last_name, postcode, premium_member) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [member.first_name, member.last_name, member.postcode, member.premium_member]
    results = run_sql(sql, values)
    member.id = results[0]["id"]  #added to member
    #print("Member id from member_repo.save  = " , member.id)
    return member

#Need to be able to select members by their ID
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s "
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['postcode'], result['premium_member'], result['id'])
    return member

#Need a function to select all the rows in the table of members 
def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    if results:
        for result in results:
            member = Member(result['first_name'], result['last_name'], result['postcode'], result['premium_member'], result['id'])
            members.append(member)
            members.sort(key=lambda x: x.last_name) #shows members in alphabetical order by last name.
    return members

def update(member):
    sql = "UPDATE members SET (first_name, last_name, postcode, premium_member) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.postcode, member.premium_member, member.id]
    run_sql(sql, values)

def get_members_in_session(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.members_id WHERE sessions_id = %s"
    values = id
    results = run_sql(sql, values)
    for row in results:
        member = row
        members.append(member)
    return members

#Delete all rows from the members table - used for tesing purposes only
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)