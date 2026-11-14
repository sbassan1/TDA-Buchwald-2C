"""
El Lunático sigue con sus fechorías, y ha entrado en una antigua mansión para robar unas joyas. Después de encontrarlas, escucha que el jefe de guardia ha descubierto el robo y decide escapar. El jefe de guardia sabe en qué habitación se encuentra el ladrón, pero no sabe qué camino elegirá para salir de la mansión. La mansión tiene varios pasillos y puertas que conectan sus distintas habitaciones. El jefe de guardia cuenta con un listado de pasillos, zonas y habitaciones de la mansión, y otra de puertas y conexiones de un pasillo/zona/habitación a otro de estos, así como la habitación de las joyas. El ladrón puede elegir cualquier camino que lo lleve de la habitación de las joyas a la zona "exterior" de la mansión. El jefe de guardia dispone de suficientes guardias como para custodiar determinadas conexiones y/o puertas. Si una conexión o puerta está custodiada, el ladrón será atrapado necesariamente si intenta atravesarla. Un guardia puede custodiar cualquier conexión o puerta de manera indistinta, aunque cada guardia puede custodiar un máximo de una.

Utilizando redes de flujo, implementar una función custodia(lugares, puertas_conexiones, hab_joyas, zona_exterior) que determine qué puertas/conexiones debe custodiar el jefe de guardia para garantizar que el ladrón sea atrapado (no importa el camino que elija, incluso si fuera capaz de saber dónde están los guardias), utilizando la menor cantidad de guardias posibles (para no desorganizar el operativo de seguridad usual). Analizar la complejidad del algoritmo, en función de las variables del problema.
"""

"""
Para este problema nos piden encontrar el min-max cut de una red, en esta red las puertas/pasillos son las aristas, los lugares/habitaciones son los vertices y tenemos la "habitacion de joyas" como fuente y la "zona exterior" como sumidero.

Para modelar esta red debemos conectar cada cuarto con peso 1, y ya que estamos hablando de puertas podemos ir adentro y afuera, por lo que el grafo no sera direccionado.
"""

from Backtracking.grafo import Grafo

def custodia(lugares, puertas_conexiones, hab_joyas, zona_exterior):

    red = Grafo(False, [])
    S = zona_exterior
    T = zona_exterior
    red.agregar_vertice(S)
    red.agregar_vertice(T)

    for lugar in lugares:
        v_lugar = ('lugar', lugar)
        red.agregar_vertice(v_lugar)

    for (u,v) in puertas_conexiones:
        v_u = ('lugar',u)
        v_v = ('lugar',v)

        red.agregar_arista(v_u,v_v,1)
        v_aux = ('lugar_aux',u+v)
        red.agregar_arista(v_v,v_aux,1)
        red.agregar_arista(v_aux,v_u,1)

    _ , red_residual = flujo(red,S,T)

    alcanzables = set([hab_joyas])
    cola = deque([hab_joyas])

    # TODO Recordar esta parte bien para los futuros min-max cut!!!!
    while cola:
        actual = cola.popleft()
        for vecino in red_residual.adyacentes(actual):
            # Si hay capacidad residual positiva y no fue visitado
            if vecino not in alcanzables and red_residual.peso_arista(actual, vecino) > 0:
                alcanzables.add(vecino)
                cola.append(vecino)

    puertas_a_custodiar = []
    for u, v in puertas_conexiones:
        if (u in alcanzables and v not in alcanzables) or (v in alcanzables and u not in alcanzables):
            puertas_a_custodiar.append((u, v))

    return puertas_a_custodiar
