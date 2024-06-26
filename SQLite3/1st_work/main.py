from PIL import Image as PILImage
import sqlite3
import customtkinter as cs
from tkinter import *
from new_window import add_new_window

def main():
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('460x487')
    app.resizable(False, False)
    app.title('My Telephone book')

    img_add = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-добавить-файл-64.png')
    img_add = img_add.resize((64, 64))  # Resize image if necessary
    img_add = cs.CTkImage(img_add)  # Create CTkImage object

    cs.CTkButton(app, text='Додати контакт       ', image=img_add, height=40, command=add_new_window).place(x=50, y=5)

    img_del = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-удалить-файл-64.png')
    img_del = img_del.resize((64, 64))
    img_del = cs.CTkImage(img_del)

    cs.CTkButton(app, text='Видалити контакт', image=img_del, height=40).place(x=260, y=5)

    img_edit = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-редактирование-файла-64.png')
    img_edit = img_edit.resize((64, 64))
    img_edit = cs.CTkImage(img_edit)

    cs.CTkButton(app, text='Редагувати контакт', image=img_edit, height=40).place(x=50, y=60)

    img_update = PILImage.open(f'SQLite3\\1st_work\\img\\icons8-обновить-документ-64.png')
    img_update = img_update.resize((64, 64))
    img_update = cs.CTkImage(img_update)

    cs.CTkButton(app, text='Оновити контакти', image=img_update, height=40).place(x=260, y=60)

    my_frame = cs.CTkScrollableFrame(app, width=430, height=360)
    my_frame.place(x=4, y=110)

    app.mainloop()

if __name__ == '__main__':
    main()