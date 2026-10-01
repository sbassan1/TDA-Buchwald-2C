"""
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.

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

def independent_set(grafo):
    vertices = grafo.obtener_vertices()

    if len(vertices) == 0:
       return []

    sol_local = set()
    sol_opt = set()

    return list(independent_set_rec(grafo, vertices, 0, sol_local, sol_opt))


def independent_set_rec(grafo, vertices, i, sol_local, sol_opt):
    if i == len(vertices):
        if len(sol_local) > len(sol_opt):
            return sol_local.copy()
        return sol_opt

    if len(sol_local) + (len(vertices) - i) <= len(sol_opt):
        return sol_opt

    v_actual = vertices[i]

    if es_compatible(grafo, v_actual, sol_local):
        sol_local.add(v_actual)
        sol_opt = independent_set_rec(grafo, vertices, i + 1, sol_local, sol_opt)
        sol_local.remove(v_actual)

    sol_opt = independent_set_rec(grafo, vertices, i + 1, sol_local, sol_opt)

    return sol_opt


def es_compatible(grafo, vertice, sol_local):
    for v in sol_local:
        if vertice in grafo.adyacentes(v):
            return False
    return True
