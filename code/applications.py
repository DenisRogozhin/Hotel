class Reserve_application():
    
    def __init__(self, configuration, first_day, last_day):
        self.configuration = configuration
        self.first_day = first_day
        self.last_day = last_day
        
        
class Settle_application():
    
    def __init__(self, configuration, current_day, day_count):
        self.configuration = configuration
        self.day_count = day_count
        self.current_day = current_day