import ctypes
from .allocators import malloc, free
from .exceptions import BoundaryError


class ChunkMeta(type):

    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if isinstance(value, Attribute):
                value.field_name = name
        return super().__new__(cls, name, bases, attrs)


class Attribute:

    def __init__(self):
        self._inited = False

    def __get__(self, obj, _=None):
        return obj.__dict__[self.field_name]

    def __set__(self, obj, value):
        obj.__dict__[self.field_name] = value
        self._inited = True


class AttributeFrontend(Attribute):

    def __set__(self, obj, value):
        if obj.__dict__.get(self.field_name) is None:
            super().__set__(obj, value)


class _NotNegativeInteger(Attribute):

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            super().__set__(obj, value)
        else:
            raise ValueError('%s is not NotNegativeInteger.' % value)


class NotNegativeInteger(AttributeFrontend, _NotNegativeInteger):
    pass


class BaseMemoryChunk(metaclass=ChunkMeta):

    address = NotNegativeInteger()
    length = NotNegativeInteger()

    def copy_from_chunk(self, chunk):
        for index, value in enumerate(chunk):
            self[index] = value

    def clone(self, allocator=malloc):
        chunk = allocator(self.length, self.__class__)
        for index, value in enumerate(self):
            chunk[index] = value
        return chunk

    def __eq__(self, other):
        return type(self) == type(other) and all([
            self.length == other.length,
            self._pointer[:self.length] == other._pointer[:other.length]
        ])

    def __repr__(self):
        return "<Chunk addr=%s and data=[%s, ...]>" % (
            self.address, ', '.join(str(item) for item in self._pointer[:5])
        )

    def __getitem__(self, item):
        if isinstance(item, int):
            if item < 0 or item >= self.length:
                raise BoundaryError(self)
        elif isinstance(item, slice):
            # implement for slices
            pass
        else:
            raise TypeError()

        return self._pointer.__getitem__(item)

    def __setitem__(self, item, value):
        if item < 0 or item >= self.length:
            raise BoundaryError(self)

        return self._pointer.__setitem__(item, value)

    def __iter__(self):
        return iter(self._pointer[:self.length])

    def __init__(self, address, length, c_type=ctypes.c_ubyte):
        self.address = address
        self.length = length
        self._pointer = ctypes.cast(address, ctypes.POINTER(c_type))
