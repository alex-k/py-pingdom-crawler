from Check import Check
from db.Db import Db

class Service:
    __db = None
    
    def __init__(self, db = Db):
        self.__db = db
    
    def __get_all_checks_ids(self):
        return self.__db.select_column_from_table('checks','id')
    
    def get_all_checks(self):
        checks = []
        for check_id in self.__get_all_checks_ids():
            checks.append(Check(check_id))
        return checks
