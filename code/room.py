from room_type import *

class Room():

    def __init__(self, id_):
        self.free = True
        self.reserved = [] # [(day_st, day_fin, room_type)]
        # указание типа нужно, чтобы знать, в качестве комнаты какого типа сдается комната в данный период
        self.id = id_
        
        
    def try_reserve(self, start_day, end_day):        
        for first_reserved, last_reserved, _ in self.reserved:
            if start_day >= last_reserved:
                continue
            #если мы тут, значит start_day < last_reversed
            if end_day <= first_reserved:
                return True, self.id
            else:
                return False, None
        return True, self.id
    
    def reserve(self, start_day, end_day, room_type):
        self.reserved.append((start_day, end_day, room_type))
        self.reserved = sorted(self.reserved, key = lambda x: x[0])
    
    def try_settle(self, current_day, day_count):
        return self.try_reserve(current_day, current_day + day_count)
    
    def settle(self, current_day, day_count, room_type):
        return self.reserve(current_day, current_day + day_count, room_type)