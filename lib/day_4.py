import re
from collections import Counter

class RoomDecoder(object):
    def __init__(self):
        self.sum_of_sector_ids = 0

    def sum_sector_ids(self, data):
        rooms = data.strip().split('\n')
        for room in rooms:
            checksum = room.split('[')[1][:-1]
            first_part = room.split('[')[0]
            sector_id = first_part.split('-').pop()
            letters = re.sub('[^a-zA-Z]', '', first_part)

            frequencies = dict(Counter(list(letters)))
            largest_values = sorted(frequencies.values(), reverse=True)[:5]
            print(frequencies)
            print(largest_values)
            # largest_values = self._get_largest_values(sorted_frequencies, 5)
            if self._is_real_room(checksum, frequencies, largest_values):
                self.sum_of_sector_ids += int(sector_id)

    # def _get_largest_values(self, numbers, length):
    #     values = []
    #     for number in numbers:
    #         if number not in values and len(values) <= 5:
    #             values.append(number)
    #     return values

    def _is_real_room(self, checksum, frequencies, largest_values):
        for letter in checksum:
            if letter not in frequencies or frequencies[letter] not in largest_values:
                return False
        return True
