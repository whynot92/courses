from tkinter import *
from tkinter import messagebox

def window_info():
    if status_checkbutton.get() == 1:
        messagebox.showinfo(title="Оповищение", message='Включено')
    else:
        messagebox.showinfo(title="Оповищение", message='Выключено')

window = Tk()

status_checkbutton = IntVar()

ch1 = Checkbutton(text='Включить',command=window_info, variable=status_checkbutton)
ch1.grid()


window.mainloop()