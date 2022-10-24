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
    print('contador vale: ', contador)
    contador+=1
print('Fin del while')