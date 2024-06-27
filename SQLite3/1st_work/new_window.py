import customtkinter as cs
import sqlite3

def update_bd(name, number):

    with sqlite3.connect(F'SQLite3\\1st_work\\number_phone.bd') as bd:
        cursor = bd.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS number(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       phone TEXT
                       )''')
        
        cursor.execute("INSERT INTO number (name, phone) VALUES (?, ?)", (name, number))


def add_new_window():
    global name_entry, number_entry
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('300x170')
    app.resizable(False, False)
    app.title('Add new Phone number')

    def add_to_bd():
        name = name_entry.get()
        number = number_entry.get()
        update_bd(name, number)

        name_entry.delete(0, 'end')
        number_entry.delete(0, 'end')
        app.destroy()

    lb1 = cs.CTkLabel(app, text=f"Напишіть Им'я нового контакта:")
    lb1.place(x=50,y=2)
    name_entry = cs.CTkEntry(app, width=290)
    name_entry.place(x=3, y=30)

    lb2 = cs.CTkLabel(app, text=f"Напишіть номер телефона:")
    lb2.place(x=70,y=60)
    number_entry = cs.CTkEntry(app, width=290)
    number_entry.place(x=3, y=90)

    bt = cs.CTkButton(app, text='Додати', command=add_to_bd)
    bt.place(x=80, y=130)

    app.mainloop()

