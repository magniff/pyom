import ctypes
from .base import PyObject


class PyFunctionObject(PyObject):
    _fields_ = [
        ('!func_code', ctypes.c_ssize_t),
        ('!func_globals', ctypes.c_ssize_t),
        ('!func_defaults', ctypes.c_ssize_t),
        ('!func_kwdefaults', ctypes.c_ssize_t),
        ('!func_closure', ctypes.c_ssize_t),
        ('!func_doc', ctypes.c_ssize_t),
        ('!func_name', ctypes.c_ssize_t),
        ('!func_dict', ctypes.c_ssize_t),
        ('!func_weakreflist', ctypes.c_ssize_t),
        ('!func_module', ctypes.c_ssize_t),
        ('!func_annotations', ctypes.c_ssize_t),
        ('!func_qualname', ctypes.c_ssize_t),
    ]
