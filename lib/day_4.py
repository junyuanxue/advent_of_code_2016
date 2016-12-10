import re
import operator

class RoomDecoder(object):
    def __init__(self):
        self.sum_of_sector_ids = 0

    def sum_sector_ids(self, data):
        rooms = data.split('\n')
        for room in rooms:
            checksum = room.split('[')[1][:-1]
            first_part = room.split('[')[0]
            sector_id = first_part.split('-').pop()
            letters = re.sub('[^a-zA-Z]', '', first_part)
            print(checksum)
            print(sector_id)
            print(letters)
            most_common_letters = self._get_most_common_letters(letters, 5)

    def _get_most_common_letters(self, letters, number):
        letters = list(letters)
        frequencies = {}
        for letter in letters:
            frequency = 1
            if letter in frequencies:
                frequency = frequencies[letter] + 1
            frequencies[letter] = frequency
        print(frequencies)
