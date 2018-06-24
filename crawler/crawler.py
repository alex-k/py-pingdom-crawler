from check.Service import Service as ChecksService
from mysql.MySQL import MySQL
from pingdom.Pingdom import Pingdom


def crawl_all_checks():
    service = ChecksService(MySQL())
    crawler = Pingdom()
    
    for check in service.get_all_checks():
        print(check.get_check_id())
        print(crawler.get_seconds_up(check.get_check_id(), 1529770607, 1529770618))

