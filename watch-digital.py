from tkinter import *
import time
from datetime import datetime
import pytz
window = Tk()
window.title('Digital Clock')
window.geometry('530x400')


def mtTime():
    h = time.strftime('%H')
    m = time.strftime('%M')
    s = time.strftime("%S")
    saat = 'TR = ' + h+':'+m+':'+s
    myLable.config(text=saat)
    myLable.after(1000, mtTime)


def laTime():
    la_timezone = pytz.timezone('America/Los_Angeles')
    la_time = datetime.now(la_timezone).strftime('%H:%M:%S')
    myLabel_la.config(text="LA = " + la_time)
    myLabel_la.after(1000, laTime)


myLable = Label(window, font=(
    'Arial', 72), fg='white', bg='blue', anchor='center')
myLable.pack(expand=True)

myLabel_la = Label(window, font=('Arial', 72), fg='white',
                   bg='green', anchor='center')
myLabel_la.pack(expand=True)
mtTime()
laTime()

window.mainloop()
