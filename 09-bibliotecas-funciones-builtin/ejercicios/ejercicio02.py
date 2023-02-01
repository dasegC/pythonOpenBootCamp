""" 
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce

array = [1, 2, 3, 4, 5, 6]


def obtenerImpares(lista):
    impares = list(filter(lambda x: x % 2 != 0, lista))
    print(f'Los números impares obvtenidos del iterable son:\n {impares}')
    return impares


def sumarElementos(lista):
    resultado_suma = reduce(lambda a, b: a+b, lista)
    print(
        f'El resultado de la suma de los elementos impares es:\n {resultado_suma}')


def main():
    parasumar = obtenerImpares(array)
    sumarElementos(parasumar)


if __name__ == '__main__':
    main()
