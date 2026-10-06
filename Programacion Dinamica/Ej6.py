"""
Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando por botón del número inicial k. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual. Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos:

Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
Para N=2, depende de cuál dígito se comienza.
    Empezando por 0, son válidos 08 (cantidad: 1)
    Empezando por 1, son válidos 12, 14 (cantidad: 2)
    Empezando por 2, son válidos 21, 23, 25 (cantidad: 3)
    Empezando por 3, son válidos 32, 36 (cantidad: 2)
    Empezando por 4, son válidos 41, 45, 47 (cantidad: 3)
    Empezando por 5, son válidos 52, 54, 56, 58 (cantidad: 4)
    Empezando por 6, son válidos 63, 65, 69 (cantidad: 3)
    Empezando por 7, son válidos 74, 78 (cantidad: 2)
    Empezando por 8, son válidos 80, 85, 87, 89 (cantidad: 4)
    Empezando por 9, son válidos 96, 98 (cantidad: 2)

Métodos del grafo:
Grafo(dirigido = False, teclas_num_init = []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_teclas_num(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str
"""

from Backtracking.grafo import Grafo

def numeros_posibles(k, n):

    if n <= 0:
        return 0

    numero_inicial = str(k)

    teclado_numerico = Grafo(False, [])
    teclas_num = ['1','2','3','4','5','6','7','8','9','0']
    for v in teclas_num:
        teclado_numerico.agregar_vertice(v)

    aristas_teclado = [('1','2'),('1','4'),('2','3'),('2','5'),('3','6'),('4','5'),('4','7'),('5','8'),('5','6'),('6','9'),('7','8'),('8','9'),('8','0')]
    for v, w in aristas_teclado:
        teclado_numerico.agregar_arista(v, w)

    mem = {v: 1 for v in teclas_num} # Todas las teclas comienzan con 1 combinacion, su mismo numero

    for _ in range(2, n + 1): # Genero todas las combinaciones de n tamaño
        combinaciones = {}
        for v in teclas_num: # Por cada tecla
            cant_comb = 0
            for w in teclado_numerico.adyacentes(v): # Genero su combinacion
                cant_comb += mem[w]
            combinaciones[v] = cant_comb
        mem = combinaciones

    return mem[numero_inicial]

"""
Las combinaciones se hacen para 10 numeros distintos y para cada numero como maximo tengo 4 teclas adyacentes. Todas esas combinaciones se generan N veces:
    Por lo que la complejidad temporal en este problema es O(n*10*4) ==> O(n)

La complejidad espacial en este problema es guardar el caso de mem anterior, es un diccionario con como mucho 9 entradas con valores
"""
