import sys
from collections.abc import Iterable


class ChunkMeta(type):

    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if isinstance(value, Setter):
                value.field_name = name
        return super().__new__(cls, name, bases, attrs)


class Setter:

    def __get__(self, obj, _=None):
        return obj.__dict__[self.field_name]

    def __set__(self, obj, value):
        obj.__dict__[self.field_name] = value


class NotNegativeInteger(Setter):

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            super().__set__(obj, value)
        else:
            raise ValueError('%s is not NotNegativeInteger.' % value)


class Bytes(Setter):

    @staticmethod
    def _check(value):
        if not isinstance(value, Iterable):
            raise ValueError('%s is not iterable.' % value)
        if not all([isinstance(item, int) and item < 256 for item in value]):
            raise ValueError('%s is not valid byte array.' % value)

    def __set__(self, obj, value):
        self._check(value)
        super().__set__(obj, value)


class BaseChunkSetter(metaclass=ChunkMeta):

    shift = NotNegativeInteger()
    data = Bytes()

    def dump_data(self, pointer):
        for index, value in enumerate(self.data, self.shift):
            pointer[index] = value

    def __init__(self, *, shift, data):
        self.shift = shift
        self.data = data


class BaseChunkGetter:

    @property
    def length(self):
        return sys.getsizeof(self.entity)

    def __repr__(self):
        return "<Entity '%s' -> [%s, ...]>" % (
            self.entity, ', '.join(str(item) for item in self.pointer[:5])
        )

    def __iter__(self):
        return iter(self.pointer[:self.length])

    def __getitem__(self, item):
        return self.pointer.__getitem__(item)

    def __setitem__(self, item_name, item_value):
        self.pointer.__setitem__(item_name, item_value)

    def __init__(self, entity, pointer):
        self.entity = entity
        self.pointer = pointer
