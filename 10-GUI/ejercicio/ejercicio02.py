""" 
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=4)
window.title('Ejercicio 02')
window.config(background='wheat')


def salir():
    window.quit()


label = tkinter.Label(
    window, text='Seleccione una de las opciones de la lista', bg='blue', fg='white')
label.grid(column=0, row=0, sticky=tkinter.N)

lista_cursos = ['Python', 'C++', 'C#', 'Java', 'Javascript', 'php']
lista_items = tkinter.StringVar(value=lista_cursos)
list_box = tkinter.Listbox(window, height=10, width=9,
                           borderwidth=2, listvariable=lista_items, background='wheat')
list_box.grid(column=0, row=1, sticky=tkinter.W)


boton = tkinter.Button(window, text='Salir', command=salir).grid(
    column=0, row=4, ipadx=5, ipady=5, sticky=tkinter.S)


window.mainloop()
