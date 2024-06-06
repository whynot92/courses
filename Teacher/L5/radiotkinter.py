from tkinter import *

window = Tk()
window.title("Hello World")
window.geometry("500x500")

def change_text():
    print(var.get())

var = StringVar()
var.set("один")

radio1 = Radiobutton(text="кнопка 1", variable=var, value="один", command=change_text)
radio1.pack()

radio2 = Radiobutton(text="кнопка 2", variable=var, value="два", command=change_text)
radio2.pack()


window.mainloop()