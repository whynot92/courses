import customtkinter
import tkinter

window = customtkinter.CTk()

window.title("Hello World")
window.iconbitmap("Teacher/L6/logo.png")

window.geometry("500x500")

img = tkinter.PhotoImage(file="Teacher/L6/logo.png")

lb1 = customtkinter.CTkLabel(master=window, text="hello world", image=img)

lb1.place(x=100, y=100)

btn1 = tkinter.Button(master=window, image=img)

btn1.place(x=100, y=200)

entry = customtkinter.CTkEntry(master=window)

entry.place(x=100, y=300)

window.mainloop()