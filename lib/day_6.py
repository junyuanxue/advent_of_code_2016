class Messenger(object):
    def read(self, signal):
        lines = signal.strip().split('\n')
        columns = self._get_columns(lines)
        return 'hello'

    def _get_columns(self, lines):
        columns = [[], [], [], [], [], []]
        for line in lines:
            
