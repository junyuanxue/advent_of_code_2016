import unittest
from lib.day_5 import PasswordFinder

class PasswordFinderTestCase(unittest.TestCase):
    def setUp(self):
        self.password_finder = PasswordFinder()

    def test_finds_password(self):
        password = password_finder.run('abc')
        self.assertEqual(password, '18f47a30')

        puzzle_door_id = 'cxdnnyjw'
        puzzle_password = password_finder.run(puzzle_door_id)
