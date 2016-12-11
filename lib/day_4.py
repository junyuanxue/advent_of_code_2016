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

            occurrences = dict(Counter(list(letters)))
            largest_values = sorted(occurrences.values(), reverse=True)[:5]
            # largest_values = self._get_largest_values(sorted_occurrences, 5)
            if self._is_real_room(checksum, occurrences, largest_values) == True:
                self.sum_of_sector_ids += int(sector_id)

    # def _get_largest_values(self, numbers, length):
    #     values = []
    #     for number in numbers:
    #         if number not in values and len(values) <= 5:
    #             values.append(number)
    #     return values

    def _is_real_room(self, checksum, occurrences, largest_values):
        checksum_list = list(checksum)
        print(occurrences)
        print(checksum)
        for index, letter in enumerate(checksum_list):
            if letter not in occurrences or occurrences[letter] not in largest_values:
                return False
            elif occurrences[letter] in largest_values and index < 4:
                next_letter = checksum_list[index + 1]
                if next_letter not in occurrences:
                    return False
                elif occurrences[letter] < occurrences[next_letter]:
                    return False
                elif occurrences[letter] == occurrences[next_letter] and letter > next_letter:
                    return False
        return True
