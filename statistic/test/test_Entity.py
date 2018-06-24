import unittest
from statistic.Entity import Entity


class TestEntity(unittest.TestCase):

    def test_NotExists(self):
        period = Entity(1, 100500)
        self.assertFalse(period.exists())
        
        with self.assertRaises(Exception) as context:
            period.get_up_seconds()
        self.assertTrue('unexisted period' in context.exception)

        with self.assertRaises(Exception) as context:
            period.get_down_seconds()
        self.assertTrue('unexisted period' in context.exception)
        
        period.set_up_seconds(1)
        self.assertFalse(period.exists())

        with self.assertRaises(Exception) as context:
            period.get_up_seconds()
        self.assertTrue('unexisted period' in context.exception)

        with self.assertRaises(Exception) as context:
            period.get_down_seconds()
        self.assertTrue('unexisted period' in context.exception)

    def test_NotExists(self):
        period = Entity(1, 100500)
        period.set_up_seconds(540)
        period.set_down_seconds(60)
        
        self.assertEqual(1, period.get_check_id())
        self.assertEqual(100500, period.get_time())
        self.assertTrue(period.exists())
        self.assertEqual(540,period.get_up_seconds())
        self.assertEqual(60,period.get_down_seconds())
