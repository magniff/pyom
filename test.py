import unittest
import ctypes
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

    def test_not_equal(self):
        self.assertNotEqual((100).memory, 'helloworld'.memory)


class TestHandlerBasics(unittest.TestCase):

    def test_memory_handler_type(self):
        self.assertTrue(isinstance((100).memory, pyom.Chunk))

    def test_attrs(self):
        self.assertTrue(hasattr((100).memory, 'length'))
        self.assertTrue(hasattr((100).memory, 'address'))


if __name__ == '__main__':
    with pyom.wonderland():
        unittest.main()
