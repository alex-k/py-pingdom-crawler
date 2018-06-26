import crawler.crawler
from repository.dummy.Dummy import Dummy
from repository.mysql.MySQL import MySQL

crawler.crawler.crawl_all_checks(Dummy())
