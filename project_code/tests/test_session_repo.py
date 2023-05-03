import unittest
from models.member import *
from models.session import *
from models.booking import *

import repositories.session_repo as session_repo

class TestSession(unittest.TestCase):

    def setUp(self):
        self.member1 = Member("John", "Smith", "EH3", False)
        self.member2 = Member("Sara", "Cox", "EH4", True)
        self.member3 = Member("David", "Keen", "EH1", True)

        self.session1 = Session("Muy Thai", 90, True)
        self.session2 = Session("Extreme Spin", 30, False)

    #Need to save data to tables first and check return to compare in a test
    @unittest.skip("comment out this line to run the test")
    def test_save_session(self):
        session_repo.delete_all()
        session = session_repo.save(self.session1)
        self.assertEqual("Muy Thai", session.name)
        self.assertEqual(90, session.duration)
        self.assertEqual(True, session.premium_session)
        session_repo.delete_all()

    #Need to be able to select a member by id and return it
    @unittest.skip("comment out this line to run the test")
    def test_select_session(self):
        session_repo.delete_all()
        session = session_repo.save(self.session1)
        test_id = session.id
        test_session = session_repo.select(test_id)
        self.assertEqual("Muy Thai", test_session.name)
        self.assertEqual(90, test_session.duration)
        self.assertEqual(True, session.premium_session)
        session_repo.delete_all()

    @unittest.skip("comment out this line to run the test")
    def test_select_all_sessions(self):
        session_repo.delete_all()
        session_repo.save(self.session1)
        session_repo.save(self.session2)
        list_of_sessions = session_repo.select_all()
        self.assertEqual(2, len(list_of_sessions))
        session_repo.delete_all()

    #Need to test the delete_all func - first populate using save that we know works, then delete all and then select_all that we know works and compare the empty list returnedto zero.
    @unittest.skip("comment out this line to run the test")
    def test_delete_all_sessions(self):
        session_repo.save(self.session1)
        session_repo.save(self.session2)
        session_repo.delete_all()
        list_of_sessions = session_repo.select_all()
        self.assertEqual(0, len(list_of_sessions))
    