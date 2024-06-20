from tkinter import *

def print_text(event=None):
    lb['text'] = scale_user.get()


window = Tk()

lb = Label(text="")
lb.pack()

scale_user = Scale(orient=HORIZONTAL,
                   length=300,
                   from_=0,
                   to=100,
                   tickinterval=10,
                   resolution=10, command=print_text)
scale_user.pack()

scale_user.bind("<Motion>", print_text)

window.mainloop()