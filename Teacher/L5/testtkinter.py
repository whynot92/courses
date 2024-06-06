from tkinter import *

window = Tk()
window.title("Hello World")
window.geometry("500x500")

def change_text():
    text = entry.get()

    lb1["text"] = text


lb1 = Label(window, text="hello world", fg="red", bg="gray", width=100)
lb1.place(x=100, y=100)

entry = Entry(window, width=100)
entry.place(x=100, y=200)

btn1 = Button(window, text="Нажми", command=change_text, fg="red", bg="gray")
btn1.place(x=100, y=300)


window.mainloop()