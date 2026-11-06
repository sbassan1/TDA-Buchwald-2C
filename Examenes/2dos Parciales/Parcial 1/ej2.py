"""
Tenemos un grafo no dirigido que representa una grilla de n×n. Definimos que un vértice en la fila i y columna j es el vértice (i, j). Todos los vértices tienen exactamente 4 adyacentes, salvo los de los bordes, es decir los de la primera y última fila o columna.

Implementar una función que dado el grafo y m puntos iniciales distintos en la grilla (i1, j1), ···, (im, jm), determine si existen m caminos disjuntos (de vértices) donde cada uno comience en un punto inicial, y termine en m puntos diferentes del borde. En los ejemplos del dorso, el de la izquierda tiene solución (la cuál se muestra) mientras que el de la derecha no tiene solución. Utilizar redes de flujo para resolver este problema. Indicar y justificar la complejidad del algoritmo implementado.

Metodos de grafo
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

# Grilla es grafo no dirigido con pesos de 1
# Puntos es una lista de (i,j) de los puntos iniciales
# Tenemos acceso a funcion ford_fulkerson(red,s,t)

from grafo import Grafo

def existen_m_caminos(grilla, puntos):
    red = Grafo(dirigido=True)
    
    s = 's'
    t = 't'
    red.agregar_vertice(s)
    red.agregar_vertice(t)
    
    for v in grilla.obtener_vertices():
        v_in = (v, 'in')
        v_out = (v, 'out')
        red.agregar_vertice(v_in)
        red.agregar_vertice(v_out)
        red.agregar_arista(v_in, v_out, peso=1)

    for v in grilla.obtener_vertices():
        v_out = (v, 'out')
        for w in grilla.adyacentes(v):
            w_in = (w, 'in')
            red.agregar_arista(v_out, w_in, peso=float('inf'))

    for punto in puntos:
        punto_in = (punto, 'in')
        red.agregar_arista(s, punto_in, peso=1)

    for v in grilla.obtener_vertices():
        if len(grilla.adyacentes(v)) < 4:
            v_out = (v, 'out')
            red.agregar_arista(v_out, t, peso=1)

    flujo_maximo, _ = ford_fulkerson(red, s, t)

    return flujo_maximo == m