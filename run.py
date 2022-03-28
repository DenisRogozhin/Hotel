#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from enum import Enum, IntEnum
import random


# # 1. Перечислимый тип данных - тип комнаты и функция для получения комнаты со следующим приоритетом

# In[2]:


class RoomType(IntEnum):
    luxury = 5
    half_luxury = 4
    tho_with_sofa = 3
    two = 2
    one = 1
    
def get_next(our_room_type):
    for room_type in RoomType:
        if room_type - our_room_type == 1:
            return room_type
    return None


    


# # 2. Комната

# In[3]:


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


# # 3. Отель

# In[4]:


for room_type in RoomType:
    print(room_type)


# In[5]:


class Hotel():
    
    def __init__(self, configuration):
        self.profit = 0
        
        self.rooms = dict()
        room_id = 500
        for room_type in RoomType:
            self.rooms[room_type] = [Room(room_id + i) for i in range(configuration[room_type])]
            room_id = room_id - 100
        
        self.prices = dict()
        self.prices[RoomType.one] = 100
        self.prices[RoomType.two] = 200
        self.prices[RoomType.tho_with_sofa] = 250
        self.prices[RoomType.half_luxury] = 400
        self.prices[RoomType.luxury] = 500
        
        self.reserve_application_accepted = 0
        self.reserve_application_not_accepted = 0
        
        self.settle_application_accepted = 0
        self.settle_application_not_accepted = 0
   
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
                            message += "(Забронирована в качестве типа - " + real_type.name + ")"
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
                            message += "(При этом она сдается в качестве комнаты типа " + real_type.name + ")"
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
                        msg += "Leaving from" + str(room.id) +". Period =(" + str(day_st) + "," + str(day_fn) + ")"
                        msg += "One day price = " + str(self.prices[real_type])
                        msg +=  "Cost = " + str(cost) + "\n"
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
        
        


# # 4. Заявки на бронирование и заселение

# In[6]:


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


# # 5. Эксперимент

# In[7]:


class Experiment():
    
    def __init__(self, M, k_1, k_2, k2_sofa, k_half_luxury, k_luxury):
        self.days = M
        self.leaving = ""
        
        self.configuration = dict()
        self.configuration[RoomType.one] = k_1
        self.configuration[RoomType.two] = k_2
        self.configuration[RoomType.tho_with_sofa] = k2_sofa
        self.configuration[RoomType.half_luxury] = k_half_luxury
        self.configuration[RoomType.luxury] = k_luxury
        
        self.hotel = Hotel(self.configuration)
        
        self.time = 0
        self.day = 0
        self.model_step = 2 #шаг моделирования 2 часа
        
        #время генерации заявки - с.в. из U([1,5])
        self.interval_of_generation_reserve = int(np.random.uniform(1,5))
        self.interval_of_generation_settle = int(np.random.uniform(1,5))
        
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
            self.interval_of_generation_reserve = int(np.random.uniform(1,5))
            print("update interval_of_generation_reserve:", self.interval_of_generation_reserve)
        if self.interval_of_generation_reserve > time_left:
            self.interval_of_generation_reserve -= time_left

            
        time_left = self.model_step
        while self.interval_of_generation_settle <= time_left:
            self.generate_settle_application()
            time_left = time_left - self.interval_of_generation_settle
            self.interval_of_generation_settle = int(np.random.uniform(1,5))
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


# # 6. Пример

# In[8]:


#exp = Experiment(30, 5, 5, 5, 5, 5)
exp = Experiment(30, 2, 2, 2, 2, 2)


# In[9]:


exp.step()


# In[10]:


exp.step()


# In[11]:


exp.step()


# In[12]:


exp.step()


# In[13]:


exp.step()


# In[14]:


exp.step()


# In[15]:


exp.step()


# In[16]:


while exp.step() == 0:
    continue


# # 7. Интерфейс

# In[17]:


from tkinter import *
from tkinter.ttk import Combobox, Treeview, Style



def exit(window):
    window.destroy()
    
def exit1(window1):
    window1.destroy()    

