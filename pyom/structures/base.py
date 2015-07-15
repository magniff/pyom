import ctypes


class obj_pointer(ctypes.c_ssize_t):
    pass


class PropMeta(type(ctypes.Structure)):

    PREFIX = '!'

    @classmethod
    def make_property(cls, f_name):
        def prop_field(self):
            return ctypes.cast(
                getattr(self, f_name.lstrip(cls.PREFIX)),
                ctypes.POINTER(ctypes.py_object)
            )[0]

        return property(prop_field)

    def __new__(cls, name, bases, attrs):
        fields = attrs.get('_fields_', tuple())

        additional_attrs = {
            f_name.lstrip(cls.PREFIX)+'_o': cls.make_property(f_name) for
            f_name, _ in fields if f_name.startswith(cls.PREFIX)
        }

        fixed_fields = [
            (attr_name.lstrip(cls.PREFIX), attr_value) for
            attr_name, attr_value in fields
        ]

        attrs['_fields_'] = fixed_fields

        attrs.update(additional_attrs)
        return super().__new__(cls, name, bases, attrs)


class BaseStructure(ctypes.Structure, metaclass=PropMeta):
    @classmethod
    def from_object(cls, obj):
        return ctypes.cast(id(obj), ctypes.POINTER(cls))[0]


class PyObject(BaseStructure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),
        ('!ob_type', ctypes.c_ssize_t),
    ]


class PyVarObject(PyObject):
    _fields_ = [
        ('ob_size', ctypes.c_int),
    ]


class PyTypeObject(PyVarObject):
    _fields_ = [
        ('tp_name', ctypes.c_ssize_t),
    ]
