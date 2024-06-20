from tkinter import *

def courses_today():
    today_courses = var.get()
    lb4['text'] = 39 if today_courses == 'Dollar' else 41

def converter():
    int_conventer = en1.get()
    get_courses = lb4['text']
    lb5['text'] = int(int_conventer) * int(get_courses)

window = Tk()
window.title("Currency Conventer")
window.geometry("300x160")

var = StringVar()
var.set('Dollar')

lb1 = Label(text="Choose a currency:")
lb1.grid()

rd1 = Radiobutton(text='Dollar', variable=var, value='Dollar', command=courses_today)
rd1.place(x='200', y='2')
rb2 = Radiobutton(text='Euro', variable=var, value='Euro', command=courses_today)
rb2.place(x='200', y='20')

lb2 = Label(text='Course: ')
lb2.place(x='0', y='60')

lb4 = Label(text='39')
lb4.place(x='150', y='62',)

lb3 = Label(text='Enter the amount in currency: ')
lb3.place(x='0', y='90')

en1 = Entry(width='20')
en1.place(x='150', y='93')

bt1 = Button(text='Convert', command=converter)
bt1.place(x='5', y='120')

lb5 = Label(text='', fg='red')
lb5.place(x='150', y='122')

window.mainloop()