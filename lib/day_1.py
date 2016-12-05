class BlockCalculator(object):
    def __init__(self):
        self.totalBlocksAway = 0
        self.distance = 0

    def run(self, input):
        instructions = input.split(', ')
        x = 0
        y = 0
        facing = 0 # north: 0, east: 1: south: 2, west: 3
        coordinates = [[x, y]]
        for index, instruction in enumerate(instructions):
            direction = instruction[0]
            distance = int(instruction[1:])
            if direction == 'R':
                if facing == 0:
                    x += distance
                elif facing == 2:
                    x -= distance
                elif facing == 1:
                    y -= distance
                elif facing == 3:
                    y += distance
                facing = (facing + 1)%4
            else:
                if facing == 0:
                    x -= distance
                elif facing == 2:
                    x += distance
                elif facing == 1:
                    y += distance
                elif facing == 3:
                    y -= distance
                facing = (facing - 1)%4
        self.totalBlocksAway = abs(x) + abs(y)
