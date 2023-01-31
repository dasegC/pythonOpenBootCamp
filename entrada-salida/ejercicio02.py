""" 
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle


class Vehiculo:
    def __init__(self, color, ruedas, puertas) -> None:
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self) -> str:
        return f'El vehículo es de color {self.color}, tiene {self.ruedas} ruedas y {self.puertas} puertas.'

def crearArchivo():
    try:
        auto = Vehiculo('Azul', 4, 5)
        archivo = open('./entrada-salida/vehiculo.bin', 'wb')
        pickle.dump(auto, archivo)
    except Exception as e:
        print(e)
    finally:
        archivo.close()
    

def leerArchivo():
    try:
        archivo = open('./entrada-salida/vehiculo.bin', 'rb')
        vehiculo = pickle.load(archivo)
    except Exception as e:
        print(e)
    finally:
        archivo.close()
        return vehiculo

def main():
    crearArchivo()  
    datos = leerArchivo()
    print(datos)


if __name__ == '__main__':
    main()