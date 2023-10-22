##import calendar
##   
##yy = 2017
##mm = 11
##   
### display the calendar
##print(calendar.month(yy, mm))

import tkinter as tk
from tkcalendar import DateEntry
from datetime import date
my_w=tk.Tk()
my_w.geometry("380x220")


cal=DateEntry(my_w,selectmode='day')
cal.grid(row=1,column=1,padx=15)
dt=date(year=2022,month=10,day=1)
cal.set_date(dt)
my_w.mainloop()
##x=datetime.datetime.now()
##print(x)
