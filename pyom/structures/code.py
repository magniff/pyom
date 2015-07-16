import ctypes
from .base import PyObject


class PyCodeObject(PyObject):
    _fields_ = [
        ('co_argcount', ctypes.c_int),
        ('co_kwonlyargcount', ctypes.c_int),
        ('co_nlocals', ctypes.c_int),
        ('co_stacksize', ctypes.c_int),
        ('co_flags', ctypes.c_int),
        ('co_code', ctypes.c_ssize_t),
        ('co_consts', ctypes.c_ssize_t),
        ('co_names', ctypes.c_ssize_t),
        ('co_varnames', ctypes.c_ssize_t),
        ('co_freevars', ctypes.c_ssize_t),
        ('co_cellvars', ctypes.c_ssize_t),
    ]


# typedef struct {
#     PyObject_HEAD
#     int co_argcount;        /* #arguments, except *args */
#     int co_kwonlyargcount;    /* #keyword only arguments */
#     int co_nlocals;        /* #local variables */
#     int co_stacksize;        /* #entries needed for evaluation stack */
#     int co_flags;        /* CO_..., see below */
#     PyObject *co_code;        /* instruction opcodes */
#     PyObject *co_consts;    /* list (constants used) */
#     PyObject *co_names;        /* list of strings (names used) */
#     PyObject *co_varnames;    /* tuple of strings (local variable names) */
#     PyObject *co_freevars;    /* tuple of strings (free variable names) */
#     PyObject *co_cellvars;      /* tuple of strings (cell variable names) */
#     /* The rest doesn't count for hash or comparisons */
#     unsigned char *co_cell2arg; /* Maps cell vars which are arguments. */
#     PyObject *co_filename;    /* unicode (where it was loaded from) */
#     PyObject *co_name;        /* unicode (name, for reference) */
#     int co_firstlineno;        /* first source line number */
#     PyObject *co_lnotab;    /* string (encoding addr<->lineno mapping) See
#                    Objects/lnotab_notes.txt for details. */
#     void *co_zombieframe;     /* for optimization only (see frameobject.c) */
#     PyObject *co_weakreflist;   /* to support weakrefs to code objects */
# } PyCodeObject;
