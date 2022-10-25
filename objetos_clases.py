from abc import ABC, abstractmethod

class Juguete:
    _encendido = True
    
    def enciende(self):
        self._encendido = True
    
    def apaga(self):
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido


""" d = Dino()
d.apaga()
print(d.isEncendido())

d2 = Dino()
d2.enciende()
print(d2.isEncendido())

 """
 
 # Herencia
 

class Potato(Juguete):
    def quitarOreja(self):
        pass
    
    def ponerOreja(self):
        pass
    
class Dino(Juguete):
    color = None
    nombre = None
    
    def __init__(self, nombre):
        self.color = "Verde"
        self.nombre = nombre
    
    def verEscamas():
        pass

""" p = Dino("Daro")
print(p.color)
print(p.nombre) """


_encendido = False

def enciende():
    global _encendido
    _encendido = True
    print('Invoco a enciende')

def apaga():
    global _encendido
    _encendido = False

def isEncendido():
    return _encendido

diccionario = {
    '_encendido': False,
    'enciende': enciende,
    'apaga': apaga
}

""" probando = diccionario['_encendido']
diccionario['enciende']()
 """

# Clases Abstractas importar modulos, ver linea 1

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    
    def diHola(self):
        print('Hola')

class Perro(Animal):
    def sonido(self):
        print('Guau')

class Gato(Animal):
    def sonido(self):
        print("Miau")

""" p = Perro()
p.sonido()
p.diHola() #NO es abstarcto
g = Gato()
g.sonido() #NO es abstarcto
g.diHola() """

# HAS-A (composiciones)


class Motor:
    tipo = 'Diesel'

class Ventanas:
    cantidad = 5
    
    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4
    
class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    Carroceria = Carroceria()
    pass

""" c = Coche()
print('Motor es', c.motor.tipo)
print('Ventanas:',c.Carroceria.ventanas.cantidad)
c.Carroceria.ventanas.cambiarCantidad(3)
print('Ventanas:',c.Carroceria.ventanas.cantidad) """

class Categorias:
    idCategoria = 0
    nombre =''

class Proveedores:
    idProveedor = 0
    nombre = 0


class Productos:
    idProductos = 0
    CategoriaProducto = Categorias()
    precio = 0
    tamaño = 0
    tipoDeProducto = 0
    CIFProveedor = Proveedores()

p = Productos()
p.CIFProveedor.nombre
p.CategoriaProducto.idCategoria