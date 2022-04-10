from room import *

class Hotel():
    
    def __init__(self, configuration, prices):
        self.profit = 0
        
        self.rooms = dict()
        room_id = 500
        for room_type in RoomType:
            self.rooms[room_type] = [Room(room_id + i) for i in range(configuration[room_type])]
            room_id = room_id - 100
        
        self.prices = prices
        
        self.reserve_application_accepted = 0
        self.reserve_application_not_accepted = 0
        
        self.settle_application_accepted = 0
        self.settle_application_not_accepted = 0
        
        self.greater_type_count = 0
   
    def accept_reserve_application(self, reserve_application):
        print("==================================================")
        print("Получена заявка на бронирование!!!!!")
        for room_type in RoomType:
            print(room_type, ':', reserve_application.configuration[room_type])
        print("День заселения:", reserve_application.first_day)
        print("День выселения:", reserve_application.last_day)
        print("==================================================")
        
        reserved_all = True
        already_reserved = dict()
        for room_type in RoomType:
            for i in range(reserve_application.configuration[room_type]):
                cur_room_type = room_type
                while cur_room_type != None:
                    for room in self.rooms[cur_room_type]:
                        if room.id in already_reserved:
                            reserved = False
                            continue
                        reserved, id_ = room.try_reserve(reserve_application.first_day, reserve_application.last_day)
                        if reserved:
                            already_reserved[id_] =(room_type, cur_room_type,
                                                    reserve_application.first_day, reserve_application.last_day)
                            break
                    if not reserved:
                        cur_room_type = get_next(cur_room_type)
                    else:
                        break
                if not reserved:
                    reserved_all = False
                    cannot_reserve = room_type
                    break
            if not reserved_all:
                break
        
        message = ""
        if not reserved_all:
            message = "Нет достаточного кол-ва свободных номеров типа = " + cannot_reserve.name
            self.reserve_application_not_accepted += 1
        else:
            self.reserve_application_accepted += 1
            for id_, (real_type, type_, first, last) in already_reserved.items():
                for room in self.rooms[type_]:
                    if room.id == id_:
                        room.reserve(first, last, real_type)
                        message += "Забронирована комната " + str(id_) +". Ее тип - " + type_.name
                        if real_type != type_:
                            self.greater_type_count += 1
                            message += "(Cдается как - " + real_type.name + ")"
                        message +=  ". Период бронирования (" + str(first) + "," 
                        message +=  str(last) + ")\n"
            
        print(message)        
        return message                
                        

    
    def accept_settle_application(self, settle_application):
        print("==================================================")
        print("Получена заявка на заселение!!!!!")
        for room_type in RoomType:
            print(room_type, ':', settle_application.configuration[room_type])
        print("текущий день:", settle_application.current_day)
        print("количество дней:", settle_application.day_count)
        print("==================================================")
        
        settled_all = True
        already_settled = dict()
        for room_type in RoomType:
            for i in range(settle_application.configuration[room_type]):
                cur_room_type = room_type
                while cur_room_type != None:
                    for room in self.rooms[cur_room_type]:    
                        if room.id in already_settled:
                            settled = False
                            continue
                        settled, id_ = room.try_settle(settle_application.current_day, settle_application.day_count)
                        if settled:
                            already_settled[id_] = (room_type, cur_room_type,
                                                    settle_application.current_day, settle_application.day_count)
                            break
                    if not settled:
                        cur_room_type = get_next(cur_room_type)
                    else:
                        break
                if not settled:
                    settled_all = False
                    cannot_settle = room_type
                    break
            if not settled_all:
                break
        
        message = ""
        if not settled_all:
            message = "Нет достаточного кол-ва свободных номеров типа = " + cannot_settle.name
            self.settle_application_not_accepted += 1
        else:
            self.settle_application_accepted += 1
            for id_, (real_type, type_, current_day, day_count) in already_settled.items():
                for room in self.rooms[type_]:
                    if room.id == id_:
                        room.settle(current_day, day_count, real_type)
                        message += "Заселение в комнату " + str(id_) +". Ее тип - " + type_.name
                        if real_type != type_:
                            self.greater_type_count += 1
                            message += "(Cдается как " + real_type.name + ")"
                        message +=  ". Период (" + str(current_day) + "," 
                        message +=  str(current_day + day_count) + ")\n"
            
        print(message)        
        return message                
        
        
    
    def leaving(self, curr_day):
        print("выселение!!!")
        msg = ""
        for room_type in RoomType:
            for room in self.rooms[room_type]:
                for (day_st, day_fn, real_type) in room.reserved:
                    if day_fn == curr_day:
                        room.free = True
                        room.reserved.remove((day_st, day_fn, real_type))
                        cost = (day_fn - day_st) * self.prices[real_type]
                        self.profit += cost
                        msg += "Leaving from " + str(room.id) +". Period =(" + str(day_st) + " ," + str(day_fn) + "). "
                        msg += "One day price = " + str(self.prices[real_type])
                        msg +=  ". Cost = " + str(cost) + "\n"
                        break
        return msg


    
    def settling(self, curr_day):
        print("Заселение!!")
        for room_type in RoomType:
            for room in self.rooms[room_type]:
                for (day_st, day_fn, real_type) in room.reserved:
                    if day_st == curr_day:
                        room.free = False
                        break
        return
    

    def count_stats(self):
        count_free = 0
        count_not_free = 0
        for room_type in RoomType:
            for room in self.rooms[room_type]:
                if room.free:
                    count_free += 1
                else:
                    count_not_free += 1 
        stats = dict()
        stats["busy"] = count_not_free / (count_not_free + count_free)
        stats["profit"] = self.profit
        
        stats["accepted_reserve"] = self.reserve_application_accepted
        stats["accepted_settle"] = self.settle_application_accepted
        stats["not_accepted_reserve"] = self.reserve_application_not_accepted
        stats["not_accepted_settle"] = self.settle_application_not_accepted
        stats["greater_type"] = self.greater_type_count
        
        if (self.reserve_application_accepted + self.reserve_application_not_accepted) > 0 :
            stats["reserve_ok"] = self.reserve_application_accepted / (self.reserve_application_accepted + 
                                                                   self.reserve_application_not_accepted)
        else:
            stats["reserve_ok"] = 0
        if (self.settle_application_accepted + self.settle_application_not_accepted) > 0 :    
            stats["settle_ok"] = self.settle_application_accepted / (self.settle_application_accepted + 
                                                                   self.settle_application_not_accepted)
        else:
            stats["settle_ok"] = 0
        return stats