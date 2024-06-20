from tkinter import *
import random

secret_number = random.randint(1, 100)
counter = 0

def input_validation():
    global counter
    input_text = input_user.get()

    if input_text.isdigit() and 1 <= int(input_text) <= 100:
        guess = int(input_text)
        
        if counter < 7:
            if guess > secret_number:
                lb3['text'] = 'Your number is more mysterious'
            elif guess < secret_number:
                lb3['text'] = 'Your number is less mysterious'
            else:
                lb3['text'] = 'you won'
                return
            counter += 1
        if counter >= 7:
            lb3['text'] = 'You have used all the attempts. Another time.'
    else:
        lb3['text'] = 'Incorrectly entered data'

window = Tk()
window.title('Guess the number')
window.geometry('300x200')

lb1 = Label(text='I guessed a number from 1 to 100')
lb1.grid(row=0, column=0, columnspan=2)

lb2 = Label(text='Enter a number:')
lb2.grid(row=1, column=0)

input_user = Entry(width=6)
input_user.grid(row=1, column=1)

bt1 = Button(text='Click', command=input_validation)
bt1.grid(row=2, column=0, columnspan=2)

lb3 = Label(text='', bg='gray', width=43, height=5)
lb3.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
