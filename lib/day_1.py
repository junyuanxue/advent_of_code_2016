class BlockCalculator(object):
    def __init__(self):
        self.totalBlocksAway = 0
        self.distance = 0

    def run(self, input):
        instructions = input.split(', ')
        x = 0
        y = 0
        facing = 0 # north: 0, east: 1: south: 2, west: 3
        step_action = {0: 1, 1: -1, 2: -1, 3: 1}
        direction_action = {'R': 1, 'L': -1}
        spots_tracker = [[x, y]]
        first_repeated_spot_found = False

        for instruction in instructions:
            direction_text = instruction[0]
            distance = int(instruction[1:])

            direction = direction_action[direction_text]
            step = step_action[facing]

            for i in range(distance):
                if facing % 2 == 0:
                    x += step * direction
                else:
                    y += step * direction

                current_spot = [x, y]
                if current_spot in spots_tracker and not first_repeated_spot_found:
                    self.distance = self._get_distance(x, y)
                    first_repeated_spot_found = True
                spots_tracker.append(current_spot)

            facing = (facing + (1 * direction)) % 4

        self.totalBlocksAway = self._get_distance(x, y)

    def _get_distance(self, x, y):
        return abs(x) + abs(y)
