import unittest
from repository.dummy.Dummy import Dummy


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.db = Dummy()
    
    def test_select_column_from_table(self):
        self.assertEqual([1, 2, 22], self.db.get_all_checks())
    
    def test_get_statistic(self):
        self.assertEqual(self.db.get_statistic(1, 1529798400),
                         {
                             'check_id': 1,
                             'totaldown': 60,
                             'totalup': 540,
                             'timestamp': 1529798400
                         })
    
    def test_get_unexisted_statistic(self):
        self.assertEqual(self.db.get_statistic(1, 1529798200), {})
        self.assertEqual(self.db.get_statistic(2, 1529798400), {})
