""" 
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""
try:
    archivo = open('ejercicio01.txt', 'w', encoding='utf8')
    archivo.write('Ejercicio 01 de ficheros')
    lectura = open('ejercicio01.txt','r+')
    archivo.seek(0)
    print(lectura.read())
except Exception as e:
    print(e)
finally:
    archivo.close()