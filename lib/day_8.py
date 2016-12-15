class Authy(object):
    def __init__(self):
        self.SCREEN_WIDTH = 50
        self.SCREEN_HEIGHT = 6

    def count_lit_pixels(self, sequence):
        steps = sequence.strip().split('\n')
        screen = ['-' * self.SCREEN_WIDTH] * self.SCREEN_HEIGHT
        print(screen)
        for step in steps:
            if 'rect' in step:
                width = int(step.split('x')[0][:-1])
                height = int(step.split('x')[1])
            if 'rotate' in step:
                distance = int(step.split(' ').pop())
                coordinate = step.split('=')[0][-1]
                position = step.split('=')[1][0]
        return '1'
