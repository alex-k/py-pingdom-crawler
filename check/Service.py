from Check import Check
from repository.Repository import Repository


class Service:
    __db = None
    
    def __init__(self, db=Repository):
        self.__db = db
    
    def __get_all_checks_ids(self):
        ids = self.__db.get_all_checks()
        return ids
    
    def get_all_checks(self):
        checks = []
        for check_id in self.__get_all_checks_ids():
            checks.append(Check(check_id))
        return checks
