
class Fastread(object):

    def __init__(self,
                 filename: str = None):
        self.filename = filename

    def _load(self,
              sep: str = None):
        if not self.filename:
            raise Exception('You need filename')
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if sep:
                        line = line.split(str(sep))
                    yield line
        except FileNotFoundError:
            raise FileNotFoundError('File not Found')

    def lines(self,
              sep: str = None):
        return self._load(sep)

    def find(self,
             word: str = None):
        if not word:
            raise Exception('Type word')

        for line in self._load():
            if word in line:
                yield line

    def row(self,
            number: int = None):
        if not number:
            raise Exception('Type number')

        lines = self.lines()
        try:
            row = list(lines)[number]
            return row
        except Exception as e:
            raise Exception(e)
