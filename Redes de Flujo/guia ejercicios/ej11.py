"""
Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima. Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de préstamos. ¿Cuál es el orden temporal de la solución implementada?
"""


"""
Queremos modelar el problema para una red de flujo, nos piden asignar libros a alumnos de tal forma que la cantidad de libros a prestar sea la maxima.

Tenemos tres copias de cada libro, cada alumno quiere libros diferentes.

- Comenzaremos con un vertice fuente, de este vertice conectaremos aristas a vertices libro, cada arista (fuente,libro) tendrá una capacidad de 3 para simbolizar las copias de la biblioteca.

- El prestamo de libros se representará como una arista de un vertice libro a un vertice alumno con capacidad 1, ya que cada alumno pedira solo una copia (no esta asegurado que la conseguiran).

- Luego de los vertices alunmnos que tienen sus libros prestados conectaremos cada uno a un sumidero con capacidad de arista infinito (o de la cantidad de libros) para simbolizar la cantidad total de libros que tienen.

- De tal forma que para ver la cantidad maxima de libros a prestar es el resultado de ver el flujo máximo que pasa a el sumidero. 


"""

#pedidos es un diccionario donde las llaves son los alumnos y los valores son una lista de libros

from Backtracking.grafo import Grafo

def cantidad_max_libros(pedidos):

    red = Grafo(True, [])
    s = 's'
    t = 't'
    red.agregar_vertice(s)
    red.agregar_vertice(t)
    
    libros_procesados = set()

    for alumno, lista_libros in pedidos.items():
        v_alum = ('alumno', alumno)
        red.agregar_vertice(v_alum)
        red.agregar_arista(v_alum, t, 10)

        for libro in lista_libros:
            v_lib = ('libro', libro)
            
            if libro not in libros_procesados:
                red.agregar_vertice(v_lib)
                red.agregar_arista(s, v_lib, 3)
                libros_procesados.add(libro)
            
            red.agregar_arista(v_lib, v_alum, 1)
            
    dic_flujo = ford_fulkerson(red, s, t) 
    
    asignaciones = {}
    for alumno, lista_libros in pedidos.items():
        asignaciones[alumno] = []
        v_alum = ('alumno', alumno)
        
        for libro in lista_libros:
            v_lib = ('libro', libro)
            if v_lib in dic_flujo and v_alum in dic_flujo[v_lib] and dic_flujo[v_lib][v_alum] == 1:
                asignaciones[alumno].append(libro)
                
    return asignaciones