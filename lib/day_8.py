class Authy(object):
    def __init__(self):
        self.SCREEN_WIDTH = 50
        self.SCREEN_HEIGHT = 6
        self.screen = ['-' * self.SCREEN_WIDTH] * self.SCREEN_HEIGHT

    def count_lit_pixels(self, sequence):
        steps = sequence.strip().split('\n')
        for step in steps:
            if 'rect' in step:
                width = int(step.split('x')[0].split(' ').pop())
                height = int(step.split('x')[1])
                self._turn_on_rectangle(width, height)
            if 'rotate' in step:
                coordinate = step.split('=')[0][-1]
                position = int(step.split('=')[1].split(' by')[0])
                distance = int(step.split(' ').pop())
                self._rotate(coordinate, position, distance)
        print(self.screen)
        return ''.join(self.screen).count('#')

    def _turn_on_rectangle(self, width, height):
        for i, row in enumerate(self.screen):
            if i < height:
                j = 0
                while j < width:
                    self._switch('#', i, j)
                    j += 1

    def _switch(self, mode, row_index, column_index):
        row = list(self.screen[row_index])
        row[column_index] = mode
        self.screen[row_index] = ''.join(row)

    def _rotate(self, coordinate, position, distance):
        frozen_screen = self._freeze_screen()
        if coordinate == 'x':
            for i, row in enumerate(frozen_screen):
                value = row[position]
                new_index = self._get_new_index(i, distance, self.SCREEN_HEIGHT)
                self._switch(value, new_index, position)
        else:
            row = frozen_screen[position]
            for i, spot in enumerate(list(row)):
                new_index = self._get_new_index(i, distance, self.SCREEN_WIDTH)
                self._switch(spot, position, new_index)

    def _get_new_index(self, i, distance, limit):
        new_index = i + distance
        while new_index >= limit:
            new_index -= limit
        return new_index

    def _freeze_screen(self):
        frozen_screen = []
        for row in self.screen:
            frozen_screen.append(row)
        return frozen_screen
