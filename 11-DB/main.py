import sqlite3
import getpass


def main():
    crear_usuario(5,'miguel2','gmnz')


def main2():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verificar_credenciales(username, password):
        print('Login Correcto.')
    else:
        print('Login incorrecto.')


def verificar_credenciales(username, password):
    conn = sqlite3.connect("./11-DB/miaplicacion.db")
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'

    rows = conn.execute(query)
    data = rows.fetchone()
    print(f'Data es: {type(data)}')

    cursor.close()
    conn.close()


def crear_usuario(identificador, username, password):
    conn = sqlite3.connect("./11-DB/miaplicacion.db",isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO users(id,username,password) VALUES(?,?,?)'''

    rows = conn.execute(query,(identificador,username,password))

    cursor.close()
    conn.close()
    
  


    

if __name__ == '__main__':
    main()