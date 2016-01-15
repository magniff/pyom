import ctypes
from .exceptions import BoundaryError


class BaseMemoryChunk:

    def __repr__(self):
        return "<Chunk addr=%s and data=[%s, ...]>" % (
            self.address, ', '.join(str(item) for item in self._pointer[:5])
        )

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < 0 or item >= self.length:
                raise BoundaryError(self)
        return self._pointer.__getitem__(item)

    def __setitem__(self, item, value):
        if not isinstance(item, int):
            raise IndexError('Only int objects supported for indexing here.')
        if item < 0 or item >= self.length:
            raise BoundaryError(self)

        return self._pointer.__setitem__(item, value)

    def __iter__(self):
        return iter(self._pointer[:self.length])

    def __init__(self, address, length, c_type=ctypes.c_ubyte):
        self.address = address
        self.length = length
        self._pointer = ctypes.cast(address, ctypes.POINTER(c_type))
