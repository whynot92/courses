from tkinter import *

window = Tk()

def change_lb2():
    text_user = enr1.get()
    lb2["text"] = f"Мене звати {text_user}"

lb1 = Label(text="Введіть Ваше ім'я")
lb1.place(x=50, y=20)

enr1 = Entry()
enr1.place(x=40, y=40)

but = Button(text="Клац", command=change_lb2)
but.place(x=80, y=70)

lb2 = Label(text="test")
lb2.place(x=85, y=120)

window.mainloop()