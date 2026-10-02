"""
Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

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

def hay_isomorfismo(g1, g2):
    v1 = g1.obtener_vertices()
    v2 = g2.obtener_vertices()

    if len(v1) != len(v2):
        return False

    grados_g1 = sorted([len(g1.adyacentes(v)) for v in v1])
    grados_g2 = sorted([len(g2.adyacentes(v)) for v in v2])
    if grados_g1 != grados_g2:
        return False

    # Mapeos y seguimiento de vértices usados
    mapeo = {}            # v_g1 -> v_g2
    usados_g2 = set()     # Conjunto de vértices de G2 ya mapeados

    return hay_isomorfismo_rec(g1, v1, 0, g2, v2, mapeo, usados_g2)


def hay_isomorfismo_rec(g1, v1_lista, idx, g2, v2_lista, mapeo, usados_g2):

    if idx == len(v1_lista):
        return True

    v1_actual = v1_lista[idx]

    # Probamos asociar v1_actual con cada vértice candidato en G2
    for candidato_v2 in v2_lista:
        if candidato_v2 in usados_g2:
            continue  # Este vértice de G2 ya fue asignado a otro de G1

        # Verificar si la asignación v1_actual -> candidato_v2 es consistente
        if es_valido(g1, v1_actual, g2, candidato_v2, mapeo):

            # A) Hacemos la elección
            mapeo[v1_actual] = candidato_v2
            usados_g2.add(candidato_v2)

            # B) Avanzamos al siguiente vértice de G1
            if hay_isomorfismo_rec(g1, v1_lista, idx + 1, g2, v2_lista, mapeo, usados_g2):
                return True

            # C) Deshacemos la elección (BACKTRACKING)
            del mapeo[v1_actual]
            usados_g2.remove(candidato_v2)

    return False

def es_valido(g1, v1_actual, g2, candidato_v2, mapeo):
    # Condición 1: Deben tener el mismo número de vecinos
    if len(g1.adyacentes(v1_actual)) != len(g2.adyacentes(candidato_v2)):
        return False

    # Condición 2: Preservar las aristas con los vértices de G1 YA mapeados
    for v1_anterior, v2_anterior in mapeo.items():
        # Si v1_actual está conectado con v1_anterior en G1...
        estan_unidos_g1 = g1.estan_unidos(v1_actual, v1_anterior)
        # ...entonces candidato_v2 DEBE estar conectado con v2_anterior en G2 (y viceversa)
        estan_unidos_g2 = g2.estan_unidos(candidato_v2, v2_anterior)

        if estan_unidos_g1 != estan_unidos_g2:
            return False

    return True
