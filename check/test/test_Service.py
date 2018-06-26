import unittest
from check.Service import *
from check.Check import *
from repository.dummy.Dummy import Dummy

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(Dummy())
    
    def test_get_all_checks(self):
        checks = [Check(1), Check(2), Check(22)]
        self.assertEqual(checks, self.service.get_all_checks())
