import struct


def integer_to_memory(value):
    return tuple(map(int, struct.pack("<I", value)))
