
"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien

(i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.
"""

def dominating_set_min(grafo):
    vertices = list(grafo.obtener_vertices())
    cant_vertices = len(vertices)

    # Lista de adjayentes de cada vertice, use este en vez de adjacentes por que me daba errores :s
    vecinos = {v: set(grafo.adyacentes(v)) for v in vertices}
    mejor_solucion = set(vertices)

    elegidos = set()
    dominados = set()
    frecuencias_dominacion = {}  # Lleva la cuenta de cuántas veces un vértice es dominado

    backtracking(0, vertices, vecinos, cant_vertices, elegidos, dominados, frecuencias_dominacion, mejor_solucion)

    return list(mejor_solucion)


def backtracking(idx, vertices, vecinos, cant_vertices, elegidos, dominados, frecuencias_dominacion, mejor_solucion):

    if len(elegidos) >= len(mejor_solucion):
        return

    if len(dominados) == cant_vertices:
        mejor_solucion.clear()
        mejor_solucion.update(elegidos)
        return

    if idx == cant_vertices:
        return

    v = vertices[idx]

    # Elegimos a 'v'
    elegidos.add(v)


    # Vertices que serían dominados si elegimos a 'v'
    afectados = vecinos[v] | {v}

    # Actualizamos dominación
    for u in afectados:
        frecuencias_dominacion[u] = frecuencias_dominacion.get(u, 0) + 1
        if frecuencias_dominacion[u] == 1: # Si es la primera vez que es dominado, lo agregamos al conjunto de dominados
            dominados.add(u)

    backtracking(idx + 1, vertices, vecinos, cant_vertices, elegidos, dominados, frecuencias_dominacion, mejor_solucion)

    # NO elegimos a 'v'
    elegidos.remove(v)
    for u in afectados:
        frecuencias_dominacion[u] -= 1
        if frecuencias_dominacion[u] == 0: # Nos fijamos que ya no esté dominado por ningún otro vértice elegido
            dominados.remove(u)

    backtracking(idx + 1, vertices, vecinos, cant_vertices, elegidos, dominados, frecuencias_dominacion, mejor_solucion)
