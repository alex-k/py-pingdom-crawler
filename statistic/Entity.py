class Entity:
    __check_id = None
    __time = None
    __up_seconds = None
    __down_seconds = None
    
    def __init__(self, check_id, time):
        self.__check_id = check_id
        self.__time = time
    
    def get_check_id(self):
        return self.__check_id
    
    def get_time(self):
        return self.__time
    
    def set_up_seconds(self, seconds):
        self.__up_seconds = seconds

    def get_up_seconds(self):
        if self.exists():
            return self.__up_seconds
        else:
            raise Exception('unexisted period')
        
    def set_down_seconds(self, seconds):
        self.__down_seconds = seconds
        
    def get_down_seconds(self):
        if self.exists():
            return self.__down_seconds
        else:
            raise Exception('unexisted period')
    
    def exists(self):
        return self.__up_seconds and self.__down_seconds
