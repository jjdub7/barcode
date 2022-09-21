import unittest
from barcode.maths import calculate_check_digit

class BarcodeCheckDigitTests(unittest.TestCase):

    def test_GTIN_8(self):
        test_value = 7241193
        expected_value = 3

        self.assertEqual(expected_value, calculate_check_digit(test_value))

    def test_GTIN_12(self):
        test_value = 31231234312
        expected_value = 7

        self.assertEqual(expected_value, calculate_check_digit(test_value))

    def test_GTIN_13(self):
        test_value = 531241238312
        expected_value = 7

        self.assertEqual(expected_value, calculate_check_digit(test_value))

    def test_GTIN_14(self):
        test_value = 8273471003231
        expected_value = 3

        self.assertEqual(expected_value, calculate_check_digit(test_value))

    def test_GSIN(self):
        test_value = 5235235423541150
        expected_value = 6

        self.assertEqual(expected_value, calculate_check_digit(test_value))

    def test_SSCC(self):
        test_value = 91012934234951122
        expected_value = 6

        self.assertEqual(expected_value, calculate_check_digit(test_value))

    def test_invalid(self):
        test_value = 1

        with self.assertRaises(ValueError) as errContext:
            calculate_check_digit(test_value)
        self.assertIn('Invalid length for non-check-digits.  Valid lengths are [7, 11, 12, 13, 16, 17]', str(errContext.exception))
