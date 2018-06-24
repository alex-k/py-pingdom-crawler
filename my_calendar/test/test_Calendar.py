import unittest
from my_calendar.Calendar import Calendar
import datetime


class TestCalendar(unittest.TestCase):
    
    def test_get_utc_date(self):
        day = Calendar.get_utc_date(datetime.datetime(2011, 8, 22, 0, 0, 0))
        self.assertEqual('1313971200', day.strftime("%s"))
    
    def test_get_current_month(self):
        month = Calendar.get_first_day_in_month_utc(2011, 8)
        self.assertEqual('1312156800', month.strftime("%s"))
    
    def test_get_next_month(self):
        month = Calendar.get_first_day_in_next_month_utc(2011, 8)
        self.assertEqual('1314835200', month.strftime("%s"))
    
    def test_get_next_day(self):
        month = Calendar.get_first_day_in_month_utc(2011, 8)
        next_day = Calendar.get_next_day(month)
        self.assertEqual('1312243200', next_day.strftime("%s"))
    
    def test_get_all_days_in_month(self):
        days = Calendar.get_all_days_in_month_utc(2018, 2)
        self.assertEqual(28, len(days))
        self.assertEqual(datetime.datetime(2018, 2, 1, 3, 0), days[0])
        self.assertEqual(datetime.datetime(2018, 2, 28, 3, 0), days[-1])
