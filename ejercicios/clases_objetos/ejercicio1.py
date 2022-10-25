""" En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola. """

class Vehiculo():
    def __init__(self, color, ruedas, puertas): #Creo constructor
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
    def __str__(self):
        return "El coche es de color {}, tiene {} ruedas y {} puertas. ".format(self.color,self.ruedas, self.puertas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + "Con una velocidad de {} km/h y una cilindrada de {}".format(self.velocidad, self.cilindrada)

auto = Coche('rojo',4,4,150,1200)
print(auto)