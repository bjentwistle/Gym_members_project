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

        self.session1 = Session("Muy Thai", 90, True)
        self.session2 = Session("Extreme Spin", 30, False)

        # #book Sara Cox on the Muy Thai session
        # self.booking1 = Booking(self.member2.id, self.session1.id)
        # #book John Smith on the Extreme Spin session
        # self.booking2 = Booking(self.member1.id, self.session2.id)
        # #book David Keen on the Muy Thai session
        # self.booking3 = Booking(self.member3.id, self.session1.id)
        # #book Sara Cox on the Extreme Spin session
        # self.booking4 = Booking(self.member2.id, self.session1.id)


    #Need to save data to tables first and check return to compare in a test
    #session_repo and members_repo save functions have been tested already.
    @unittest.skip("comment out this line to run the test")
    def test_save_booking(self):
        booking_repo.delete_all()        
        member_repo.delete_all()
        session_repo.delete_all()

        member = member_repo.save(self.member2)
        session = session_repo.save(self.session1)

        booking_id = booking_repo.save(member, session)
        booking = booking_repo.select(booking_id)

        self.assertEqual(member.id, booking.member_id)
        self.assertEqual(session.id, booking.session_id)
        booking_repo.delete_all()
        member_repo.delete_all()
        session_repo.delete_all()

    #@unittest.skip("comment out this line to run the test")
    def test_select_all_bookings(self):
        booking_repo.delete_all()
        member_repo.delete_all()
        session_repo.delete_all()

        member1 = member_repo.save(self.member1)
        member2 = member_repo.save(self.member2)
        session1 = session_repo.save(self.session1)

        booking_repo.save(member2, session1)
        booking_repo.save(member1, session1)

        results = booking_repo.select_all()
        self.assertEqual(2, len(results))
        self.assertEqual(member2.id, results[0].member_id)
        self.assertEqual(member1.id, results[1].member_id)
        booking_repo.delete_all()
        member_repo.delete_all()
        session_repo.delete_all()

