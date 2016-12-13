import unittest
from lib.day_7 import IPChecker

class IPCheckerTestCase(unittest.TestCase):
    def setUp(self):
        self.ip_checker = IPChecker()
        self.ips = 'abba[mnop]qrst\nabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn'
        self.more_ips = 'aba[bab]xyz\nxyx[xyx]xyx\naaa[kek]eke\nzazbz[bzb]cdb'
        with open('tests/input/input_day_7.txt', 'r') as input_file:
            self.puzzle_ips = input_file.read()

    def test_counts_ips_that_support_tls(self):
        number = self.ip_checker.count(self.ips, 'tls')
        self.assertEqual(number, 2)

        puzzle_tally = self.ip_checker.count(self.puzzle_ips, 'tls')
        self.assertEqual(puzzle_tally, 110)

    def test_counts_ips_that_support_ssl(self):
        number = self.ip_checker.count(self.more_ips, 'ssl')
        self.assertEqual(number, 3)

        puzzle_tally = self.ip_checker.count(self.puzzle_ips, 'ssl')
