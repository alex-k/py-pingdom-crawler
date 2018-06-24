import unittest


class test_MySQL(unittest.TestCase):
    def setUp(self):
        from mysql.MySQL import MySQL
        self.db = MySQL()
    
    def test_select_column_from_table(self):
        self.assertEqual([1, 2, 22], self.db.get_all_column_values('checks', 'id'))
