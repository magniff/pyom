import struct


def integer_to_memory(value):
    """Memory representation for C integer
    """
    return tuple(map(int, struct.pack('@I', value)))
