import unittest
from .craigslist_toronto_scraper import Command, get_list_of_dict_from_soup


class TestCraigsListScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Command()

    def test_query_none(self):
        self.assertRaises(KeyError, lambda: self.scraper.handle(None))

    def test_get_list_of_dict_no_soup(self):
        with self.assertRaises(TypeError):
            get_list_of_dict_from_soup(None)


if __name__ == '__main__':
    unittest.main()
