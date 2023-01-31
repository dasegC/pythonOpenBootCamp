# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

#Usando for 
lista= []
for numero in range(1,101):
    lista.append(numero)
print(sorted(lista, reverse=True))

#Usando while
contador = 100
while contador >=1:
    print(contador)
    contador-=1