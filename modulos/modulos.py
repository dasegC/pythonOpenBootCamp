from unittest import result
import operaciones  as o

def main():
    """ resultado = o.suma(2,2)
    print('Hola en Main', resultado)
    resta = o.resta(4,2)
    print(resta) """
    print(o.como_me_llamo())
    
    op = o.Operador()
    print(op.Multiplicacion(4,2))
    print(o.PI)

if __name__ == '__main__':
    main()