import tkinter
from tkinter import StringVar, ttk

window = tkinter.Tk()

# (0,0)    (1,0)   (2,0)
# (0,1)    (1,1)   (2,1)
# (0,2)    (1,2)   (2,2)
# (0,3)    (1,3)   (2,3)
# ##########################
# Label    Entry   (2,0)
# Label    Entry   (2,1)
# (0,2)    (1,2)   (2,1)


#window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Frame
""" frame = ttk.Frame(window)
label =ttk.Label(frame, text='hola')
label.grid(column=0,row=0, sticky=tkinter.W,padx=50,pady=50)

frame.grid(column=0,row=0,sticky=tkinter.W) """

# List Box
""" lista=['Windows','macOS','Linux','MS DOS','AmigaOS','BeOS']
lista_items = StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0,row=0,sticky=tkinter.W) """

# Radio Button
""" seleccionado = tkinter.StringVar()
r1=ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
r2=ttk.Radiobutton(window, text='No', value='2', variable=seleccionado)
r3=ttk.Radiobutton(window, text='Quizás', value='3', variable=seleccionado)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)

seleccionado2=tkinter.StringVar()
rs1=ttk.Radiobutton(window,text='Si2', value=12,variable=seleccionado2)
rs1.grid(column=1,row=0, padx=5,pady=5) """

# Checkbutton
""" def miFuncion():
    print('Clickeado')
seleccion = tkinter.StringVar()
check = ttk.Checkbutton(window, text='Acepto los términos', variable=seleccion, command=miFuncion)
check.grid(column=0, row=0, padx=5,pady=5) """

# Evento
""" def saludar(event):
    print('Han hecho click en saludar')


def saludarDobleClick(event):
    print('Han hecho doble click en saludar')

def salir(event):
    print('Adios')
    window.quit()


boton = tkinter.Button(window, text='Haz click')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludarDobleClick)

botonSalir = tkinter.Button(window,text='Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>', salir) """

window.mainloop()


#window.columnconfigure(0, weight=1)
#window.columnconfigure(1, weight=3)
