import unittest
from lib.day_4 import RoomDecoder

class RoomDecoderTestCase(unittest.TestCase):
    def setUp(self):
        self.room_decoder = RoomDecoder()
        with open('tests/input/input_day_4.txt', 'r') as input_file:
            self.puzzle_data = input_file.read()

    def test_sums_sector_ids_of_real_rooms(self):
        decoy_data = 'aaaaa-bbb-z-y-x-123[abxyz]\na-b-c-d-e-f-g-h-987[abcde]\nnot-a-real-room-404[oarel]\ntotally-real-room-200[decoy]'
        self.room_decoder.run(decoy_data)
        self.assertEqual(self.room_decoder.sum_of_sector_ids, 1514)

    def test_sums_sector_ids_of_real_rooms_after_crazy_input(self):
        self.room_decoder.run(self.puzzle_data)
        self.assertEqual(self.room_decoder.sum_of_sector_ids, 409147)

    def test_decrypts_room_names(self):
        name = self.room_decoder.decrypt_name('qzmt-zixmtkozy-ivhz', 343)
        self.assertEqual(name, 'very encrypted name')

    def test_finds_north_pole_storage_from_crazy_input(self):
        self.room_decoder.run(self.puzzle_data)
        correct_room = 'kloqemlib-lygbzq-pqloxdb-991[lbqod]'
        self.assertEqual(self.room_decoder.north_pole_storage, correct_room)
