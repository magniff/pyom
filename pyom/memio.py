import ctypes
import logging

from .hanlers import BaseChunkSetter


class BaseChunkProxy:

    def __repr__(self):
        return "<Entity '%s' -> [%s, ...]>" % (
            self.entity, ', '.join(str(item) for item in self.pointer[:5])
        )

    def __iter__(self):
        logging.warn('Bad idea, srsly use slices!')
        logging.warn('Request skipped.')
        return iter(tuple())

    def __getitem__(self, item):
        return self.pointer.__getitem__(item)

    def __setitem__(self, item_name, item_value):
        self.pointer.__setitem__(item_name, item_value)

    def __init__(self, entity, pointer):
        self.entity = entity
        self.pointer = pointer


class BaseMemIO:
    """This is simple descriptor, which instance we are going to inject into
    object`s (common base class) dictionary. Normally this is impossible, so we
    need to do a little trick.
    """

    GETTER = BaseChunkProxy
    SETTER = BaseChunkSetter

    def _get_pointer(self, obj):
        return ctypes.cast(id(obj), ctypes.POINTER(ctypes.c_ubyte))

    def __get__(self, obj, _=None):
        return self.GETTER(obj, self._get_pointer(obj))

    def __set__(self, obj, chunk_object):
        if not isinstance(chunk_object, self.SETTER):
            raise TypeError(
                '%s is not instance of %s.' % (chunk_object, self.SETTER)
            )

        chunk_object._dump_data(self._get_pointer(obj))
