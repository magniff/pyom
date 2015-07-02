import collections
import ctypes
import functools
import struct
import sys


mem = collections.namedtuple('mem', ('addr', 'handle'))


@functools.lru_cache
def _select_libc():
    if 'win' in sys.platform.lower():
        dll = ctypes.CDLL('msvcrt')
    else:
        dll = ctypes.CDLL('libc')
    return dll


def malloc(count):
    addr = _select_libc().malloc(count)
    return mem(
        addr=addr,
        handle=ctypes.cast(addr, ctypes.POINTER(ctypes.c_ubyte))
    )


def free(address):
    return _select_libc().free(address)


def integer_to_memory(value):
    """Memory representation for C integer
    """
    return tuple(int(item) for item in struct.pack('@I', value))
