import ctypes
from pyom.memio import BaseMemIO, ChunkSetter as Chunk


ATTR_TO_INJECT = 'memory'


object_dict = ctypes.cast(
    id(object)+type.__dictoffset__, ctypes.POINTER(ctypes.py_object)
)


def activate(memory_viewer=None):
    object_dict[0][ATTR_TO_INJECT] = (
        memory_viewer() if memory_viewer else BaseMemIO()
    )


def deactivate():
    del object_dict[0][ATTR_TO_INJECT]
