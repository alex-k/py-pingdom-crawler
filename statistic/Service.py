from statistic.Entity import Entity
from repository.Repository import Repository
from repository.dummy.Dummy import Dummy

class Service:
    __db = None
    
    def __init__(self, db):
        self.__db = db
    
    def get_period(self, check_id, time):
        period = Entity(check_id, time)
        
        row = self.__db.get_statistic(check_id, time)
        if 'check_id' in row and row['check_id'] == check_id:
            if 'totalup' in row:
                period.set_up_seconds(row['totalup'])
            if 'totaldown' in row:
                period.set_down_seconds(row['totaldown'])
        
        return period
