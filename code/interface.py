from experiment import *

from tkinter import *
from tkinter.ttk import Combobox, Treeview, Style

class Interface:
    
    def __init__(self):
        self.error_label = None
        self.window = Tk()
        self.window.geometry('1000x750')
        self.window.title("Система бронирования гостиницы")
        
        
        lbl_title = Label(self.window, text="Введение параметров моделирования", font=("Arial Bold", 20))
        lbl_title.place(x = 500, y = 0)
        
        #кнопка выхода
        btn_exit = Button(self.window, text="Выход", bg="yellow", fg="red", command=lambda : self.exit())
        btn_exit.place(x = 400, y = 680)
        
        #
        btn_start = Button(self.window, text="Начать моделирование", bg="yellow", fg="red", command=lambda :self.start_modeling())
        btn_start.place(x = 900, y = 680)
        
        lbl0 = Label(self.window, text="Количество дней моделирования", font=("Arial Bold", 12))
        lbl0.place(x = 300, y = 50)
        self.textVar = StringVar(self.window)
        self.textVar.set('20')
        combo = Combobox(self.window,  textvariable=self.textVar)  
        combo['values'] = [i for i in range(12, 31)] 
        combo.place(x = 700, y = 50) 
        
        
        
        lbl1 = Label(self.window, text="Количество одноместных номеров", font=("Arial Bold", 12))
        lbl1.place(x = 300, y = 150)
        self.textVar1 = StringVar(self.window)
        self.textVar1.set('6')
        combo1 = Combobox(self.window,  textvariable=self.textVar1)   
        combo1['values'] = [i for i in range(0, 10)] 
        combo1.place(x = 700, y = 150) 
        
        
        lbl2 = Label(self.window, text="Количество двуместных номеров", font=("Arial Bold", 12))
        lbl2.place(x = 300, y = 180)
        self.textVar2 = StringVar(self.window)
        self.textVar2.set('5')
        combo2 = Combobox(self.window,  textvariable=self.textVar2) 
        combo2['values'] = [i for i in range(0, 10)]  
        combo2.place(x = 700, y = 180)  
        
        
        lbl3 = Label(self.window, text="Количество двуместных номеров с раскладным диваном", font=("Arial Bold", 11))
        lbl3.place(x = 300, y = 210)
        self.textVar3 = StringVar(self.window)
        self.textVar3.set('4')
        combo3 = Combobox(self.window,  textvariable=self.textVar3)
        combo3['values'] = [i for i in range(0, 10)]   
        combo3.place(x = 700, y = 210)  
        
        
        lbl4 = Label(self.window, text="Количество полулюкс номеров", font=("Arial Bold", 12))
        lbl4.place(x = 300, y = 240)
        self.textVar4 = StringVar(self.window)
        self.textVar4.set('3')
        combo4 = Combobox(self.window,  textvariable=self.textVar4)  
        combo4['values'] = [i for i in range(0, 10)] 
        combo4.place(x = 700, y = 240) 
        
        lbl5 = Label(self.window, text="Количество люкс номеров", font=("Arial Bold", 12))
        lbl5.place(x = 300, y = 270)
        self.textVar5 = StringVar(self.window)
        self.textVar5.set('2')
        combo5 = Combobox(self.window,  textvariable=self.textVar5)
        combo5['values'] = [i for i in range(0, 10)] 
        combo5.place(x = 700, y = 270) 
        
        
        
        lbl1p = Label(self.window, text="Цена одноместных номеров", font=("Arial Bold", 12))
        lbl1p.place(x = 300, y = 370)
        self.textVar1p = StringVar(self.window)
        self.textVar1p.set('100')
        txt1 = Entry(self.window, width=25, textvariable = self.textVar1p)
        txt1.place(x = 700, y = 370) 
        
        
        lbl2p = Label(self.window, text="Цена двуместных номеров", font=("Arial Bold", 12))
        lbl2p.place(x = 300, y = 400)
        self.textVar2p = StringVar(self.window)
        self.textVar2p.set('200')
        txt2 = Entry(self.window, width=25, textvariable = self.textVar2p)
        txt2.place(x = 700, y = 400)  
        
        
        lbl3p = Label(self.window, text="Цена двуместных номеров с раскладным диваном", font=("Arial Bold", 11))
        lbl3p.place(x = 300, y = 430)
        self.textVar3p = StringVar(self.window)
        self.textVar3p.set('250')
        txt3 = Entry(self.window, width=25, textvariable = self.textVar3p)
        txt3.place(x = 700, y = 430) 
        
        
        lbl4p = Label(self.window, text="Цена полулюкс номеров", font=("Arial Bold", 12))
        lbl4p.place(x = 300, y = 460)
        self.textVar4p = StringVar(self.window)
        self.textVar4p.set('400')
        txt4 = Entry(self.window, width=25, textvariable = self.textVar4p)
        txt4.place(x = 700, y = 460)  
        
        lbl5p = Label(self.window, text="Цена люкс номеров", font=("Arial Bold", 12))
        lbl5p.place(x = 300, y = 490)
        self.textVar5p = StringVar(self.window)
        self.textVar5p.set('500')
        txt5 = Entry(self.window, width=25, textvariable = self.textVar5p)
        txt5.place(x = 700, y = 490) 
        
        
        lbl1u = Label(self.window, text="Минимальное время между заявками", font=("Arial Bold", 12))
        lbl1u.place(x = 300, y = 600)
        self.textVar1u = StringVar(self.window)
        self.textVar1u.set('2')
        combo1u = Combobox(self.window,  textvariable=self.textVar1u)  
        combo1u['values'] = [i for i in range(1, 10)] 
        combo1u.place(x = 700, y = 600) 
        
        lbl2u = Label(self.window, text="Максимальное время между заявками", font=("Arial Bold", 12))
        lbl2u.place(x = 300, y = 630)
        self.textVar2u = StringVar(self.window)
        self.textVar2u.set('5')
        combo2u = Combobox(self.window,  textvariable=self.textVar2u)  
        combo2u['values'] = [i for i in range(2, 20)] 
        combo2u.place(x = 700, y = 630) 
        
        self.window.mainloop()
        return
        
        
    def exit(self):
        self.window.destroy()
        
        
    def start_modeling(self):
        
        if self.error_label is not None:
            self.error_label.destroy()
        
        try:
            M = int(self.textVar.get())
            
            k_1 = int(self.textVar1.get())
            k_2 = int(self.textVar2.get())
            k2_sofa = int(self.textVar3.get())
            k_half_luxury = int(self.textVar4.get())
            k_luxury = int(self.textVar5.get())
            
            price_1 = int(self.textVar1p.get())
            price_2 = int(self.textVar2p.get())
            price_2_sofa = int(self.textVar3p.get())
            price_half_luxury = int(self.textVar4p.get())
            price_luxury = int(self.textVar5p.get())
            
            min_gen = int(self.textVar1u.get())
            max_gen = int(self.textVar2u.get())
            
        except:
            self.error_label = Label(self.window, text="Все данные должны быть числовыми!", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if min_gen > max_gen:
            self.error_label = Label(self.window, text="Минимальное время должно быть не меньше максимального", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_1 >= price_2:
            self.error_label = Label(self.window, text="Цена одноместного номера должна быть меньше цены двуместного", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_1 >= price_2_sofa:
            self.error_label = Label(self.window, text="Цена одноместного номера должна быть меньше цены двуместного с диваном", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_1 >= price_half_luxury:
            self.error_label = Label(self.window, text="Цена одноместного номера должна быть меньше цены полулюкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_1 >= price_luxury:
            self.error_label = Label(self.window, text="Цена одноместного номера должна быть меньше цены люкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.grid(column=0, row=0)
            return
        
        if price_2 >= price_2_sofa:
            self.error_label = Label(self.window, text="Цена двуместного номера должна быть меньше цены двуместного с диваном", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return 
        
        if price_2 >= price_half_luxury:
            self.error_label = Label(self.window, text="Цена двуместного номера должна быть меньше цены полулюкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_2 >= price_luxury:
            self.error_label = Label(self.window, text="Цена двуместного номера должна быть меньше цены люкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_2_sofa >= price_half_luxury:
            self.error_label = Label(self.window, text="Цена двуместного номера с диваном должна быть меньше цены полулюкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_2_sofa >= price_luxury:
            self.error_label = Label(self.window, text="Цена двуместного номера с диваном должна быть меньше цены люкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        if price_half_luxury >= price_luxury:
            self.error_label = Label(self.window, text="Цена полулюкса должна быть меньше цены люкса", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
            
        
        if M < 12 or M > 30:
            self.error_label = Label(self.window, text="Число дней должно быть от 12 до 30!", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        if (k_1 < 0 or k_1 > 9 or
            k_2 < 0 or k_2 > 9 or
            k2_sofa < 0 or k2_sofa > 9 or
            k_half_luxury < 0 or k_half_luxury > 9 or
            k_luxury < 0 or k_luxury > 9):
            self.error_label = Label(self.window, text="Число номеров должно быть от 0 до 9!", font=("Arial Bold", 25), fg = "red")
            self.error_label.place(x = 100, y = 720)
            return
        
        self.window.destroy()
        
        self.window = Tk()
        self.window.geometry('1000x750')
        self.window.title("Система бронирования гостиницы")
        self.lbl_day_val = None
        self.lbl_time_val = None
        self.settle_ok_val = None
        self.lbl_profit_val = None
        self.lbl_busy_val = None
        self.reserve_ok_val = None
        self.gr = None
        self.count_gr = None
        self.count_settle_not_ok_val = None
        self.count_reserve_not_ok_val = None
        self.count_settle_ok_val = None
        self.count_reserve_ok_val = None
        
        lbl = Label(self.window, text="Моделирование", font=("Arial Bold", 30), fg = "red")
        lbl.place(x=500, y=0)
        
        configuration = dict()
        configuration[RoomType.one] = k_1
        configuration[RoomType.two] = k_2
        configuration[RoomType.tho_with_sofa] = k2_sofa
        configuration[RoomType.half_luxury] = k_half_luxury
        configuration[RoomType.luxury] = k_luxury
           
        prices = dict()    
        prices[RoomType.one] = price_1
        prices[RoomType.two] = price_2
        prices[RoomType.tho_with_sofa] = price_2_sofa
        prices[RoomType.half_luxury] = price_half_luxury
        prices[RoomType.luxury] = price_luxury
        
        generation_conf = dict()
        generation_conf["min_time"] = min_gen
        generation_conf["max_time"] = max_gen
        
        self.exp = Experiment(M, configuration, prices, generation_conf)
        
        #кнопка выхода
        btn_exit = Button(self.window, text="Выход", bg="yellow", fg="red", command=lambda : self.exit())
        btn_exit.place(x=800, y = 680)
        #шаш моделирование
        btn_step = Button(self.window, text="Шаг моделирование", bg="yellow", fg="red", command=lambda: self.step())
        btn_step.place(x=1000, y=680)
        
        #до конца
        btn_all_steps = Button(self.window, text="До конца", bg="yellow", fg="red", command=lambda: self.all_steps())
        btn_all_steps.place(x=1200, y=680)
               
        self.window.mainloop()
    
    def step(self):
        if self.exp.step() == 0:
            if self.lbl_day_val is not None:
                self.lbl_day_val.destroy()
            if self.lbl_time_val is not None:
                self.lbl_time_val.destroy()
        
            lbl_day = Label(self.window, text="День", font=("Arial Bold", 25))
            lbl_day.place(x=1100, y=10)
            day = str(self.exp.day)
            self.lbl_day_val = Label(self.window, text=day, font=("Arial Bold", 25))
            self.lbl_day_val.place(x=1300, y=10)
            
            
            lbl_time = Label(self.window, text="Время", font=("Arial Bold", 25))
            lbl_time.place(x=1100, y=50)
            time = str(self.exp.time)
            self.lbl_time_val = Label(self.window, text=time, font=("Arial Bold", 25))
            self.lbl_time_val.place(x=1300, y=50)
                       
            self.print_stats()          
                                   
            i = 0
            rows = []
            cols = ["id", "type", "price", "reserved"]
            
            for room_type in RoomType:
                for room in self.exp.hotel.rooms[room_type]:
                    data = [str(room.id), room_type.name, self.exp.hotel.prices[room_type]]
                    if room.reserved:
                        day_st = room.reserved[0][0]
                        real_type = room.reserved[0][2]
                        if day_st <= int(day):
                            if real_type != room_type:
                                data[2] = self.exp.hotel.prices[real_type]
                                
                    
                    reserved = []
                    for (day_st, day_fn, real_type) in room.reserved:
                        string = "(" + str(day_st) + ", " + str(day_fn) + ")," + str(real_type.name) + ""
                        reserved.append(string)
                    data.append(reserved)
                    rows.append(data)
                        
                    i = i + 1
            
            
            lbl_rooms = Label(self.window, text="Занятость номеров гостиницы", font=("Arial Bold", 20))
            lbl_rooms.place(x=300, y=50)
            
            frame = Frame()
            frame.place(x = 0, y = 100)
            
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
            table.column("reserved", width=875)
            
            table.pack(expand=NO, fill=BOTH)
            

            lbl_appls = Label(self.window, text="Поступившие заявки", font=("Arial Bold", 20))
            lbl_appls.place(x=300, y=330)
            
            frame1 = Frame()
            frame1.place(x = 0, y = 370)
            
            Style().configure('MyStyle1.Treeview', rowheight=45) 
            table1 = Treeview(frame1, show = 'headings', height = 5, style = 'MyStyle1.Treeview')
            cols = ["Период", "Типы_комнат", "Тип_заявки", "Сообщение"]
            table1["columns"] = cols
            
            rows = []
            for (type_, application, msg) in self.exp.applications:
                if type_ == "settle":
                    period = (self.exp.day, self.exp.day + application.day_count)
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
            table1.column("Типы_комнат", width=375)
            table1.column("Тип_заявки", width=100)
            table1.column("Сообщение", width=500)
            table1.pack(expand=YES, fill=BOTH)

            lbl_leave = Label(self.window, text="Выселение", font=("Arial Bold", 20))
            lbl_leave.place(x=100, y=630)
            
            frame2 = Frame()
            frame2.place(x = 0, y = 680)
            table2 = Treeview(frame2, show = 'headings', height = 3)
            cols = ["Выселение"]
            table2["columns"] = cols
            rows = list(map(lambda x: [x], self.exp.leaving.split("\n")))
            
            for row in rows:
                table2.insert('', 'end', values = row)
             
            for col in cols:
                table2.heading(col, text=col, anchor='center')
            table2.column("Выселение", width=700)    
            table2.pack(expand=YES, fill=BOTH)
            return 0
        else:
            self.final_stats()
            return
        
    
    def all_steps(self):
        while self.exp.step() == 0:
            continue
        self.final_stats()
        return
    
    
    def final_stats(self):
        self.window.destroy()
        self.window = Tk()
        self.window.geometry('1000x750')
        self.window.title("Итоговая статистика")
        lbl = Label(self.window, text="Итоговая статистика", font=("Arial Bold", 30), fg = "red")
        lbl.place(x=500, y=0)
        self.print_stats()
        btn_exit = Button(self.window, text="Выход", bg="yellow", fg="red", command=lambda : self.exit())
        btn_exit.place(x=800, y = 680)
        return
        
        
    def print_stats(self):
        lbl_profit = Label(self.window, text="Прибыль", font=("Arial Bold", 20))
        lbl_profit.place(x=1100, y=180)
        profit = str(self.exp.hotel.profit)
        self.lbl_profit_val = Label(self.window, text=profit, font=("Arial Bold", 20))
        self.lbl_profit_val.place(x=1420, y=180)
        
        stats = self.exp.hotel.count_stats()            
        lbl_busy = Label(self.window, text="Загруженность", font=("Arial Bold", 20))
        lbl_busy.place(x=1100, y=220)
        busy = str( stats["busy"] )
        if len(busy ) > 3:
            busy = busy[:4]
        self.lbl_busy_val = Label(self.window, text=busy, font=("Arial Bold", 20))
        self.lbl_busy_val.place(x=1420, y=220)
        
        lbl_reserve_ok = Label(self.window, text="Доля принятых заявок на бронь", font=("Arial Bold", 15))
        lbl_reserve_ok.place(x=1100, y=260)
        reserve_ok = str( stats["reserve_ok"] )
        if len(reserve_ok ) > 3:
            reserve_ok = reserve_ok[:4]
        self.reserve_ok_val = Label(self.window, text=reserve_ok, font=("Arial Bold", 15))
        self.reserve_ok_val.place(x=1420, y=260)
        
        lbl_settle_okk = Label(self.window, text="Доля принятых заявок на заселение", font=("Arial Bold", 13))
        lbl_settle_okk.place(x=1100, y=300)
        settle_ok = str( stats["settle_ok"] )
        if len(settle_ok ) > 3:
            settle_ok = settle_ok[:4]
        self.settle_ok_val = Label(self.window, text=settle_ok, font=("Arial Bold", 15))
        self.settle_ok_val.place(x=1420, y=300)
        
        
        lbl_count_reserve_ok = Label(self.window, text="Число принятых заявок на бронь", font=("Arial Bold", 15))
        lbl_count_reserve_ok.place(x=1100, y=340)
        reserve_ok = str( stats["accepted_reserve"] )
        self.count_reserve_ok_val = Label(self.window, text=reserve_ok, font=("Arial Bold", 15))
        self.count_reserve_ok_val.place(x=1420, y=340)
        
        lbl_count_settle_okk = Label(self.window, text="Число принятых заявок на заселение", font=("Arial Bold", 13))
        lbl_count_settle_okk.place(x=1100, y=380)
        settle_ok = str( stats["accepted_settle"] )
        self.count_settle_ok_val = Label(self.window, text=settle_ok, font=("Arial Bold", 15))
        self.count_settle_ok_val.place(x=1420, y=380)
        
        lbl_count_reserve_not_ok = Label(self.window, text="Число непринятых заявок на бронь", font=("Arial Bold", 13))
        lbl_count_reserve_not_ok.place(x=1100, y=420)
        reserve_ok = str( stats["not_accepted_reserve"] )
        self.count_reserve_not_ok_val = Label(self.window, text=reserve_ok, font=("Arial Bold", 15))
        self.count_reserve_not_ok_val.place(x=1420, y=420)
        
        lbl_count_settle_not_ok = Label(self.window, text="Число непринятых заявок на заселение", font=("Arial Bold", 13))
        lbl_count_settle_not_ok.place(x=1100, y=460)
        settle_ok = str( stats["not_accepted_settle"] )
        self.count_settle_not_ok_val = Label(self.window, text=settle_ok, font=("Arial Bold", 15))
        self.count_settle_not_ok_val.place(x=1420, y=460)
        
        lbl_count_gr = Label(self.window, text="Число номеров сдаваемых по меньше цене", font=("Arial Bold", 11))
        lbl_count_gr.place(x=1100, y=500)
        gr = str( stats["greater_type"] )
        self.count_gr = Label(self.window, text=gr, font=("Arial Bold", 15))
        self.count_gr.place(x=1420, y=500)
        
        lbl_gr = Label(self.window, text="Доля номеров сдаваемых по меньше цене", font=("Arial Bold", 11))
        lbl_gr.place(x=1100, y=540)
        if stats["accepted_reserve"] + stats["accepted_settle"] > 0 :
            gr = str( stats["greater_type"] / (stats["accepted_reserve"] + stats["accepted_settle"]))
        else:
            gr = str(0)
        if len(gr ) > 3:
            gr = gr[:4]
        self.gr = Label(self.window, text=gr, font=("Arial Bold", 15))
        self.gr.place(x=1420, y=540)
        return
        

print("start")
Interface()
print("end")