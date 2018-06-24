from abc import ABCMeta, abstractmethod


class Db:
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
    
    @abstractmethod
    def get_all_column_values(self, table_name, column_name):
        pass
    
    @abstractmethod
    def get_values_by(self, table_name, column_names, criteria):
        pass
