class Authy(object):
    def __init__(self):
        SCREEN_WIDTH = 50
        SCREEN_HEIGHT = 6

    def count_lit_pixels(self, sequence):
        steps = sequence.strip().split('\n')
        for step in steps:
            if 'rect' in step:
                width = int(step.split('x')[0][:-1])
                height = int(step.split('x')[1])
            if 'rotate' in step:
                distance = int(step.split(' ').pop())
                coordinate = step.split('=')[0][-1]
                position = step.split('=')[1][0]
        return '1'
