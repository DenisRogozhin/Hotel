from hotel import *
from applications import *

class Experiment():
    
    def __init__(self, M, room_conf, prices_conf, generation_conf):
        self.days = M
        self.leaving = ""
        
        self.configuration = room_conf
        self.prices = prices_conf
       
        
        self.hotel = Hotel(self.configuration, self.prices)
        
        self.time = 0
        self.day = 0
        self.model_step = 2 #шаг моделирования 2 часа
        
        self.min_time_gen = generation_conf["min_time"]
        self.max_time_gen = generation_conf["max_time"]
        
        #время генерации заявки - с.в. из U([min_time,max_time])
        self.interval_of_generation_reserve = int(np.random.uniform(self.min_time_gen,self.max_time_gen))
        self.interval_of_generation_settle = int(np.random.uniform(self.min_time_gen,self.max_time_gen))
        
        self.applications = []
               
        
    def generate_reserve_application(self):
        
        configuration = dict()
        summa = 0
        for i, room_type in enumerate(RoomType):
            count = random.choices([0, 1, 2], weights=[0.5, 0.4, 0.1])[0]
            if i < len(RoomType) - 1:
                configuration[room_type] = count
                summa += count
            else:
                if summa == 0:
                    configuration[room_type] = random.choices([1, 2], weights=[0.8, 0.2])[0] 
                else:
                    configuration[room_type] = count

            
        first_day = int(np.random.uniform(self.day + 1, self.days))
        last_day = int(np.random.uniform(first_day + 1, self.days + 1))
        
        reserve_application = Reserve_application(configuration, first_day, last_day)
        message = self.hotel.accept_reserve_application(reserve_application)
        self.applications.append(("reserve", reserve_application, message))
                    
    
    def generate_settle_application(self):
        
        configuration = dict()
        summa = 0
        for i, room_type in enumerate(RoomType):
            count = random.choices([0, 1, 2], weights=[0.5, 0.4, 0.1])[0]
            if i < len(RoomType) - 1:
                configuration[room_type] = count
                summa += count
            else:
                if summa == 0:
                    configuration[room_type] = random.choices([1, 2], weights=[0.8, 0.2])[0] 
                else:
                    configuration[room_type] = count
            
        day_count = int(np.random.uniform(1, self.days - self.day + 1))
        
        settle_application = Settle_application(configuration, self.day, day_count)
        message = self.hotel.accept_settle_application(settle_application)
        self.applications.append(("settle", settle_application, message))
    
    def step(self):
        self.applications = []
        if self.day == self.days + 1:
            print("Stop modeling")
            return 1
    
        print("STEP!")
        self.time += self.model_step
        if self.time == 24:
            self.time = 0
            self.day += 1
        
            
        print("day:", self.day)
        print("time:", self.time)
        
        print("model_step:", self.model_step)
        print("current interval_of_generation_reserve:", self.interval_of_generation_reserve)
        print("current interval_of_generation_settle:", self.interval_of_generation_settle)
        
            
        # generating applications
        time_left = self.model_step
        while self.interval_of_generation_reserve <= time_left:
            self.generate_reserve_application()
            time_left -= self.interval_of_generation_reserve
            self.interval_of_generation_reserve = int(np.random.uniform(self.min_time_gen,self.max_time_gen))
            print("update interval_of_generation_reserve:", self.interval_of_generation_reserve)
        if self.interval_of_generation_reserve > time_left:
            self.interval_of_generation_reserve -= time_left

            
        time_left = self.model_step
        while self.interval_of_generation_settle <= time_left:
            self.generate_settle_application()
            time_left = time_left - self.interval_of_generation_settle
            self.interval_of_generation_settle = int(np.random.uniform(self.min_time_gen,self.max_time_gen))
            print("update interval_of_generation_settle:", self.interval_of_generation_settle)
        if self.interval_of_generation_settle > time_left:
            self.interval_of_generation_settle -= time_left

            
        #выселение из гостиницы проводится в 10 утра каждый день

        #заселение в гостиницу проводится в 12 дня каждый день
        
        if self.time == 10:
            self.leaving = self.hotel.leaving(self.day)
            
        if self.time == 12:
            self.hotel.settling(self.day)
            
        return 0