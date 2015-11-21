import struct
import ctypes


def integer_to_memory(value):
    """Memory representation for C integer
    """
    return tuple(int(item) for item in struct.pack('@I', value))


def get_flags(klass):
    flags = ctypes.pythonapi.PyType_GetFlags(id(klass))
    pointer = ctypes.cast(id(klass), ctypes.POINTER(ctypes.c_ulong))
    return pointer[:50].index(flags), flags


def set_flags(klass, new_flags):
    index, _ = get_flags(klass)
    ctypes.cast(id(klass), ctypes.POINTER(ctypes.c_ulong))[index] = new_flags


def activate_inheritance(klass):
    set_flags(klass, get_flags(klass)[1] | 1 << 10)


def enforce_class(instance, klass):
    instance.memory = (8, integer_to_memory(id(klass)))
