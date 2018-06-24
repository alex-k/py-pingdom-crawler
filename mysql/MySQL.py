from db.Db import Db


class MySQL(Db):
    def __init__(self):
        pass
    
    def get_all_column_values(self, table_name, column_name):
        return [1, 2, 22]
    
    def get_values_by(self, table_name, column_names, criteria):
        if criteria['check_id'] == 1 and criteria['timestamp'] == 1529798400:
            return {
                'check_id': criteria['check_id'],
                'totaldown': 60,
                'totalup': 540,
                'timestamp': criteria['timestamp']
            }
        else:
            return {}
