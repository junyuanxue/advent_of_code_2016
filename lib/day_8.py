class Authy(object):
    def __init__(self):
        self.SCREEN_WIDTH = 50
        self.SCREEN_HEIGHT = 6
        self.screen = ['-' * self.SCREEN_WIDTH] * self.SCREEN_HEIGHT

    def count_lit_pixels(self, sequence):
        steps = sequence.strip().split('\n')
        print(self.screen)
        for step in steps:
            if 'rect' in step:
                width = int(step.split('x')[0][:-1])
                height = int(step.split('x')[1])
                self._turn_on_rectangle(width, height)
            if 'rotate' in step:
                distance = int(step.split(' ').pop())
                coordinate = step.split('=')[0][-1]
                position = step.split('=')[1][0]
        return '1'

    def _turn_on_rectangle(self, width, height):
        for index, row in enumerate(screen):
            if index < height:

    def _switch(self, mode, row, index):
        string = '-'
        replacement = '#'
        if mode == 'off':
            string = '#'
            replacement '-'
        return row[:index].replace(string, replacement) + row[index:]
