# AND --> TRue, False

print('t y f', True & False)
print('t y t',True and True)
print('f y f',False & False)
print('f y t',False & True)

print('--------------')
# OR --> TRue, False
print('t o f', True or False)
print('t o t',True | True)
print('f o f',False | False)
print('f o t',False | True)

# XOR --> TRue, False
print('t xor f', True ^ False)
print('t xor t',True ^ True)
print('f xor f',False ^ False)
print('f xor t',False ^ True)

a = 5
b = 6
c = 7

if ((a >= 5) & (b <=6)):
    print('Esta condición es verdadera')
elif (a==5):
    print('Esta condición es verdadera pero no se ejecuta')

contador = 1;
while (contador <10):
    if (contador %2 == 0):
        print(contador, "es un número par")
    else:
        print(contador, "es un número impar")
    contador+=1
print('Fin del while')

lista = [1,2,3,'a']
longitud = len(lista)
print('La lista tiene', longitud, "items")

for valorActual in range(longitud):
    print(lista[valorActual])
    

listaPalabras = ['hola', 'mensaje', 'adios']

for palabra in listaPalabras:
    print('Palabra actual:',palabra)
    if (palabra == 'mensaje'):
        print('He encontrado la palabra mensaje')
        break

listaDesordenada = [3,4,1,2,5]
print(listaDesordenada)
listaOrdenada = sorted(listaDesordenada)
print(listaOrdenada)
listaOrdenadaReversa = sorted(listaDesordenada, reverse=True)
print(listaOrdenadaReversa)

valor = 1 #(input('Ingrese un valor del 1 al 5: '))

match valor:
    case 1:
        print("El valor es 1")
    case 2:
        print("El valor es 2")
    case 3:
        print("El valor es 3")
    case 4:
        print("El valor es 4")
    case 5:
        print("El valor es 5")
        
for palabra in listaPalabras:
    if palabra=='verbo':
        print('He encontrado la palabra mensaje')
        break
else:
    print('No he encontrado nada')