import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=10)

lista = ['Laravel', 'Vue.js', 'MongoDB', 'Reect.js', 'Node.js', 'Angular', 'Python', 'JavaScript', 'MySQL']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

libre_label = ttk.Label(window, text="El texto que queráis")
libre_label.grid(column=1, row=0, sticky=tkinter.W, padx=5, pady=5)

window.mainloop()