""" 
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

def nota_minima(notas):
    minimo = min(notas)
    while (notas.count(minimo)>0):
        for i in notas:
            if i == minimo:
                notas.remove(i)
    minimo_2 = min(notas)
    return minimo_2

def listar_nombres(estudiantes, notas_minimas):
    nombres = []
    for i in range(len(estudiantes)):
        if (estudiantes[i][1] == notas_minimas):
            nombres.append(estudiantes[i][0])
    nombres = sorted(nombres)
    return nombres
        
def imprimir_listado(lista_nombres):
    for i in lista_nombres:
        print(i)

if __name__ == '__main__':
    estudiantes = []
    notas = []
    
    for i in range(int(input())):
        name = input()
        score = float(input())
        
        estudiantes.append([name,score]) 
        notas.append(score) 
        notas = sorted(notas)
    
    segundo_minimo = nota_minima(notas)
    nombres = listar_nombres(estudiantes,segundo_minimo)
    imprimir_listado(nombres)
