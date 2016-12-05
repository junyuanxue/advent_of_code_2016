class BlockCalculator(object):
    def __init__(self):
        self.totalBlocksAway = 0
        self.distance = 0

    def run(self, input):
        instructions = input.split(', ')
        x = 0
        y = 0
        facing = 0 # north: 0, east: 1: south: 2, west: 3
        spots_tracker = []
        first_repeated_spot_found = False
        for instruction in instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            if direction == 'R':
                for i in range(distance):
                    if facing == 0:
                        x += 1
                    elif facing == 2:
                        x -= 1
                    elif facing == 1:
                        y -= 1
                    elif facing == 3:
                        y += 1
                    current_spot = [x, y]
                    if current_spot in spots_tracker and not first_repeated_spot_found:
                        self.distance = self._get_distance(x, y)
                    spots_tracker.append(current_spot)
                facing = (facing + 1)%4
            else:
                for i in range(distance):
                    if facing == 0:
                        x -= 1
                    elif facing == 2:
                        x += 1
                    elif facing == 1:
                        y += 1
                    elif facing == 3:
                        y -= 1
                    current_spot = [x, y]
                    if current_spot in spots_tracker and not first_repeated_spot_found:
                        self.distance = self._get_distance(x, y)
                    spots_tracker.append(current_spot)
                facing = (facing - 1)%4

        self.totalBlocksAway = self._get_distance(x, y)

    def _get_distance(self, x, y):
        return abs(x) + abs(y)
