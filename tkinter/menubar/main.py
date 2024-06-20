from tkinter import *

window = Tk()

mine_menu = Menu()
window.config(menu=mine_menu)

filemenu = Menu(mine_menu, tearoff=0)
mine_menu.add_cascade(label='File', menu=filemenu)

filemenu.add_cascade(label='New')
filemenu.add_cascade(label='Save')
filemenu.add_cascade(label='Open')
filemenu.add_separator()
filemenu.add_cascade(label='Exit')

editmenu = Menu(mine_menu, tearoff=0)
mine_menu.add_cascade(label='Edit', menu=editmenu)

editmenu.add_cascade(label='News')
editmenu.add_cascade(label='Save')
editmenu.add_cascade(label='Open')
editmenu.add_separator()
editmenu.add_cascade(label='Exit')

view_menu = Menu(mine_menu, tearoff=0)
mine_menu.add_cascade(label='View', menu=view_menu)

view_menu.add_cascade(label='test')
view_menu.add_cascade(label='Save')
view_menu.add_cascade(label='Open')
view_menu.add_separator()
view_menu.add_cascade(label='Exit')

window.mainloop()