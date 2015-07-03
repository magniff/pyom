import ctypes
import sys

from .exceptions import InsufficientMemory


def _select_libc():
    platform = sys.platform.lower()
    if 'win' in platform:
        dll = ctypes.CDLL('msvcrt')
    elif 'linux' in platform:
        dll = ctypes.CDLL('libc.so.6')
    else:
        raise RuntimeError('Your platform is not supported. Sorry.')
    return dll


LIBC_REALIZATION = _select_libc()


def memcpy(dest_chunk, source_chunk):
    return LIBC_REALIZATION.memcpy(
        dest_chunk.address, source_chunk.address, source_chunk.length
    )


def malloc(count, chunk_class):
    address = LIBC_REALIZATION.malloc(count)

    if not address:
        raise InsufficientMemory(count)

    return chunk_class(address, count)


def free(address):
    return LIBC_REALIZATION.free(address)
