import ctypes

from .getsets import BaseChunkSetter, BaseChunkGetter


class BaseMemIO:
    """This is simple descriptor, which instance we are going to inject into
    object`s (common base class) dictionary. Normally this is impossible, so we
    need to do a little trick.
    """

    GETTER = BaseChunkGetter
    SETTER = BaseChunkSetter

    @staticmethod
    def _get_pointer(obj):
        return ctypes.cast(id(obj), ctypes.POINTER(ctypes.c_ubyte))

    def __get__(self, obj, _=None):
        return self.GETTER(obj, self._get_pointer(obj))

    def __set__(self, obj, chunk_object):
        if not isinstance(chunk_object, self.SETTER):
            raise TypeError(
                '%s is not instance of %s.' % (chunk_object, self.SETTER)
            )

        chunk_object.dump_data(self._get_pointer(obj))
