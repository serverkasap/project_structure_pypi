import unittest
from celebrity_births.scraper import Scraper
from celebrity_births.date import Date

class CelebrityTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_celebrity_with_date(self):
        date = Date(27, 3, 2020).to_wiki_format()
        celebrities = self.scraper.get_celebrities(date)
        self.assertIn('Quentin Tarantino', celebrities)