class BoundaryError(Exception):
    def __init__(self, chunk):
        self.chunk = chunk
        self.value = str(self)

    def __str__(self):
        return 'Lookup out of chunk boundary in chunk %s.' % self.chunk


class AllocatorError(Exception):
    pass


class InsufficientMemory(AllocatorError):
    def __init__(self, length):
        self.length = length
        self.value = str(self)

    def __str__(self):
        return 'Insufficient memory for a block length of %s.' % self.chunk


class FreeRoutineBadBlock(AllocatorError):
    def __init__(self, address):
        self.address = address
        self.value = str(self)

    def __str__(self):
        return 'Block starts at %s is not heap block.' % self.address
