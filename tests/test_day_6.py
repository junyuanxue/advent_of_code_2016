import unittest
from lib.day_6 import Messenger

class MessengerTestCase(unittest.TestCase):
    def setUp(self):
        self.messenger = Messenger()
        self.signal = 'eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\nnssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar'
        with open('tests/input/input_day_6.txt', 'r') as input_file:
            self.puzzle_signal = input_file.read()

    def test_reads_message_from_most_frequent_letters(self):
        message = self.messenger.read(self.signal, 'most')
        self.assertEqual(message, 'easter')

        puzzle_message = self.messenger.read(self.puzzle_signal, 'most')
        self.assertEqual(puzzle_message, 'ikerpcty')

    def test_reads_message_from_least_common_letters(self):
        message = self.messenger.read(self.signal, 'least')
        self.assertEqual(message, 'advent')

        puzzle_message = self.messenger.read(self.puzzle_signal, 'least')
        self.assertEqual(puzzle_message, 'uwpfaqrq')
