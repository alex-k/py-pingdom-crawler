import unittest
from pingdom.Pingdom import Pingdom


class TestPingdom(unittest.TestCase):
    def setUp(self):
        self.crawler = Pingdom()

    def test_get_seconds_up(self):
        self.assertEqual(self.crawler.get_seconds_up(1, 0, 0), 540)

    def test_get_seconds_down(self):
        self.assertEqual(self.crawler.get_seconds_down(1, 0, 0), 60)
