import unittest
from lib.day_5 import PasswordFinder

class PasswordFinderTestCase(unittest.TestCase):
    def setUp(self):
        self.password_finder = PasswordFinder()
        self.door_id = 'cxdnnyjw'

    def test_finds_password_in_simple_mode(self):
        password = self.password_finder.run_simple_mode('abc')
        self.assertEqual(password, '18f47a30')

        puzzle_password = self.password_finder.run_simple_mode(self.door_id)
        self.assertEqual('f77a0e6e', puzzle_password)

    def test_finds_password_in_advanced_mode(self):
        password = self.password_finder.run_advanced_mode('abc')
        self.assertEqual(password, '05ace8e3')

        puzzle_password = self.password_finder.run_advanced_mode(self.door_id)
        self.assertEqual(puzzle_password, '999828ec')
