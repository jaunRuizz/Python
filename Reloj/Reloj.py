# Creating a Digital Clock using Python + Tkinter
# Youtube URL: https://youtu.be/3RuCv_puwVI

import time
import tkinter as tk
import datetime
from datetime import date

class Digital_clock():
    def __init__(self):
        self.mywindow = tk.Tk()
        self.mywindow.geometry("350x250")
        self.mywindow.resizable(0,0)
        self.mywindow.title("Creating a Digital Clock | Python + Tkinter")
        self.mywindow.config(background='#1f2f3f')
        self.current_time_label = tk.Label(text="", font=('Tahoma', 44), fg='#ffffff', bg='#72a922', pady=10, padx=10)
        self.week_day_label = tk.Label(text="", font=('Tahoma', 12), fg='#ffffff', bg='#449a66', pady=10, padx=10)
        self.created_by_label = tk.Label(text="Dany LSTI", font=('Tahoma', 9), fg='#ffffff', bg='#ff3333', pady=3, padx=3)
        self.current_time_label.place(x=50, y=50)
        self.week_day_label.place(x=75, y=150)
        self.created_by_label.place(x=140, y=200)
        self.update_clock()
        self.get_date()
        self.mywindow.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=now)
        self.mywindow.after(1000, self.update_clock)

    def get_date(self):
        # Get Week Day
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime("%A")

        # Get Current date
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        self.week_day_label.configure(text = d1 + ' | ' + week_day)


main=Digital_clock()