import unittest
import pyom


class TestChunkBasics(unittest.TestCase):

    def test_attrs(self):
        chunk = pyom.Chunk(id(int), 10)
        self.assertTrue(hasattr(chunk, 'length'))
        self.assertTrue(hasattr(chunk, 'address'))

    def test_boundary_check_get(self):
        self.assertRaises(pyom.BoundaryError, lambda: (100).memory[100])
        self.assertRaises(pyom.BoundaryError, lambda: (100).memory[-1])

    def test_boundary_check_set(self):
        def set_too_big():
            (100).memory[100] = 10

        def set_negative():
            (100).memory[-1] = 10

        self.assertRaises(pyom.BoundaryError, set_too_big)
        self.assertRaises(pyom.BoundaryError, set_negative)

    def test_clone(self):
        chunk0 = (100).memory
        chunk1 = chunk0.clone()
        self.assertEqual(chunk0, chunk1)


class TestHandlerBasics(unittest.TestCase):

    def test_memory_handler_type(self):
        self.assertTrue(isinstance((100).memory, pyom.Chunk))

    def test_attrs(self):
        self.assertTrue(hasattr((100).memory, 'length'))
        self.assertTrue(hasattr((100).memory, 'address'))


class TestIntHack(unittest.TestCase):

    # hacks 100 to be another then int class
    def test_int_class_swap(self):
        class Tint(int):
            def __repr__(self):
                return 'tint object'

        obj = 100

        chunk_original = obj.memory
        chunk_copy = chunk_original.clone()

        id_of_int = pyom.integer_to_memory(id(int))
        id_of_tint = pyom.integer_to_memory(id(Tint))

        index = chunk_original[:100].index(id_of_int[0])
        obj.memory = (index, id_of_tint)
        self.assertTrue(isinstance(obj, Tint))
        self.assertTrue(repr(obj) == 'tint object')

    def test_dump_attr_presents(self):
        self.assertTrue(hasattr(object, 'memory'))


if __name__ == '__main__':
    with pyom.wonderland():
        unittest.main()
