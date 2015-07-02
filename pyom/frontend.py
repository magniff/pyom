import ctypes

from .memio import ObjectMemoryIO


ATTR_TO_INJECT = 'memory'
OBJECT_DICT = ctypes.cast(
    id(object)+type.__dictoffset__, ctypes.POINTER(ctypes.py_object)
)


def activate(memory_viewer=None):
    OBJECT_DICT[0][ATTR_TO_INJECT] = (
        memory_viewer() if memory_viewer else ObjectMemoryIO()
    )


def deactivate():
    del OBJECT_DICT[0][ATTR_TO_INJECT]
