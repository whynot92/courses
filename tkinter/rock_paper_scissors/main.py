from tkinter import *
import random

counter_win = 0
counter_lose = 0
counter_draw = 0

def play_game(play_choice):
    global counter_win, counter_lose, counter_draw
    computer_choice = random.randint(0, 3)
    
    if play_choice == computer_choice:
        counter_draw += 1
        lb4['text'] = 'Ничья'
        lb3['text'] = f'Ничей: {counter_draw}'
    elif play_choice > computer_choice:
        counter_win += 1
        lb4['text'] = 'Вы выиграли'
        lb1['text'] = f'Побед: {counter_win}'
    else:
        counter_lose += 1
        lb4['text'] = 'Вы проиграли'
        lb2['text'] = f'Проигрышей: {counter_lose}'

def stone():
    play_game(0)

def scissors():
    play_game(1)

def paper():
    play_game(2)



window = Tk()
window.title('Stone, Paper, Scissors')
window.geometry('300x120')

lb1 = Label(text=f'Побед: {counter_win}')
lb1.place(x='0', y='0')

lb2 = Label(text=f'Проигрышей: {counter_lose}')
lb2.place(x='0', y='20')

lb3 = Label(text=f'Ничей: {counter_draw}')
lb3.place(x='0', y='40')

lb4 = Label(text='Начало игры!', font='Arial 20')
lb4.place(x='110', y='15')

bt1 = Button(text='Камень', width='12', height='2', command=stone)
bt1.place(x='5', y='70')

bt2 = Button(text='Ножницы', width='12', height='2', command=scissors)
bt2.place(x='100', y='70')

bt3 = Button(text='Бумага', width='12', height='2', command=paper)
bt3.place(x='200', y='70')



window.mainloop()