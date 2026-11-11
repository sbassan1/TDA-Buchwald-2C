
"""
Shane Hollander e Ilya Rozanov, las dos máximas estrellas y eternos rivales de la liga de hockey sobre hielo, deben organizar durante los playoffs la distribución de equipamiento oficial entre las distintas arenas donde se juegan los partidos. Cuentan con un grafo dirigido y pesado donde las aristas representan rutas terrestres y su peso indica la capacidad (en bolsos) del camión asignado a ese tramo. En cada vértice tenemos un valor w(v) que implica: si es positivo, se trata de un depósito desde el cual se pueden cargar hasta esa cantidad de bolsos; si es negativo, se trata de una arena que necesita recibir esa cantidad de bolsos para que se pueda disputar el partido; si es 0, es simplemente un punto de trasbordo donde se puede cambiar de camión 

Usando redes de flujo, implementar un algoritmo que reciba dicho grafo y determine si es posible cumplir con los requisitos de todas las arenas. No es necesario indicar cómo serían los traslados. Indicar y justificar la complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo
"""


"""
Tenemos un grafo dirigido donde las aristas representan la capacidad del camion en ese momento. Los vertices pueden ser de oferta y demanda (De forma que si son positivos se deben agregar bolsos y si son negativos entonces se debe dejar una cantidad de bolsos)

Viendo esto para modelar esta red deberemos usar una Super Fuente y un Super Sumidero, conectandolo a los vertices positivos y/o negativos con w para que agreguen o quiten flujo (peso de bolsos):

- Todas los vertices con w(v) >= 0, se conectan con una arista a la super fuente (S,v, w(v))
- Todas los vertices con w(v) > 0, se conectan con una arista al super sumidero (T,v, -w(v))

Para verificar que todos los vertices demanda (negativos) son tomados en cuenta, debemos verificar que el flujo al Super Sumidero es >= a la cantidad de demanda.
"""

from Backtracking.grafo import Grafo

def cumple_con_demanda(grafo: Grafo, w: dict):
    vert = grafo.obtener_vertices()

    S = 's' # Super fuente
    T = 'f' # Super sumidero
    grafo.agregar_vertice(S)
    grafo.agregar_vertice(T)

    demanda_total = 0

    for v in vert: #O(V)
        val = w.get(v, 0) # Si no está en w, asumimos 0 (neutro)
        if val > 0:
            grafo.agregar_arista(S, v, val)
        elif val < 0:
            demanda_total += -val
            grafo.agregar_arista(v, T, -val)

    # Suponiendo que tu función de flujo devuelve (flujo_maximo, red_residual)
    flujo_max, red_residual = flujo(grafo, S, T)

    return flujo_max == demanda_total