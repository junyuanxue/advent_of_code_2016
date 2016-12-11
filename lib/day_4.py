from collections import Counter

class RoomDecoder(object):
    def __init__(self):
        self.sum_of_sector_ids = 0
        self.north_pole_storage = ''

    def run(self, data):
        rooms = data.strip().split('\n')
        for room in rooms:
            first_part = room.split('[')[0]

            checksum = room.split('[')[1][:-1]
            sector_id = int(first_part.split('-').pop())
            encrypted_name = first_part[:-4]
            letters = encrypted_name.replace('-', '')

            occurrences = dict(Counter(list(letters)))
            largest_values = sorted(occurrences.values(), reverse=True)[:5]
            if self._is_real_room(checksum, occurrences, largest_values) == True:
                self.sum_of_sector_ids += sector_id
                decrypted_name = self.decrypt_name(encrypted_name, sector_id)
                self._find_north_pole_room(decrypted_name, room)

    def decrypt_name(self, encrypted_name, sector_id):
        output = ''
        for letter in encrypted_name:
            output += ' ' if letter == '-' else self._decode(letter, sector_id)
        return output

    def _find_north_pole_room(self, name, room):
        if 'northpole object' in name:
            self.north_pole_storage = room

    def _decode(self, letter, number):
        ordinal = ord(letter)
        new_ordinal = ordinal + number
        while new_ordinal > ord('z'):
            new_ordinal -= 26
        return chr(new_ordinal)

    def _is_real_room(self, checksum, occurrences, largest_values):
        checksum_list = list(checksum)
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
