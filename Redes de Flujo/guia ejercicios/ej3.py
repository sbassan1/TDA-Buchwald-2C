"""
Dada una red y un diccionario que representa los valores de los flujos para las aristas, todos valores que respetan la restricción de cada arista, construir la red residual que refleja el estado actual de la red en función a los valores de flujo dados.
"""

from Backtracking.grafo import Grafo


def construir_red_residual(red, flujos):
    red_residual = Grafo(dirigido=True)
    
    for v in red.obtener_vertices():
        red_residual.agregar_vertice(v)
        
    for v in red.obtener_vertices():
        for w in red.adyacentes(v):
            capacidad = red.peso_arista(v, w)
            # Obtenemos el flujo actual para la arista (v, w). Si no está, es 0.
            flujo = flujos.get((v, w), 0)
            
            capacidad_residual_fwd = capacidad - flujo
            if capacidad_residual_fwd > 0:
                if red_residual.estan_unidos(v, w):
                    peso_actual = red_residual.peso_arista(v, w)
                    red_residual.agregar_arista(v, w, peso_actual + capacidad_residual_fwd)
                else:
                    red_residual.agregar_arista(v, w, capacidad_residual_fwd)
            
            capacidad_residual_bwd = flujo
            if capacidad_residual_bwd > 0:
                if red_residual.estan_unidos(w, v):
                    peso_actual = red_residual.peso_arista(w, v)
                    red_residual.agregar_arista(w, v, peso_actual + capacidad_residual_bwd)
                else:
                    red_residual.agregar_arista(w, v, capacidad_residual_bwd)
                    
    return red_residual