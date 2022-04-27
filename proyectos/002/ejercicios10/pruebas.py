import tkinter
from tkinter import colorchooser

window = tkinter.Tk()
filename = colorchooser.askcolor(initialcolor='#ffffff')
window.mainloop()