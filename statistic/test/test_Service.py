import unittest
from statistic.Service import Service
from mysql.MySQL import MySQL


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(MySQL())
    
    def testGetExistedPeriod(self):
        period = self.service.get_period(1, 1529798400)
        self.assertEqual(1, period.get_check_id())
        self.assertEqual(1529798400, period.get_time())
        self.assertTrue(period.exists())
        self.assertEqual(60, period.get_down_seconds())
        self.assertEqual(540, period.get_up_seconds())
    
    def testGetUnExistedPeriod(self):
        period = self.service.get_period(1, 1529712000)
        self.assertEqual(1, period.get_check_id())
        self.assertEqual(1529712000, period.get_time())
        self.assertFalse(period.exists())
