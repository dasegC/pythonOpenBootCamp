""" import _thread
import time


def horaActual(nombre_thread, tiempo_de_espera):
    count = 0
    while count < 5:
        time.sleep(tiempo_de_espera)
        print(f'hilo: {nombre_thread} - {time.ctime(time.time())} ')

_thread.start_new_thread(horaActual, ('thread_uno', 1))
_thread.start_new_thread(horaActual, ('thread_dos', 2))

print('He disparado los hilos')

while True:
    pass """

""" import logging


logging.basicConfig(level=logging.DEBUG)
logging.debug('Prueba de debug')
logging.info('Arrancando programa')
logging.warning('Hace calor')
logging.error('test')
logging.critical('adios') """

# map, filter, reducee

# FILTER
""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def miFuncion(x):
    if x % 2 == 0:
        return True

    return False

resultado = filter(miFuncion, numeros)# Si devuelve True, guarda valor en var
resultado = filter(lambda x: x%2 == 0, numeros) 
print(list(resultado)) """

# MAP
""" def cuadrado(x):
    return x*x

resultado = map(cuadrado, [1,2,3,4,5,6,7,8,9]) #aplica la func a c/elem del iterable 
resultado = map(lambda x: x*x, [1,2,3,4,5,6,7,8,9])
print(list(resultado)) """

# REDUCE

""" from functools import reduce
def suma(a, b):
    print(f'a: {a} - b: {b}')
    return a + b



res = reduce(suma, [1, 2, 3, 4, 5]) # Ejecuta func recurs hasta que list se quede con un elem
res = reduce(lambda a,b:a+b, [1,2,3,4,5])
print(res) """


# ZIP
""" cursos = ['java', 'Python', 'Git']
asistentes = [15, 20, 4]
demo = zip(cursos, asistentes)
print(list(demo)) """


# ALL - ANY
""" listaA = [1 == 1, 2 == 2, 3 == 4]
#res = any(listaA) # SI una condicion es verdadera retorna True
res = all(listaA) # TODAS las cond deben ser verd o retorna False
print(res) """


# ROUND
""" a = 5.5
b = 5.4
c = 5.6

print(round(a))
print(round(b))
print(round(c)) """

# MIN - MAX
""" print(min(1,2,3,4,5,6,7,8))
print(max(1,2,3,4,5,6,7,8)) """

# POW
""" print(pow(2, 4)) """

# SORTED
""" lista = ['z', 'c', 'd', 'a']
ordenada = sorted(lista)
ordenada_reversa = sorted(lista, reverse=True)
ordenada_reversa_key = sorted(lista, reverse=True, key=lambda x:str(x).startswith('a'))
print(ordenada)
print(ordenada_reversa)
print(ordenada_reversa_key) """


# INPUT

""" from getpass import getpass
user = input('Username: ')
passwd = getpass('Password: ')

print(user, passwd) """

