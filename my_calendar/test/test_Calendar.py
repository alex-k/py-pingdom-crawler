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
        date = datetime.datetime.now(datetime.timezone.utc)
        days = Calendar.get_all_days_in_month_utc(2018, 2)
        self.assertEqual(28, len(days))
        self.assertEqual('1517443200', days[0].strftime("%s"))
        self.assertEqual('1519776000', days[-1].strftime("%s"))
