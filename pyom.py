import ctypes


ATTR_TO_INJECT = 'dump'


class LLReader:
    """This is simple descriptor, which instance we are going to inject into
    object`s (common base class) dictionary. Normally this is impossible, so we
    need to do a little trick.
    """
    def __get__(self, obj, _=None):
        return ctypes.cast(id(obj), ctypes.POINTER(ctypes.c_ubyte))

    def __set__(self, obj, value):
        pass


object_dict = ctypes.cast(
    id(object)+type.__dictoffset__, ctypes.POINTER(ctypes.py_object)
)


def activate(memory_viewer=None):
    object_dict[0][ATTR_TO_INJECT] = (
        memory_viewer() if memory_viewer else LLReader()
    )


def deactivate():
    del object_dict[0][ATTR_TO_INJECT]
