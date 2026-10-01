
"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.
"""

def vertex_cover_min(grafo):
    vertices = list(grafo.obtener_vertices())
    mejor_solucion = [set(vertices)]
    solucion_actual = set()

    backtrack(grafo, solucion_actual, mejor_solucion, vertices, 0)
    return list(mejor_solucion[0])


def es_vertex_cover(solucion, grafo):
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v not in solucion and w not in solucion:
                return False
    return True


def backtrack(grafo, solucion_actual, mejor_solucion, vertices, index):

    if len(solucion_actual) >= len(mejor_solucion[0]):  # Poda: no seguir buscando soluciones peores o iguales
        return

    if index == len(vertices):  # Caso base: ya se consideraron todos los vertices
        if es_vertex_cover(solucion_actual, grafo): # Todos los vertices estan en la solucion
            mejor_solucion[0] = set(solucion_actual)
        return

    v = vertices[index]

    if v in solucion_actual:
        backtrack(grafo, solucion_actual, mejor_solucion, vertices, index + 1)
        return

    solucion_actual.add(v)
    backtrack(grafo, solucion_actual, mejor_solucion, vertices, index + 1)
    solucion_actual.remove(v)

    forzados = [w for w in grafo.adyacentes(v) if w not in solucion_actual]

    for w in forzados:
        solucion_actual.add(w)

    backtrack(grafo, solucion_actual, mejor_solucion, vertices, index + 1)

    for w in forzados:
        solucion_actual.remove(w)
