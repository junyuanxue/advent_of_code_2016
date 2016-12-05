class BlockCalculator(object):

    def run(self, input):
        instructions = input.split(', ')
        x = 0
        y = 0
        facing = 'N' # north: 0, east: 1: south: 2, west: 3
        for index, instruction in enumerate(instructions):
            direction = instruction[0]
            distance = int(instruction[1])
            if direction == 'R':
                if facing == 'N':
                    x += distance
                    facing = 'E'
                elif facing == 'S':
                    x -= distance
                    facing = 'W'
                elif facing == 'E':
                    y -= distance
                    facing = 'S'
                elif facing == 'W':
                    y += distance
                    facing = 'N'
            else:
                if facing == 'N':
                    x -= distance
                    facing = 'W'
                elif facing == 'S':
                    x += distance
                    facing = 'E'
                elif facing == 'E':
                    y += distance
                    facing = 'N'
                elif facing == 'W':
                    y -= distance
                    facing = 'S'
        print(x)
        print(y)
        return abs(x) + abs(y)
