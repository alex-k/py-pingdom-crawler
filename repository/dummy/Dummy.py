from repository.Repository import Repository


class Dummy(Repository):
    def __init__(self):
        pass
    
    def get_all_checks(self):
        return [1, 2, 22]

    def get_statistic(self, check_id, timestamp):
        if check_id == 1 and timestamp == 1529798400:
            return {
                'check_id': 1,
                'totaldown': 60,
                'totalup': 540,
                'timestamp': 1529798400
            }
        else:
            return {}
