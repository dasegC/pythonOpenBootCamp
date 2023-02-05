""" 
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""

import tkinter
from tkinter import StringVar, ttk


window = tkinter.Tk()
window.title('Ejercicio 01')
window.config(background='wheat')
window.columnconfigure(0, weight=4)


label = tkinter.Label(
    window, text='Seleccione una de las opciones...', bg='blue', fg='white')
label.grid(column=0, row=0, sticky=tkinter.N)


def mostrarSeleccion():
    window.config(print('Ha seleccionado la {}'.format(seleccion.get())))


def reset():
    seleccion.set(None)
    
def salir():
    window.quit()

seleccion = tkinter.StringVar()
seleccion.set(None)
radio_1 = ttk.Radiobutton(window, text='Opción 1', value='Opcion 1',
                          variable=seleccion, command=mostrarSeleccion)
radio_2 = ttk.Radiobutton(window, text='Opción 2', value='Opcion 2',
                          variable=seleccion, command=mostrarSeleccion)
radio_3 = ttk.Radiobutton(window, text='Opción 3', value='Opcion 3',
                          variable=seleccion, command=mostrarSeleccion)


radio_1.grid(column=0, row=1, padx=5, pady=5,
             ipadx=2, ipady=2, sticky=tkinter.W)
radio_2.grid(column=0, row=2, padx=5, pady=5,
             ipadx=2, ipady=2, sticky=tkinter.W)
radio_3.grid(column=0, row=3, padx=5, pady=5,
             ipadx=2, ipady=2, sticky=tkinter.W)


boton = tkinter.Button(window, text='Reiniciar', command=reset).grid(column=0,row=4, ipadx=5,ipady=5,sticky=tkinter.W)
boton = tkinter.Button(window,text='Salir', command=salir).grid(column=1,row=4, ipadx=5,ipady=5,sticky=tkinter.E)

window.mainloop()
