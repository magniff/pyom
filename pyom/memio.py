import sys
from .getsets import BaseMemoryChunk


class ObjectMemoryIO:
    """This is simple descriptor, which instance we are going to inject into
    object`s (common base class) dictionary. Normally this is impossible, so we
    need to do a little trick.
    """
    CHUNK_HANDLER = BaseMemoryChunk

    def __get__(self, obj, _=None):
        return self.CHUNK_HANDLER(address=id(obj), length=sys.getsizeof(obj))

    def __set__(self, obj, value):
        pass
