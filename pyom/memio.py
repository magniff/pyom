import sys

from .getsets import BaseMemoryChunk
from .exceptions import BoundaryError


class ObjectMemoryIO:
    """This is simple descriptor, which instance we are going to inject into
    object`s (common base class) dictionary. Normally this is impossible, so we
    need to do a little trick.
    """
    CHUNK_HANDLER = BaseMemoryChunk

    def __get__(self, obj, _=None):
        return self.CHUNK_HANDLER(address=id(obj), length=sys.getsizeof(obj))

    def __set__(self, obj, value):
        shift, data = value
        chunk = self.CHUNK_HANDLER(id(obj), sys.getsizeof(obj))

        if shift + len(data) > chunk.length:
            raise BoundaryError(chunk)

        for index, byte_to_set in enumerate(data, shift):
            chunk[index] = byte_to_set
