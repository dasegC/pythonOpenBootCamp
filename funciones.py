anonima = lambda : print("Hola")
anonima()

#Con un parametro
anonima2 = lambda nombre : print('Hola',nombre)
anonima2("Daro")
#COn mas parametros
anonima3 = lambda nombre, saludo : print('Hola',nombre, saludo)
anonima3("Daro", "Como estas?")
# Las funciones anonimas no tienen return, se escriben asi
sumatoria = lambda x, y : x + y
print(sumatoria(2,2))