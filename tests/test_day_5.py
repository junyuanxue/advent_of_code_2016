import unittest
from lib.day_5 import PasswordFinder

class PasswordFinderTestCase(unittest.TestCase):
    def setUp(self):
        self.password_finder = PasswordFinder()

    def test_finds_password(self):
        password = self.password_finder.run('abc')
        self.assertEqual(password, '18f47a30')

        # door_id = 'cxdnnyjw'
        # puzzle_password = self.password_finder.run(door_id)
