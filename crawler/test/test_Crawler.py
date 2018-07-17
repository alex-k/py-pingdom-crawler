import unittest
import crawler
from repository.dummy.Dummy import Dummy


class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.db = Dummy()

    def test_crawl_all_checks(self):
        crawler.crawl_all_checks(self.db)
