class BoundaryError(Exception):
    def __init__(self, chunk):
        self.chunk = chunk
        self.value = str(self)

    def __str__(self):
        return 'Lookup out of chunk boundary in chunk %s.' % self.chunk
