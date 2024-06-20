from tkinter import *


def add_lang():
    sc.insert(END, input_lang.get())

def delete_selected():
    selected_item = sc.curselection()
    sc.delete(selected_item[0])

window = Tk()
window.title('List Lang BOX')
window.geometry('280x325')

input_lang = Entry(width='33',)
input_lang.place(x='3', y='8', )

bt1 = Button(text='Вставити', font='Arial 10', command=add_lang)
bt1.place(x='210', y='3')

sc = Listbox(width='45', height='15')
sc.place(x='2', y='35')


bt2 = Button(text='Удалить', font='Arial 10', command=delete_selected)
bt2.place(x='213', y='285')



window.mainloop()