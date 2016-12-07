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
                if step == 'U' and y < 1:
                    y += 1
                elif step == 'D' and y > -1:
                    y -= 1
                elif step == 'R' and x < 1:
                    x += 1
                elif step == 'L' and x > -1:
                    x -= 1
            number = self._get_number([x, y], coordinates_map)
            code += str(number)
        return code

    def unlock_funky_keypad(self, instructions):
        x = -2
        y = 0 # 5 -> (-2, 0), central point 7 (0, 0), absolute value can't go over 2
        code = ''
        coordinates_map = {
            1: [0, 2],
            2: [-1, 1],
            3: [0, 1],
            4: [1, 1],
            5: [-2, 0],
            6: [-1, 0],
            7: [0, 0],
            8: [1, 0],
            9: [2, 0],
            'A': [-1, -1],
            'B': [0, -1],
            'C': [1, -1],
            'D': [0, -2]
        }
        for line in instructions:
            steps = list(line)
            for step in steps:
                if step == 'U' and y < x + 2 and y < 2 - x:
                    y += 1
                elif step == 'D' and y > x - 2 and y > x * -1 - 2:
                    y -= 1
                elif step == 'R' and x < 2 - y and x < y + 2:
                    x += 1
                elif step == 'L' and x > y - 2 and x > -2 - y:
                    x -= 1
            number = self._get_number([x, y], coordinates_map)
            code += str(number)
        return code

    def _get_number(self, dot, coordinates_map):
        for number, coordinates in coordinates_map.items():
            if coordinates == dot: return number
