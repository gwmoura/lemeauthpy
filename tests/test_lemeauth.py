import unittest
import os
from lemeauth import LemeAuth

class TestLemeAuth(unittest.TestCase):
    """ Test for LemeAuth class """

    def get_credentials(self):
        """ get credendials from env vars """
        return (os.getenv('USER'), os.getenv('PASS'))


    def test_login(self):
        """ Test if login pass when send a valid password """
        user, password = self.get_credentials()
        auth = LemeAuth(user, password)
        self.assertTrue(auth.login())


    def test_failed_login(self):
        """ Test if login falied when send a invalid password """
        user, password = self.get_credentials()
        auth = LemeAuth(user, 'banana')
        self.assertFalse(auth.login())
