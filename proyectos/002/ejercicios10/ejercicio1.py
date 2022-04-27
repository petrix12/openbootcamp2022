import tkinter
from tkinter import ttk

def OpcionSeleccionada():
    opcion_label = ttk.Label(window, text=seleccion.get())
    opcion_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

def Reiniciar():
    seleccion.set(None)
    opcion_label = ttk.Label(window, text="Seleccione una opción")
    opcion_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=4)

opcion_label = ttk.Label(window, text="Seleccione una opción")
opcion_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

seleccion = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Opción 1", value="Seleccionó la opción 1", variable=seleccion, command=OpcionSeleccionada)
r2 = ttk.Radiobutton(window, text="Opción 2", value="Seleccionó la opción 2", variable=seleccion, command=OpcionSeleccionada)
r3 = ttk.Radiobutton(window, text="Opción 3", value="Seleccionó la opción 3", variable=seleccion, command=OpcionSeleccionada)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

reset_button = ttk.Button(window, text="Reiniciar", command=Reiniciar)
reset_button.grid(column=1, row=4, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()