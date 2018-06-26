from datetime import datetime, timedelta
import calendar


class Calendar:
    
    @staticmethod
    def get_utc_date(d):
        return datetime.fromtimestamp(calendar.timegm(d.utctimetuple()))
    
    @staticmethod
    def get_first_day_in_month_utc(year, month):
        return Calendar.get_utc_date(datetime(year, month, 1, 0, 0, 0, 0))
    
    @staticmethod
    def get_first_day_in_next_month_utc(year, month):
        sourcedate = datetime(year, month, 1, 0, 0, 0, 0)
        month = sourcedate.month - 1 + 1
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return Calendar.get_utc_date(datetime(year, month, day))
    
    @staticmethod
    def get_next_day(date):
        # type: (datetime) -> datetime
        return date + timedelta(days=1)
    
    @staticmethod
    def get_all_days_in_month_utc(year, month):
        days = []
        
        day = Calendar.get_first_day_in_month_utc(year, month)
        end_day = Calendar.get_first_day_in_next_month_utc(year, month)
        while day < end_day:
            days.append(day)
            day = Calendar.get_next_day(day)
        
        return days
