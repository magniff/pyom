from collections.abc import Iterable


class ChunkMeta(type):

    def __new__(cls, name, bases, attrs):
        for name, value in attrs.items():
            if isinstance(value, Setter):
                value.field_name = name
        return super().__new__(cls, name, bases, attrs)


class Setter:

    def __get__(self, obj, klass=None):
        pass

    def __set__(self, obj, value):
        obj.__dict__[self.field_name] = value


class NotNegativeInteger(Setter):

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            super().__set__(obj, value)
        else:
            raise ValueError('%s is not NotNegativeInteger.' % value)


class Bytes(Setter):

    def _check(self, value):
        if not isinstance(value, Iterable):
            raise ValueError('%s is not iterable.' % value)
        if not all([isinstance(item, int) and item < 256 for item in value]):
            raise ValueError('%s is not valid byte array.' % value)

    def __set__(self, obj, value):
        self._check(value)
        super().__set__(obj, value)


class ChunkSetter(metaclass=ChunkMeta):

    shift = NotNegativeInteger()
    data = Bytes()

    def __init__(self, shift, data):
        self.shift = shift
        self.data = data
