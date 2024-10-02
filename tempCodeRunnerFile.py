from tkinter import *
import time

window = Tk()
window.title('Digital Clock')
window.geometry('530x150')


def mtTime():
    h = time.strftime('%H')
    m = time.strftime('%M')
    s = time.strftime("%S")
    saat = 'TR = ' + h+':'+m+':'+s
    myLable.config(text=saat)
    myLable.after(1000, mtTime)


myLable = Label(window, font=(
    'Arial', 72), fg='white', bg='blue', anchor='center')
myLable.pack(expand=True)
mtTime()

window.mainloop()