def step(exp, window1):
    if exp.step() == 0:
        
        lbl_day = Label(window1, text="День", font=("Arial Bold", 10))
        lbl_day.grid(column=3, row=10)
        day = str(exp.day)
        lbl_day_val = Label(window1, text=day, font=("Arial Bold", 10))
        lbl_day_val.grid(column=6, row=10)
        
        
        lbl_time = Label(window1, text="Время", font=("Arial Bold", 10))
        lbl_time.grid(column=3, row=20)
        time = str(exp.time)
        lbl_time_val = Label(window1, text=time, font=("Arial Bold", 10))
        lbl_time_val.grid(column=6, row=20)
        
        ###
        lbl_profit = Label(window1, text="Прибыль", font=("Arial Bold", 10))
        lbl_profit.grid(column=3, row=30)
        profit = str(exp.hotel.profit)
        lbl_profit_val = Label(window1, text=profit, font=("Arial Bold", 10))
        lbl_profit_val.grid(column=6, row=30)
        
        stats = exp.hotel.count_stats()
        
        #stats["reserve_ok"] 
        #stats["settle_ok"]
        
        lbl_busy = Label(window1, text="Загруженность", font=("Arial Bold", 10))
        lbl_busy.grid(column=3, row=40)
        busy = str( stats["busy"] )
        if len(busy ) > 3:
            busy = busy[:4]
        lbl_busy_val = Label(window1, text=busy, font=("Arial Bold", 10))
        lbl_busy_val.grid(column=6, row=40)
        
        lbl_reserve_ok = Label(window1, text="Доля пр.заявок на бронь", font=("Arial Bold", 8))
        lbl_reserve_ok.grid(column=3, row=50)
        reserve_ok = str( stats["reserve_ok"] )
        if len(reserve_ok ) > 3:
            reserve_ok = reserve_ok[:4]
        reserve_ok_val = Label(window1, text=reserve_ok, font=("Arial Bold", 10))
        reserve_ok_val.grid(column=6, row=50)
        
        lbl_settle_okk = Label(window1, text="Доля пр.заявок на заселение", font=("Arial Bold", 8))
        lbl_settle_okk.grid(column=3, row=60)
        settle_ok = str( stats["settle_ok"] )
        if len(settle_ok ) > 3:
            settle_ok = settle_ok[:4]
        settle_ok_val = Label(window1, text=settle_ok, font=("Arial Bold", 10))
        settle_ok_val.grid(column=6, row=60)
        ###
        
        i = 0
        rows = []
        cols = ["id", "type", "price", "reserved"]
        
        for room_type in RoomType:
            for room in exp.hotel.rooms[room_type]:
                data = [str(room.id), room_type.name, exp.hotel.prices[room_type]]
                if room.reserved:
                    day_st = room.reserved[0][0]
                    real_type = room.reserved[0][2]
                    if day_st <= int(day):
                        if real_type != room_type:
                            data[2] = exp.hotel.prices[real_type]
                            
                
                reserved = []
                for (day_st, day_fn, real_type) in room.reserved:
                    string = "(" + str(day_st) + ", " + str(day_fn) + ")," + str(real_type.name) + ""
                    reserved.append(string)
                data.append(reserved)
                rows.append(data)
                    
                #lbl = Label(window1, text=(str(room.id)+"   type = " + room_type.name +
                #                           str(room.reserved)), font=("Arial Bold", 10))
                #lbl.grid(column=0, row=30 + i)
                i = i + 1
        
        frame = Frame()
        frame.grid(row = 5, column = 0)
        
        table = Treeview(frame, show = 'headings')
        table["columns"] = cols
        for row in rows:
            table.insert('', 'end', values = row)
         
        for col in cols:
            table.heading(col, text=col, anchor='center')
         
        
        scroll = Scrollbar(frame, command = table.yview)
        table.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill = Y)
        
                
        table.column("id", width=50)
        table.column("type", width=100)
        table.column("price", width=50)
        table.column("reserved", width=800)
        
        table.pack(expand=NO, fill=BOTH)
        
        #..............................
        
        frame1 = Frame()
        frame1.grid(row = 500, column = 0)
        

        Style().configure('MyStyle1.Treeview', rowheight=45) 
        table1 = Treeview(frame1, show = 'headings', height = 5, style = 'MyStyle1.Treeview')
        cols = ["Период", "Типы_комнат", "Тип_заявки", "Сообщение"]
        table1["columns"] = cols
        
        rows = []
        for (type_, application, msg) in exp.applications:
            if type_ == "settle":
                period = (exp.day, exp.day + application.day_count)
            else:
                period = (application.first_day, application.last_day)
            rooms = ""
            for room_type in RoomType:
                if application.configuration[room_type] > 0:
                    rooms += room_type.name + " " + str(application.configuration[room_type]) + "|"
            line = (period, rooms, type_, msg)
            rows.append(line)
            
                        
        for row in rows:
            table1.insert('', 'end', values = row)
         
        for col in cols:
            table1.heading(col, text=col, anchor='center')
         
        
        scroll1 = Scrollbar(frame1, command = table1.yview)
        table1.configure(yscrollcommand=scroll1.set)
        scroll1.pack(side=RIGHT, fill = Y)

        table1.column("Период", width=100)
        table1.column("Типы_комнат", width=200)
        table1.column("Тип_заявки", width=100)
        table1.column("Сообщение", width=500)
        table1.pack(expand=YES, fill=BOTH)
       
    
        ## 
        frame2 = Frame()
        frame2.grid(row = 3, column = 3)
        table2 = Treeview(frame2, show = 'headings', height = 3)
        cols = ["Выселение"]
        table2["columns"] = cols
        rows = list(map(lambda x: [x], exp.leaving.split("\n")))
        
        for row in rows:
            table2.insert('', 'end', values = row)
         
        for col in cols:
            table2.heading(col, text=col, anchor='center')
        table2.column("Выселение", width=300)    
        table2.pack(expand=YES)
        return 0
    else:
        print("stop!")
        return 1
        #вывести экран со статистикой
    
    


