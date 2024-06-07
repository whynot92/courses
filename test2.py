from tkinter import *

window = Tk()


def change_color():
    color = var.get()

    if color == 'синій':
        lb1['bg'] = 'blue'
    else:
        lb1['bg'] = 'yellow'


var = StringVar()
var.set("синій")


rad1 = Radiobutton(text="Синій", variable=var, value="синій", command=change_color)
rad1.pack()
rad2 = Radiobutton(text='Жовтий', variable=var, value='жовтий', command=change_color)
rad2.pack()

lb1 = Label(text='тут', bg='blue')
lb1.pack()
window.mainloop()