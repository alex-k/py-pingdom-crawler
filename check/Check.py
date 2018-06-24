class Check:
    __check_id = None
    
    def __init__(self, check_id):
        self.__check_id = check_id

    def __eq__(self, other):
        return self.__check_id == other.__check_id
    
    def get_check_id(self):
        return self.__check_id