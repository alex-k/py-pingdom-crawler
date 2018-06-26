from uptimeprovider.UptimeProvider import UptimeProvider


class Pingdom(UptimeProvider):
    def __init__(self):
        pass
    
    def __api_call(self,check_id, time_from, time_to):
        url = "pingdom.com/api/v2/statistic/{}?from={}&to={}".format(check_id, time_from, time_to)
        print url
    
    def get_seconds_up(self, check_id, time_from, time_to):
        self.__api_call(check_id, time_from, time_to)
        return 540;
    
    def get_seconds_down(self, check_id, time_from, time_to):
        self.__api_call(check_id, time_from, time_to)
        return 60;
