import ctypes


class BaseStructure(ctypes.Structure):

    @classmethod
    def from_address(cls, address):
        return ctypes.cast(address, ctypes.POINTER(cls))[0]

    @classmethod
    def from_object(cls, obj):
        return cls.from_address(id(obj))


class PyObject(BaseStructure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),
        ('ob_type', ctypes.c_ssize_t),
    ]


class PyVarObject(PyObject):
    _fields_ = [
        ('ob_size', ctypes.c_int),
    ]


class PyTypeObject(PyVarObject):
    _fields_ = [
        ('tp_name', ctypes.c_ssize_t),
        ('tp_basicsize', ctypes.c_int),
        ('tp_itemsize', ctypes.c_int),

        ('tp_dealloc', ctypes.c_ssize_t),
        ('tp_print', ctypes.c_ssize_t),
        ('tp_getattr', ctypes.c_ssize_t),
        ('tp_setattr', ctypes.c_ssize_t),
        ('tp_reserved', ctypes.c_ssize_t),
        ('tp_repr', ctypes.c_ssize_t),

        ('tp_as_number', ctypes.c_ssize_t),
        ('tp_as_sequence', ctypes.c_ssize_t),
        ('tp_as_mapping', ctypes.c_ssize_t),

        ('tp_hash', ctypes.c_ssize_t),
        ('tp_call', ctypes.c_ssize_t),
        ('tp_str', ctypes.c_ssize_t),
        ('tp_getattro', ctypes.c_ssize_t),
        ('tp_setattro', ctypes.c_ssize_t),

        ('tp_as_buffer', ctypes.c_ssize_t),
        ('tp_flags', ctypes.c_long),
    ]

    def activate_inheritance(self):
        self.tp_flags |= 1 << 10
