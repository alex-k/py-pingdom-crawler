from uptimeprovider.UptimeProvider import UptimeProvider


class Pingdom(UptimeProvider):
    def __init__(self):
        pass
    
    def get_seconds_up(self, check_id, time_from, time_to):
        return 540;
    
    def get_seconds_down(self, check_id, time_from, time_to):
        return 60;
