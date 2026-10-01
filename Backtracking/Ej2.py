"""
Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str
"""

def colorear(grafo, n):

    vertices = grafo.obtener_vertices()

    if not vertices:
        return False

    colores = { v: None for v in vertices } # None es no coloreado

    return colorear_rec(grafo, vertices, 0, n, colores)



def colorear_rec(grafo, vertices, i, n, colores):

    if i == len(vertices):
        return True


    for color in range(n): # Color 0..n
        vertice = vertices[i]

        if es_compatible(grafo, vertice, color, colores):
            colores[vertice] = color

            if colorear_rec(grafo, vertices, i+1, n, colores):
                return True

            colores[vertice] = None

        colorear_rec(grafo, vertices, i+1, n, colores)

    return False

def es_compatible(grafo, vertice, color, colores):
    for w in grafo.adyacentes(vertice):
        if colores[w] == color:
            return False
    return True
