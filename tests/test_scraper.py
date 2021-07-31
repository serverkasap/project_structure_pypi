import unittest
from celebrity_births.scraper import Scraper

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_wrong_date(self):
        date = 'February_30'
        with self.assertRaises(ValueError) as err:
            self.scraper.get_celebrities(date)
    
    def test_birth_header(self):
        date = 'March_27'
        h2 = self.scraper._get_birth_header(date)
        self.assertEqual(h2.text, 'Births[edit]')