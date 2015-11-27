import unittest

from util import MyArray


class TestUtil(unittest.TestCase):
    my_array = MyArray()

    def test_empty_array_returns_empty_array(self):
        empty_array = []
        flat_array = self.my_array.flat(empty_array)
        self.assertEqual(flat_array, empty_array)

    def test_onedimension_array_returns_same_array(self):
        onedimension_array = [1, 2, 3]
        flat_array = self.my_array.flat(onedimension_array)
        self.assertEqual(flat_array, onedimension_array)

    def test_twodimension_array_returns_flat_array(self):
        onedimension_array = [1, [4, 5], 3]
        flat_array = self.my_array.flat(onedimension_array)
        self.assertEqual(flat_array, [1, 4, 5, 3])

    def test_insane_array_returns_flat_array(self):
        insane_array = [1, [4, 5], [6, 7, 8, [10, 1, 12]], 3]
        flat_array = self.my_array.flat(insane_array)
        self.assertEqual(flat_array, [1, 4, 5, 6, 7, 8, 10, 1, 12, 3])

    def test_even_strings_returns_flat_array(self):
        strings_array = ["nicolas", "is", "awesome", ["hell", ["yeah!"]]]
        flat_array = self.my_array.flat(strings_array)
        self.assertEqual(flat_array, ["nicolas", "is", "awesome", "hell", "yeah!"])

    def test_your_example_returns_flat_array(self):
        your_array = [[1, 2, [3]], 4]
        flat_array = self.my_array.flat(your_array)
        self.assertEqual(flat_array, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
