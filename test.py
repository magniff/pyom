import unittest
import pyom

pyom.activate()


class TestIntHack(unittest.TestCase):

    # this hacks value of int 100 to be 200
    def test_value_hack(self):
        index = (100).dump[:20].index(100)
        (100).dump[index] = 200
        self.assertEqual(100, 200)


if __name__ == '__main__':
    unittest.main()
