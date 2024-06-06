from tkinter import *

window = Tk()

def change_color():
    lb1['bg'] = var.get()

var = StringVar()
var.set("синій")


rad1 = Radiobutton(text="Синій", variable=var, value="blue", command=change_color)
rad1.pack()
rad2 = Radiobutton(text='Жовтий', variable=var, value='yellow', command=change_color)
rad2.pack()

lb1 = Label(text='тут', bg='blue')
lb1.pack()
window.mainloop()