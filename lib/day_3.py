class TriangleFinder(object):
    def count(self, side_lengths):
        sets = side_lengths.split('\n')
        tally = 0
        for set in sets:
            sides = list(map(int, set.strip().split()))
            if self._is_triangle(sides):
                tally += 1
        return tally

    def _is_triangle(self, sides):
        if len(sides) == 3:
            x = sides[0]
            y = sides[1]
            z = sides[2]
            return x + y > z and y + z > x and x + z > y
