from PIL import Image as PILImage
import sqlite3
import customtkinter as cs
from tkinter import *
from new_window import add_new_window
from del_window import del_user_window

def fetch_contacts():
    with sqlite3.connect(f"C:\\Programming\\courses\\SQLite3\\1st_work\\number_phone.bd") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT name, phone FROM number")
        contacts = cursor.fetchall()
    return contacts

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def update_frame_with_contacts(my_frame):
    clear_frame(my_frame)
    conttacts = fetch_contacts()

    for index, cont in enumerate(conttacts):
        name, phone = cont

        label = cs.CTkLabel(my_frame, text=f"{index + 1}. {name}: {phone}")
        label.pack(anchor='w', padx=10, pady=0)

def main():
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('343x365')
    app.resizable(False, False)
    app.title('My Telephone book')

    img_add = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-добавить-файл-64.png')
    img_add = img_add.resize((64, 64))  # Resize image if necessary
    img_add = cs.CTkImage(img_add)  # Create CTkImage object

    cs.CTkButton(app, text='Додати контакт       ', image=img_add, height=40, command=add_new_window).place(x=5, y=5)

    img_del = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-удалить-файл-64.png')
    img_del = img_del.resize((64, 64))
    img_del = cs.CTkImage(img_del)

    cs.CTkButton(app, text='Видалити контакт', image=img_del, height=40, command=del_user_window).place(x=180, y=5)

    img_update = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-обновить-документ-64.png')
    img_update = img_update.resize((64, 64))
    img_update = cs.CTkImage(img_update)

    cs.CTkButton(app, text='Оновити контакти', image=img_update, height=40, command=lambda: update_frame_with_contacts(my_frame)).place(x=95, y=50)

    my_frame = cs.CTkScrollableFrame(app, width=313, height=250)
    my_frame.place(x=4, y=95)

    update_frame_with_contacts(my_frame)
    app.mainloop()

if __name__ == '__main__':
    main()