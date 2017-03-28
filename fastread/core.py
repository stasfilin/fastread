
class Fastread(object):

    def __init__(self,
                 filename: str = None):
        self.filename = filename


    def _load(self):
        if not self.filename:
            raise Exception('You need filename')
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    yield line
        except FileNotFoundError:
            raise FileNotFoundError('File not Found')

    def lines(self):
        return self._load()

    def find(self,
             word: str = None):
        if not word:
            raise Exception('Type word')

        for line in self._load():
            if word in line:
                yield line

