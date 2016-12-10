import unittest
from lib.day_4 import RoomDecoder

class RoomDecoderTestCase(unittest.TestCase):
    def setUp(self):
        self.room_decoder = RoomDecoder()
        with open('tests/input/input_day_4.txt', 'r') as input_file:
            self.puzzle_data = input_file.read()

    def test_sums_sector_ids_of_real_rooms(self):
        decoy_data = 'aaaaa-bbb-z-y-x-123[abxyz]\na-b-c-d-e-f-g-h-987[abcde]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]'
        sum_1 = self.room_decoder.sum_sector_ids(decoy_data)
        self.assertEqual(sum_1, 1514)
