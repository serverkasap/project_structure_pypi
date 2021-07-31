import unittest
from celebrity_births.date import Date


class DateTestCase(unittest.TestCase):
    def test_lower_than(self):
        date_1 = Date(1, 5, 2020)
        date_2 = Date(2, 3, 2050)
        self.assertLess(date_1, date_2)
    
    def test_date_validity(self):
        with self.assertRaises(ValueError) as err:
            Date(32, 5, 2020)
    
    def test_from_string(self):
        date_1 = Date(1, 5, 2020)
        date_2 = Date.from_string('1-5-2020')
        self.assertEqual(date_1, date_2)