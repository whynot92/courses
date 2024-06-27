import customtkinter as cs
import sqlite3

def del_from_bd(name):
    with sqlite3.connect(F'SQLite3\\1st_work\\number_phone.bd') as bd:
        cursor = bd.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS number(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       phone TEXT
                       )''')
        
        cursor.execute('DELETE FROM number WHERE name = ?', (name,))
        if cursor.rowcount == 0:
            raise ValueError(f'No user with name "{name}" found in the database')

def del_user_window():
    global name_entry
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('300x170')
    app.resizable(False, False)
    app.title('Delete contacts')

    def add_to_bd():
        name = name_entry.get()
        try:
            del_from_bd(name)
            name_entry.delete(0, 'end')
            app.destroy()
        except ValueError as e:
            lb2 = cs.CTkLabel(app, text=f'!!!Пользователя нет в базе!!!', text_color='red')
            lb2.place(x=65, y=80)


    lb1 = cs.CTkLabel(app, text=f"Введіть им'я контакта для видалення:")
    lb1.place(x=25,y=2)
    name_entry = cs.CTkEntry(app, width=290)
    name_entry.place(x=3, y=30)

    bt = cs.CTkButton(app, text='Видалити', command=add_to_bd)
    bt.place(x=80, y=130)

    app.mainloop()

