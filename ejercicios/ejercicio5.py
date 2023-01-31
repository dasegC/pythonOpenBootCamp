# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anoBisiesto(ano):
    if (ano % 4 == 0):
        if (ano % 100 == 0):
            if (ano % 400 == 0):
                print(ano, "Es un año bisiesto")
            else:
                print(ano, "NO es un año bisiesto")
        else:
            print(ano, "Es un año bisiesto")
    else:
        print(ano, "NO es un año bisiesto")

ano = int(input('Ingrese el año a comprobar: '))
anoBisiesto(ano)