from statistic.Entity import Entity
from db.Db import Db


class Service:
    __db = None
    
    def __init__(self, db=Db):
        self.__db = db
    
    def get_period(self, check_id, time):
        period = Entity(check_id, time)
        
        row = self.__db.get_values_by('statistic',
                                      ['check_id', 'totalup', 'totaldown', 'timestamp'],
                                      {'check_id': check_id, 'timestamp': time}
                                      )
        if 'check_id' in row and row['check_id'] == check_id:
            if 'totalup' in row:
                period.set_up_seconds(row['totalup'])
            if 'totaldown' in row:
                period.set_down_seconds(row['totaldown'])
        
        return period
