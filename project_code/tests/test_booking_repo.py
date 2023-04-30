import unittest
from models.member import *
from models.session import *
from models.booking import *

import repositories.booking_repo as booking_repo
#import repositories.member_repo as member_repo
#import repositories.session_repo as session_repo


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
