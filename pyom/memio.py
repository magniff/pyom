import ctypes

from .hanlers import Chunk


class BaseMemIO:
    """This is simple descriptor, which instance we are going to inject into
    object`s (common base class) dictionary. Normally this is impossible, so we
    need to do a little trick.
    """
    def _get_pointer(self, obj):
        return ctypes.cast(id(obj), ctypes.POINTER(ctypes.c_ubyte))

    def __get__(self, obj, _=None):
        return self._get_pointer(obj)

    def __set__(self, obj, chunk_object):
        if not isinstance(chunk_object, Chunk):
            raise ValueError('%s is not instance of Chunk.' % chunk_object)

        pointer = self._get_pointer(obj)
        for index, value in enumerate(chunk_object.data, chunk_object.shift):
            pointer[index] = value
