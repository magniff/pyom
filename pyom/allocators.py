import ctypes
import functools
import sys


@functools.lru_cache(maxsize=None)
def _select_libc():
    if 'win' in sys.platform.lower():
        dll = ctypes.CDLL('msvcrt')
    else:
        dll = ctypes.CDLL('libc')
    return dll


def malloc(count, chunk_class):
    return chunk_class(_select_libc().malloc(count), count)


def free(address):
    return _select_libc().free(address)
