from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repo as member_repo
import repositories.booking_repo as booking_repo 
import repositories.session_repo as session_repo 

member_repo.delete_all()
#Create instances of members
member1 = Member("John", "Smith", "EH3", False)
member2 = Member("Sara", "Cox", "EH4", True)
member3 = Member("David", "Keen", "EH1", True)
#save the members
member_repo.save(member1)
member_repo.save(member2)
member_repo.save(member3)

session_repo.delete_all()
#Create instances of sessions and save
session1 = Session("Muy Thai", 90, True, "Sunday", "5PM")
session2 = Session("Extreme Spin", 30, False, "Monday", "9AM")
#save the sessons
session_repo.save(session1)
session_repo.save(session2)

booking_repo.delete_all_bookings()
#Create bookings
booking_repo.save(member2,session1)
booking_repo.save(member1,session2)
booking_repo.save(member3,session1)
