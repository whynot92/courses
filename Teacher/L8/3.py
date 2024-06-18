from tkinter import *

window = Tk()

window.title("Hello World")

window.geometry("500x500")

img = PhotoImage(file="Teacher/L8/ff.png")

lb1 = Label(master=window, text="hello world", image=img)

lb1.place(x=0, y=0)

lb2 = Label(master=window, bg="white", height=100, width=100)

lb2.place(x=250, y=0)

window.mainloop()