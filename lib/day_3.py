class TriangleFinder(object):
    def __init__(self):
        self.tally = 0

    def count(self, side_lengths):
        sets = side_lengths.split('\n')
        for set in sets:
            sides = list(map(int, set.strip().split()))
            if len(sides) == 3 and sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[1] > sides[2]:
               self.tally += 1
