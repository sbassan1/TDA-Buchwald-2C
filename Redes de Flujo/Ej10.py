
"""
Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G. Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. ¿Cuál es la complejidad temporal de la solución implementada? ¿Cómo resolverías el problema si el grafo fuera no dirigido?

Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp) ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

La función flujo recibe la red de transporte (debe cumplir con las propiedades de red de transporte), la fuente y el sumidero, en ese orden. Devuelve un diccionario Arista -> flujo.

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

from ff import flujo
from grafo import Grafo

def disjuntos(grafo, s, t):

    vert = grafo.obtener_vertices()
    red = Grafo(True, vert)

    for v in vert: # O(V + E)
        for w in grafo.adyacentes(v):
            red.agregar_arista(v, w, 1)

    flujos = flujo(red, s, t) # O(V + E^2)
    lista_caminos = []
    
    aristas_cubiertas = set()

    # Toda la reconstruccion nos da O(V^3) pero en la realidad si tenemos en la primera iteracion V vertices entonces habra V caminos de longuitud 1 
    # No estoy del todo seguro pero creo que por eso amortiguaría a O(V^2)
    for vecino in red.adyacentes(s): # O(V)
        primera_arista = (s, vecino)
        
        if flujos.get(primera_arista, 0) == 1 and primera_arista not in aristas_cubiertas:
            camino = [s, vecino]
            aristas_cubiertas.add(primera_arista)
            vertice_actual = vecino

            while vertice_actual != t: # O(V) como mucho

                siguiente = None # Lo marco como none, pero si el flujo es correcto siempre tendra camino si el grafo esta conectado

                for vecino_sig in red.adyacentes(vertice_actual): # O(V)
                    arista = (vertice_actual, vecino_sig)

                    if flujos.get(arista, 0) == 1 and arista not in aristas_cubiertas:
                        siguiente = vecino_sig
                        aristas_cubiertas.add(arista)
                        break
                
                camino.append(siguiente)
                vertice_actual = siguiente

            if vertice_actual == t:
                lista_caminos.append(camino)

    # devolver una lista en la cual cada elemento es una lista, con el camino
    # entre s y t. Todos esos caminos deben incluir inicio (s) y fin (t).
    return lista_caminos

    # Complejidad Temporal: O(V + E^2) + O(V^2)

"""
Nos piden encontrar la maxima numero de caminos disjuntos de un grafo dirigido usando redes de flujo. Para ello modelaremos el problema de la siguiente manera, cada arista tendra un peso de 1

Nuestra estrategia será, con esta red de flujo, realizar el algoritmo de ford-fulkerson desde s a t. Tendremos una red de flujo maximo de s a t, donde el flujo a t será maximizado. 

Cada camino a t de s, será un camino disjunto, ya que solamente por cada arista puede pasar un flujo de 1. De tal modo que al conseguir el flujo usando flujo(red,s,t), obtendremos el diccionario de flujos que pasa por cada arista y lo unico que tendremos que hacer es reconstruir cada camino y guardarlo con el fin de evitar guardar el mismo camino más de una vez.

- Iteraremos sobre cada arista (v,t) conectada a el sumidero t, creando una por cada camino:
    1. Si la arista (v,t) tiene flujo 1, entonces es parte de un camino y la guardaremos en la lista
    2. Buscaremos en los adjacentes al vetice 'v' y guardaremos la arista (v',v) con flujo 1
    3. Repetimos el proceso anterior hasta que (s,v), y creamos una nueva lista con el siguiente arista conectada a t  

Si el grafo no fuese dirigido entonces deberíamos crear una arista de ida y vuelta para cada arista (u,v) con peso 1, el algoritmo de flujo encontraría los caminos como antes, pero si toma una arista (v,u) ya existiendo una (u,v) entonces lo verá como un retroceso del flujo y no pasara flujo de ese lado luego.
"""