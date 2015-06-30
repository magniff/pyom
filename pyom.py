import ctypes


ATTR_TO_INJECT = 'dump'


class LLReader:

    def __get__(self, obj, klass=None):
        pointer = ctypes.cast(id(obj), ctypes.POINTER(ctypes.c_ubyte))
        return pointer

    def __set__(self, obj, value):
        pass

    def __dell__(self, obj):
        pass


object_dict = ctypes.cast(
    id(object)+type.__dictoffset__, ctypes.POINTER(ctypes.py_object)
)


def activate():
    object_dict[0][ATTR_TO_INJECT] = LLReader()


def deactivate():
    del object_dict[0][ATTR_TO_INJECT]
