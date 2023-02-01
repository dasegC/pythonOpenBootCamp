""" 
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""

def crearLista(paises):
    lista_paises = [pais for pais in paises.split(',')]
    lista_paises_ordenada = []
    lista_paises_ordenada.append((','.join(sorted(set(lista_paises)))))
    return lista_paises_ordenada

def solicitarPaises():
    paises = input('Ingresa nombres de países separados por coma:')
    return paises

def main():
    paises = solicitarPaises()
    lista_paises = crearLista(paises)
    print(lista_paises)

if __name__ == '__main__':
    main()
