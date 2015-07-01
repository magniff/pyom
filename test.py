import unittest
import pyom


class TestChunk(unittest.TestCase):

    def test_set(self):
        def assign_negative_shift():
            pyom.Chunk(-10, [1, 2, 3])

        def assign_non_iterable_data():
            pyom.Chunk(10, 10)

        def assign_non_int_data():
            pyom.Chunk(10, ['hello', 10])

        def assign_data_to_big():
            pyom.Chunk(10, [10, 10000])

        self.assertRaises(ValueError, assign_negative_shift)
        self.assertRaises(ValueError, assign_non_iterable_data)
        self.assertRaises(ValueError, assign_non_int_data)
        self.assertRaises(ValueError, assign_data_to_big)


class TestIntHack(unittest.TestCase):

    def test_dump_attr_presents(self):
        self.assertTrue(
            hasattr(object, pyom.ATTR_TO_INJECT),
            'Fail to inject attr %s' % pyom.ATTR_TO_INJECT
        )

    # this hacks value of int 100 to be 200
    def test_value_hack(self):
        index = (100).dump[:20].index(100)
        (100).dump[index] = 200
        self.assertEqual(100, 200)


if __name__ == '__main__':
    pyom.activate()
    unittest.main()
    pyom.deactivate()