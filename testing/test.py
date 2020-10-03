from my_sum import summer

import unittest
from fractions import Fraction

class TestCase(unittest.TestCase):
    """
    docstring
    """
    def test_int_list(self):
        """
        docstring
        """
        data = [1,2,3]
        result = summer(data)
        self.assertEqual(result,6)

    def test_fractions(self ):
        """
        docstring
        """
        fract_array = [Fraction(1/4),Fraction(1/4),Fraction(1/2)]
        result = summer(fract_array)
        self.assertEqual(result,3)

if __name__ == "__main__":
    unittest.main()