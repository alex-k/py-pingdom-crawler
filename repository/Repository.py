from abc import ABCMeta, abstractmethod


class Repository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_checks(self):
        pass
    
    @abstractmethod
    def get_statistic(self, check_id, timestamp):
        # type: (int, int) -> dict
        pass

