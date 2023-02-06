""" 
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""
import sqlite3


def crear_db():
    conn = sqlite3.connect('./ejercicio01.db')
    cursor_db = conn.cursor()

    cursor_db.execute(
        'CREATE TABLE IF NOT EXISTS Alumnos(id INT PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL)')

    conn.commit()

    cursor_db.close()
    conn.close()


def insertar_alumno(id, nombre, apellido):
    conn = sqlite3.connect('./ejercicio01.db')
    cursor_db = conn.cursor()

    query = '''INSERT INTO Alumnos(id, nombre, apellido) VALUES(?,?,?)'''
    row = conn.execute(query, (id, nombre, apellido))
    conn.commit()

    cursor_db.close()
    conn.close()


def mostrar_alumno(nombre):
    conn = sqlite3.connect('./ejercicio01.db')
    cursor_db = conn.cursor()

    query = f'SELECT * FROM ALUMNOS WHERE nombre="{nombre}"'
    row = conn.execute(query)
    data = row.fetchall()
    print(data)

    cursor_db.close()
    conn.close()


if __name__ == '__main__':

    opcion = None
    while opcion != 4:
        try:
            print('Sistema de Carga de ALumnos')
            print('1 - Crear Base de Datos de Alumnos')
            print('2 - Insertar Alumnos')
            print('3 - Mostrar Alumno')
            print('4 - Salir')
            opcion = int(input('Escribe tu opción: (1 - 4): '))
            if opcion == 1:
                crear_db()
            elif opcion == 2:
                identificador = input('Ingrese el identificador del alumno: ')
                nombre = input('Ingrese el nombre del alumno: ')
                apellido = input('Ingrese el apellido del alumno: ')
                insertar_alumno(identificador, nombre, apellido)
            elif opcion == 3:
                alumno = input('Ingrese el nombre del alumno: ')
                mostrar_alumno(alumno)
        except Exception as e:
            print(f'Ha ocurrido un error: {e}')
    else:
        print('Saliendo del programa...')
