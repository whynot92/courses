import sqlite3
import customtkinter as cs
from tkinter import *

def add_new_window():
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('300x300')
    app.resizable(False, False)
    app.title('Add new Phone number')

    app.mainloop()

def main():
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('500x500')
    app.resizable(False, False)
    app.title('My Telephone book')

    img_add = PhotoImage(file=f'SQLite3\\1st_work\\img\\icons8-добавить-файл-64.png')
    cs.CTkButton(app, text='Добавити контакт   ' , image=img_add, command=add_new_window).place(x=50, y=5)

    img_del = PhotoImage(file=f'SQLite3\\1st_work\\img\\icons8-удалить-файл-64.png')
    cs.CTkButton(app, text='Видалити контакт ' , image=img_del).place(x=260, y=5)

    img_edit = PhotoImage(file=f'SQLite3\\1st_work\\img\\icons8-редактирование-файла-64.png')
    cs.CTkButton(app, text='Редагувати контакт' , image=img_edit).place(x=50, y=60)

    img_update = PhotoImage(file=f'SQLite3\\1st_work\\img\\icons8-обновить-документ-64.png')
    cs.CTkButton(app, text='Оновити контакти ' , image=img_update).place(x=260, y=60)

    my_frame = cs.CTkScrollableFrame(app, width=470, height=360)
    my_frame.place(x=4, y=120)

    app.mainloop()

if __name__ == '__main__':
    main()
