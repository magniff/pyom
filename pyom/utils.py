import struct


def integer_to_memory(value):
    """Memory representation for C integer
    """
    return tuple(int(item) for item in struct.pack('@I', value))
