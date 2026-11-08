
"""
Alan y Bárbara están conviviendo en conjunto con n−2 amigos (es decir, son n personas conviviendo). Deben organizar quién cocinará cada una de las próximas n cenas (una persona debe cocinar sí o sí cada día obviamente no tiene que ser siempre la misma). Hay que considerar que cada persona desea cocinar a lo sumo 2 noches de estas n, y que cada uno de ellos tiene planes que pueden hacer que algunas noches no puedan encargarse de la cena. Contando con la información de quién puede cada noche, ¿es posible asignar un encargado/a de la cocina para cada una de las noches, sin que nadie cocine más de 2 de estas? ¿Cómo? 

Implementar un algoritmo que, utilizando redes de flujo resuelva el problema (determine si se puede hacer una asignación, y si es así que nos indique tal asignación). Indicar y justificar la complejidad del algoritmo implementado en las variables del problema.

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

"""
Restricciones:

- Son n personas de las cuales debemos organizar quienes cocinan n cenas. (Una personas debe cocinar si o si cada dia, no puede ser la misma).
- Cada persona desea cocinar a lo sumo 2 noches de estas n y que cada uno tiene planes que pueden que una noche no puedan engargarse de la cena.

Tenemos: 
- Un diccionario de personas con los dias que estan libres (para hacermela más simple en vez de tomar los ocupados y hacer complemento) dict[persona] = [dias] \in {0,..,n-1}.

Voy a pensarlo de esta forma, tenemos una red con:

- Un vertice fuente 's' y un sumidero 't'. 
- El vetice 's' tiene conecta con una arista a cada vertice persona con capacidad 2.
- Cada vertice persona se conecta a un vertice día correspondiente con los dias libres que tiene con capacidad 1 (ya que solo pueden cocinar un dia)
- Cada vertices dia se conecta con una arista al sumidero con capacidad 1 (Ya que solo una persona va a cocinar)

Debemos averiguar si:
- El flujo total que llega a 't' es n. (Todos los días alguien cocina), si el flujo no es 'n' entonces no es posible asignar con las restricciones y devuelvo {}.
- Si el flujo es igual a n, entonces debemos reconstruir persona por persona cual dia cocina y lo guardamos en un nuevo diccionario persona -> [dia].

"""

from Backtracking.grafo import Grafo

# dias_libres, es un diccionario de Personas -> [Dias] // El día 
from Backtracking.grafo import Grafo

def quien_cocina(dias_libres, n):

    red = Grafo(dirigido=True)
    s = 's'
    t = 't'
    red.agregar_vertice(s)
    red.agregar_vertice(t)

    dias_agregados = set()

    for persona in dias_libres.keys():
        v_per = ('persona', persona)
        red.agregar_vertice(v_per)
        red.agregar_arista(s, v_per, peso=2)

        for dia in dias_libres[persona]:
            v_dia = ('dia', dia)
            if dia not in dias_agregados:
                dias_agregados.add(dia)
                red.agregar_vertice(v_dia)
                red.agregar_arista(v_dia, t, peso=1)

            red.agregar_arista(v_per, v_dia, peso=1)


    red_flujo = flujo(red, s, t)

    if flujo_total != n:
        return {}

    asignaciones = {}

    for persona in dias_libres.keys():
        v_per = ('persona', persona)
        asignaciones[persona] = []

        for dia in dias_libres[persona]:
            v_dia = ('dia', dia)
            if red_flujo.get((v_per, v_dia), 0) == 1:
                asignaciones[persona].append(dia)

    return asignaciones