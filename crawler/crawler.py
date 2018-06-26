from check.Service import Service as ChecksService
from statistic.Service import Service as StatisticService
from pingdom.Pingdom import Pingdom
from my_calendar.Calendar import Calendar
import datetime


def crawl_all_checks(repository):
    checks_service = ChecksService(repository)
    statistic_service = StatisticService(repository)
    crawler = Pingdom()
    
    date = datetime.datetime.now()
    
    print date.year
    print date.month
    days = Calendar.get_all_days_in_month_utc(date.year, date.month)
    
    day = days[0]
    
    print(day)
    
    check = checks_service.get_all_checks()[0]
    
    print(check)
    
    seconds = crawler.get_seconds_up(check.get_check_id(),
                                     day.strftime("%s"),
                                     Calendar.get_next_day(day).strftime("%s")
                                     )
    
    print seconds
    # for check in checks_service.get_all_checks():
    #     print(check.get_check_id())
    # #     # print(crawler.get_seconds_up(check.get_check_id(), 1529770607, 1529770618))
