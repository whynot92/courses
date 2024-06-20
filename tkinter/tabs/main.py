from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('250x250')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Python')
tab_control.add(tab2, text='Java')

tab_control.pack(expand=1, fill='both')

window.mainloop()