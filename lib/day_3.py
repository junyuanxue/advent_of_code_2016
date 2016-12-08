class TriangleFinder(object):
    def count(self, side_lengths):
        sets = self._split_lines(side_lengths)
        tally = 0
        for set in sets:
            sides = list(map(int, self._get_sides(set)))
            if self._is_triangle(sides):
                tally += 1
        return tally

    def count_by_column(self, side_lengths):
        lines = self._split_lines(side_lengths)
        horizonal_list = list(map(self._get_sides, lines))
        vertial_list = list(map(list, zip(*horizonal_list)))
        sets = []
        for long_list in vertial_list:
            short_lists = list(self._slice(long_list, 3))
            for short_list in short_lists:
                sets.append(short_list)
        print(sets)


    def _split_lines(self, side_lengths):
        return side_lengths.split('\n')

    def _get_sides(self, set):
        return set.strip().split()

    def _is_triangle(self, sides):
        if len(sides) == 3:
            x = sides[0]
            y = sides[1]
            z = sides[2]
            return x + y > z and y + z > x and x + z > y

    def _slice(self, long_list, n):
        for i in range(0, len(long_list), n):
            yield long_list[i:i + n]
