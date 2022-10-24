from re import A


lista = ['a','b','c']
print(lista)
lista.append('x')
lista.append('y')
lista.append('z')
print(lista)
lista.remove('c')
print(lista)
abc = ['a','b','c']
print(abc)
xyz = ['x','y','z']
print(xyz)

diccionario = {
    "clave": "valor",
    "clave2": 15
}
print(diccionario)
print(diccionario["clave2"])
print(id(diccionario))
resultado = diccionario['clave']
print(resultado)

diccionario["clave"] = 99
print(diccionario["clave"])
print(diccionario)

diccionario = {"clave1":1,"clave2":2,"clave3":3,'clave4':4}
print(diccionario)
print(id(diccionario))
eliminado = diccionario.pop('clave1')
print(eliminado)
print(diccionario)

lista1 = [1,2,3,4,5,1,2,3,4,5,6]
print(lista1)
conjunto = {1,2,3,1,2,3,4,5,1,2,3,1,2,3}
print(conjunto)
conjunto2 = {7,8,9,10,2,3,2,1}
print(conjunto2)
print(conjunto|conjunto2) #Union de conjuntos

interseccion = conjunto & conjunto2 #Intersección de conjuntos
print(interseccion)

diferencia = conjunto - conjunto2
print(diferencia)

diferenciaSimetrica = conjunto ^ conjunto2
print(diferenciaSimetrica)

miTexto = "hola, esto es un textO"
print(miTexto.capitalize()) #capitalize() Primer letra en Mayuscula
print(miTexto.title()) #title() Primer letra de cada pakabra en Mayuscula
print(miTexto.lower())
print(miTexto.upper())
print(miTexto.replace('a', 'o')) 
print(miTexto.find('texto'))
print(miTexto.split()) #Array de strings separados por espacio en blanco
print(miTexto.split(','))#Array de strings separados por ,
print(miTexto.replace(',','').lower().split())
listaTexto = ['hola', 'esto', 'es', 'un', 'texto']
print(' '.join(listaTexto))
print('-'.join(listaTexto))
miVariableCompleta = ' '.join(listaTexto)
print(miVariableCompleta)

