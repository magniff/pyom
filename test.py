import unittest
import pyom


class TestChunk(unittest.TestCase):

    def test_set(self):
        def assign_negative_shift():
            pyom.Chunk(shift=-10, data=[1, 2, 3])

        def assign_non_iterable_data():
            pyom.Chunk(shift=10, data=10)

        def assign_non_int_data():
            pyom.Chunk(shift=10, data=['hello', 10])

        def assign_data_to_big():
            pyom.Chunk(shift=10, data=[10, 10000])

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
        index = getattr(100, pyom.ATTR_TO_INJECT)[:20].index(100)
        getattr(100, pyom.ATTR_TO_INJECT)[index] = 200
        self.assertEqual(100, 200)


if __name__ == '__main__':
    pyom.activate()
    unittest.main()
    pyom.deactivate()
