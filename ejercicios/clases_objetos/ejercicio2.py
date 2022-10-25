""" En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el 
resultado de la nota y si ha aprobado o no. """

class Alumno:
    #Inicilizo atributos
    def __init__(self, alumno, nota):
        self.alumno = alumno
        self.nota = nota
    
    def imprimir(self):
        print("El alumno: {} tiene como nota final: {}".format(self.alumno, self.nota))
        
    def resultado(self):
        if self.nota < 4:
            print("Ha desaprobado la materia")
        else:
            print("Ha aprobado la materia")

alumno = "Daro GMNZ"
nota = 10

alumno1 = Alumno(alumno, nota)
alumno1.imprimir()