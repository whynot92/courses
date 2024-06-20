from tkinter import *

window = Tk()
window.title('My class')
window.geometry('500x300')

def grade_class():
    my_grade = var.get()
    lb1['text'] = f'I study in the {my_grade}'

var = StringVar()
var.set('1st grade')

lb2 = Label(text='Choose your class')
lb2.pack()

for i in range(1, 11):
    radio_one = Radiobutton(text=f'{i}st grade', variable=var, value=f'{i}st grade', command=grade_class)
    radio_one.pack()

lb1 = Label(text='I study in the 1st grade', fg='red')
lb1.pack()


window.mainloop()