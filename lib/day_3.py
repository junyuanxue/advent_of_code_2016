class TriangleFinder(object):
    def count(self, side_lengths):
        sets = side_lengths.split('\n')
        tally = 0
        for set in sets:
            sides = list(map(int, set.strip().split()))
            if len(sides) == 3:
                x = sides[0]
                y = sides[1]
                z = sides[2]
                if x + y > z and y + z > x and x + z > y:
                    tally += 1
        return tally
