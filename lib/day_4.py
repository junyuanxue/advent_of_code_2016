import re

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
            frequencies = self._map_letter_frequencies(list(letters))
            largest_values = sorted(frequencies.values(), reverse=True)[:5]
            if self._is_real_room(checksum, frequencies, largest_values):
                self.sum_of_sector_ids += int(sector_id)

    def _map_letter_frequencies(self, letters_list):
        frequencies = {}
        for letter in letters_list:
            frequency = frequencies[letter] + 1 if letter in frequencies else 1
            frequencies[letter] = frequency
        return frequencies

    def _is_real_room(self, checksum, frequencies, largest_values):
        for letter in checksum:
            if letter not in frequencies or frequencies[letter] not in largest_values:
                return False
        return True
