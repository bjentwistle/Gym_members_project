import unittest
from models.member import *
from models.session import *
from models.booking import *


class Testapp(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("John", "Smith", "EH3", False)
        self.member2 = Member("Sara", "Cox", "EH4", True)
        self.member3 = Member("David", "Keen", "EH1", True)

        self.session1 = Session("Muy Thai", 90, True)
        self.session2 = Session("Extreme Spin", 30, False)

        #book Sara Cox on the Muy Thai session
        self.booking1 = Booking(self.member2.id, self.session1.id)
        #book John Smith on the Extreme Spin session
        self.booking2 = Booking(self.member1.id, self.session2.id)
        #book David Keen on the Muy Thai session
        self.booking3 = Booking(self.member3.id, self.session1.id)
        #book Sara Cox on the Extreme Spin session
        self.booking4 = Booking(self.member2.id, self.session1.id)





#Starter code for reminders
# import pdb
# from models.location import Location
# from models.user import User
# from models.visit import Visit

# import repositories.location_repository as location_repository
# import repositories.user_repository as user_repository
# import repositories.visit_repository as visit_repository

# visit_repository.delete_all()
# location_repository.delete_all()
# user_repository.delete_all()

# user1 = User('Samwise Gamgee')
# user_repository.save(user1)

# user2 = User('Frodo Baggins')
# user_repository.save(user2)

# user3 = User('Gollum')
# user_repository.save(user3)

# location1 = Location('Mordor', 'Attractions')
# location_repository.save(location1)

# location2 = Location('The Prancing Pony', 'Tavern')
# location_repository.save(location2)

# visit1 = Visit(user1, location1, '0 stars, far too hot')
# visit_repository.save(visit1)

# visit2 = Visit(user3, location1, '5 stars, would visit again if I could')
# visit_repository.save(visit2)

# visit3 = Visit(user1, location2, '4 stars, plenty of beer available')
# visit_repository.save(visit3)

