import ctypes


class BaseStructure(ctypes.Structure):
    @classmethod
    def from_object(cls, obj):
        return ctypes.cast(id(obj), ctypes.POINTER(cls))[0]


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
    ]
