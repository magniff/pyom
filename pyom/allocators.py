import ctypes
import functools
import sys

from .exceptions import InsufficientMemory


@functools.lru_cache(maxsize=None)
def _select_libc():
    if 'win' in sys.platform.lower():
        dll = ctypes.CDLL('msvcrt')
    else:
        dll = ctypes.CDLL('libc.so.6')
    return dll


def malloc(count, chunk_class):
    address = _select_libc().malloc(count)

    if not address:
        raise InsufficientMemory(count)

    return chunk_class(address, count)


def free(address):
    return _select_libc().free(address)
