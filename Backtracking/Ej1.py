"""
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
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

def no_adyacentes(grafo, n):
    vertices = grafo.obtener_vertices()

    if n > len(vertices):
        return None

    solucion_parcial = set()
    return no_adyacentes_rec(grafo, vertices, 0, solucion_parcial, n)


def no_adyacentes_rec(grafo, vertices, i, solucion_parcial, n):

    if len(solucion_parcial) == n:
        return list(solucion_parcial)

    if i == len(vertices) or len(solucion_parcial) + (len(vertices) - i) < n: # (Si llegamos al final y no tenemos una solucion || si no llegamos a n con lo que queda) ==> fuimos
        return None

    solucion_optima = None
    v_actual = vertices[i]

    if es_compatible(grafo, solucion_parcial, v_actual): # Si el vertice actual es compatible con la sol actual lo agregamos
        solucion_parcial.add(v_actual)
        solucion_optima = no_adyacentes_rec(grafo, vertices, i + 1, solucion_parcial, n)
        solucion_parcial.remove(v_actual)

    if solucion_optima is None:
        solucion_optima = no_adyacentes_rec(grafo, vertices, i + 1, solucion_parcial, n)

    return solucion_optima


def es_compatible(grafo, solucion_parcial, vertice):
    for v in solucion_parcial:
        if vertice in grafo.adyacentes(v):
            return False
    return True
