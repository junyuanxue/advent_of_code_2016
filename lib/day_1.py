class BlockCalculator(object):

    def run(self, input):
        instructions = input.split(', ')
        x = 0
        y = 0
        for index, instruction in enumerate(instructions):
            direction = instruction[0]
            distance = int(instruction[1])
            if direction == 'R':
                x += distance
            else:
                x -= distance
        return input
