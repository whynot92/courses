import customtkinter as cs


def add_new_window():
    cs.set_appearance_mode('Default')
    cs.set_default_color_theme('blue')

    app = cs.CTk()
    app.geometry('300x170')
    app.resizable(False, False)
    app.title('Add new Phone number')

    lb1 = cs.CTkLabel(app, text=f"Напишіть Им'я нового контакта:")
    lb1.place(x=50,y=2)
    name_entry = cs.CTkEntry(app, width=290)
    name_entry.place(x=3, y=30)

    lb2 = cs.CTkLabel(app, text=f"Напишіть номер телефона:")
    lb2.place(x=70,y=60)
    number_entry = cs.CTkEntry(app, width=290)
    number_entry.place(x=3, y=90)

    bt = cs.CTkButton(app, text='Додати')
    bt.place(x=80, y=130)

    app.mainloop()
