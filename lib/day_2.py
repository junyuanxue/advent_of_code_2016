class Decoder(object):
    def run(self, instructions):
        x = 0
        y = 0 # 5 -> (0, 0) absolute values of x and y can't be bigger than 1
        code = ''
        coordinates_map = {
            1: [-1, 1],
            2: [1, 0],
            3: [1, 1],
            4: [-1, 0],
            5: [0, 0],
            6: [1, 0],
            7: [-1, -1],
            8: [0, -1],
            9: [1, -1]
        }
        for line in instructions:
            steps = list(line)
            for step in steps:
                print(step)
                if step == 'U':
                    if y < 1: y += 1
                elif step == 'D':
                    if y > -1: y -= 1
                elif step == 'R':
                    if x < 1: x += 1
                elif step == 'L':
                    if x > -1: x -= 1
            number = self._get_number([x, y], coordinates_map)
            code += str(number)
        return code

    def _get_number(self, dot, coordinates_map):
        for number, coordinates in coordinates_map.items():
            if coordinates == dot: return number
