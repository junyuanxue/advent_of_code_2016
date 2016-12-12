from collections import Counter

class Messenger(object):
    def read(self, signal):
        lines = signal.strip().split('\n')
        columns = self._get_columns(lines)
        message = ''
        for column in columns:
            occurrences = dict(Counter(column))
            # letter = sorted(occurrences, key=occurrences.get, reverse=True)[0]
            letter = sorted(occurrences, key=occurrences.get, reverse=True)[-1]
            message += letter
        return message

    def _get_columns(self, lines):
        length = len(lines[0])
        columns = [[] for _ in range(length)]
        for line in lines:
            index = 0
            while index < len(line):
                columns[index].append(line[index])
                index += 1
        return columns
