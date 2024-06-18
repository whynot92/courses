from tkinter import *

window = Tk()

window.title("Hello World")

window.geometry("500x500")

lb1 = Label(window, text="hello world", bg="gray", width=100, height=50)
lb1.place(x=0, y=0)

btn1 = Button(window, text="Нажми")
btn1.place(x=100, y=100)



window.mainloop()