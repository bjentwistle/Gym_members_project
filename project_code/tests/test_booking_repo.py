import unittest
from models.member import *
from models.session import *
from models.booking import *

import repositories.booking_repo as booking_repo
import repositories.session_repo as session_repo
import repositories.member_repo as member_repo

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("John", "Smith", "EH3", False)
        self.member2 = Member("Sara", "Cox", "EH4", True)
        self.member3 = Member("David", "Keen", "EH1", True)

        self.session1 = Session("Muy Thai", 90, True, "Sunday", "5PM")
        self.session2 = Session("Extreme Spin", 30, False, "Monday", "9AM")


    #Need to save data to tables first and check return to compare in a test
    #session_repo and members_repo save functions have been tested already.
    #@unittest.skip("comment out this line to run the test")
    def test_save_booking(self):
        booking_repo.delete_all_bookings()       
        member_repo.delete_all()
        session_repo.delete_all()
        member = member_repo.save(self.member2)
        session = session_repo.save(self.session1)
        booking = booking_repo.save(member, session)
        booking_id = int(booking.id)
        booking_selected = booking_repo.select(booking_id)
        self.assertEqual(member.id, booking_selected.member.id)
        #self.assertEqual(session.id, booking[0].id)
        booking_repo.delete_all_bookings()
        member_repo.delete_all()
        session_repo.delete_all()

    #@unittest.skip("comment out this line to run the test")
    def test_select_all_bookings(self):
        booking_repo.delete_all_bookings()
        member_repo.delete_all()
        session_repo.delete_all()
        member1 = member_repo.save(self.member1)
        member2 = member_repo.save(self.member2)
        session1 = session_repo.save(self.session1)
        booking_repo.save(member2, session1)
        booking_repo.save(member1, session1)
        results = booking_repo.select_all()
        self.assertEqual(2, len(results))
        self.assertEqual(member2.id, results[0].member.id)
        self.assertEqual(member1.id, results[1].member.id)
        booking_repo.delete_all_bookings()
        member_repo.delete_all()
        session_repo.delete_all()