# In[18]:


def all_steps(exc, window1):
    #тут тоже надо сделать вывод результатов
    while step(exc, window1) == 0:
        continue
    
def start_modeling(window):
    #M = int(combo.get())
    M = int(textVar.get())
    
    k_1 = int(textVar1.get())
    k_2 = int(textVar2.get())
    k2_sofa = int(textVar3.get())
    k_half_luxury = int(textVar4.get())
    k_luxury = int(textVar5.get())
    
    
    
    if M < 12 or M > 30:
        error_label = Label(window, text="Число дней должно быть от 12 до 30!", font=("Arial Bold", 15))
        error_label.grid(column=0, row=0)
        return
    if (k_1 < 0 or k_1 > 9 or
        k_2 < 0 or k_2 > 9 or
        k2_sofa < 0 or k2_sofa > 9 or
        k_half_luxury < 0 or k_half_luxury > 9 or
        k_luxury < 0 or k_luxury > 9):
        error_label = Label(window, text="Число номеров должно быть от 0 до 9!", font=("Arial Bold", 15))
        error_label.grid(column=0, row=0)
        return
    
    print("gg")
    window.destroy()
    window1 = Tk()
    window1.geometry('1800x750')
    window1.title("Система бронирования гостиницы")
    lbl = Label(window1, text="Моделирование", font=("Arial Bold", 15))
    lbl.grid(column=0, row=0)
    
    exp = Experiment(M, k_1, k_2, k2_sofa, k_half_luxury, k_luxury)
    
    #кнопка выхода
    btn_exit = Button(window1, text="Выход", bg="yellow", fg="red", command=lambda : exit1(window1))
    btn_exit.grid(column=0, row=1200)

    #начать моделирование
    btn_step = Button(window1, text="Шаг моделирование", bg="yellow", fg="red", command=lambda: step(exp, window1))
    btn_step.grid(column=3, row=1200)
    
    #начать моделирование
    #btn_all_steps = Button(window1, text="До конца", bg="yellow", fg="red", command=lambda: all_steps(exp, window1))
    #btn_all_steps.grid(column=6, row=1200)
           
    window1.mainloop()
    
    
    

window = Tk()
window.geometry('1000x750')
window.title("Система бронирования гостиницы")

lbl_title = Label(window, text="Введение параметры моделирования", font=("Arial Bold", 20))
lbl_title.grid(column=0, row=0)

#кнопка выхода
btn_exit = Button(window, text="Выход", bg="yellow", fg="red", command=lambda : exit(window))
btn_exit.grid(column=0, row=100)


btn_start = Button(window, text="Начать моделирование", bg="yellow", fg="red", command=lambda :start_modeling(window))
btn_start.grid(column=5, row=100)


lbl0 = Label(window, text="Количество дней моделирования", font=("Arial Bold", 10))
lbl0.grid(column=0, row=10)
textVar = StringVar(window)
textVar.set('20')
combo = Combobox(window,  textvariable=textVar)  
combo['values'] = [i for i in range(12, 31)] 
combo.grid(column=1, row=10)  


lbl1 = Label(window, text="Количество одноместных номеров", font=("Arial Bold", 10))
lbl1.grid(column=0, row=20)
textVar1 = StringVar(window)
textVar1.set('4')
combo1 = Combobox(window,  textvariable=textVar1)   
combo1['values'] = [i for i in range(0, 10)] 
combo1.grid(column=1, row=20) 


lbl2 = Label(window, text="Количество двуместных номеров", font=("Arial Bold", 10))
lbl2.grid(column=0, row=30)
textVar2 = StringVar(window)
textVar2.set('4')
combo2 = Combobox(window,  textvariable=textVar2) 
combo2['values'] = [i for i in range(0, 10)]  
combo2.grid(column=1, row=30)  

lbl3 = Label(window, text="Количество двуместных номеров с раскладным диваном", font=("Arial Bold", 10))
lbl3.grid(column=0, row=40)
textVar3 = StringVar(window)
textVar3.set('4')
combo3 = Combobox(window,  textvariable=textVar3)
combo3['values'] = [i for i in range(0, 10)]   
combo3.grid(column=1, row=40)  

lbl4 = Label(window, text="Количество полулюкс номеров", font=("Arial Bold", 10))
lbl4.grid(column=0, row=50)
textVar4 = StringVar(window)
textVar4.set('4')
combo4 = Combobox(window,  textvariable=textVar4)  
combo4['values'] = [i for i in range(0, 10)] 
combo4.grid(column=1, row=50) 

lbl5 = Label(window, text="Количество люкс номеров", font=("Arial Bold", 10))
lbl5.grid(column=0, row=60)
textVar5 = StringVar(window)
textVar5.set('4')
combo5 = Combobox(window,  textvariable=textVar5)
combo5['values'] = [i for i in range(0, 10)] 
combo5.grid(column=1, row=60) 

#txt = Entry(window, width=10)
#txt.grid(column=3, row=0)  



window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




