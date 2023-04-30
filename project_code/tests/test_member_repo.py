import unittest
from models.member import *
from models.session import *
from models.booking import *

import repositories.member_repo as member_repo


class TestGym_emulator(unittest.TestCase):

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


    #Need to save data to tables first and check return to compare in a test
    @unittest.skip("comment out this line to run the test")
    def test_save(self):
        member = member_repo.save(self.member1)
        self.assertEqual("John", member.first_name)
        self.assertEqual("Smith", member.last_name)
        self.assertEqual("EH3", member.postcode)
        self.assertEqual(False, member.premium_member)
            

    #Need to be able to select a member by id and return it
    @unittest.skip("comment out this line to run the test")
    def test_select(self):
        member = member_repo.save(self.member1)
        test_id = member.id
        test_member = member_repo.select(test_id)
        self.assertEqual("Smith", test_member.last_name)

    @unittest.skip("comment out this line to run the test")
    def test_select_all(self):
        member_repo.save(self.member1)
        member_repo.save(self.member2)
        member_repo.save(self.member3)
        list_of_members = member_repo.select_all()
        self.assertEqual(3, len(list_of_members))

    #Need to test the delete_all func - first populate using save that we know works, then delete all and then select_all that we know works and compare the empty list returnedto zero.
    @unittest.skip("comment out this line to run the test")
    def test_delete_all(self):
        member_repo.save(self.member1)
        member_repo.save(self.member2)
        member_repo.save(self.member3)
        member_repo.delete_all()
        list_of_members = member_repo.select_all()
        self.assertEqual(0, len(list_of_members))




#@unittest.skip("delete this line to run the test")
# def test_pet_shop_name(self):
#     name = get_pet_shop_name(self.cc_pet_shop)
#     self.assertEqual("Camelot of Pets", name)

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

