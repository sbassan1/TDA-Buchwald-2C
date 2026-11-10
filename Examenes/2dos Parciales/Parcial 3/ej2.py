
"""
Para poder cortar con el juego del rival, Scaloni cuenta con información precisa minuto a minuto. En un momento dado, tiene la información perfecta de qué jugador puede darle un pase a cuál otro (independientemente de quién tenga la pelota) o marcar un gol. 

Scaloni quiere saber a qué jugador, o jugadores, es indispensable marcar para evitar que nos marquen un gol. Suponiendo que una jugada arranca en el arquero contrario, y que se tiene la información de qué jugador de ese equipo puede pasarle la pelota a cuál/es otro/s (incluyendo al arquero), considerando que esto no es necesariamente recíproco (no todos los jugadores pueden hacer los mismos pases o goles, ¿o vos podés dar los mismos pases que Messi?), y cuáles jugadores podrían marcar un gol en ese momento, indicar cuáles son los mínimos jugadores contrarios a marcar de tal forma que no sea posible que nos marquen un gol (no podemos marcar al arquero). 

Resolver este problema utilizando redes de flujo. Pueden suponer que la función flujo(red, s, t) les devuelve tanto la asignación de flujo a cada arista, como también la Red Residual resultante de aplicar el algoritmo de Ford-Fulkerson. Indicar y justificar la complejidad del algoritmo planteado. Para todo el problema, considerar que, si bien hay un único arquero, podrían haber n jugadores de campo (simplemente para no quedarse con que son 10 nada más).
"""


"""
El problema nos pide encontrar cual es la minima cantidad de jugadores a marcar tal que no sea posible que la pelota llegue del arquero rival al nuestro.

De tal forma que si representamos a los jugadores como vertices y las aristas como "se la pasa a" tendremos un grafo. Pero si queremos el corte minimo con fork fulkerson, utilizando ese modelo nos dará que pases debemos cortar para que no hagan gol, no cuales jugadores. De modo que por cada jugador vertices deberemos dividirlo en dos, un vertice jugador in y otro out, esto nos permite tener una arista (V_in, V_out, 1) que represente al jugador con la pelota.

Utilizando esto creamos un modelo para la red:
- El arquero rival tiene su arista interna in->out con peso de 'inf' ya que no podremos sacarle la pelota. Su rol sera de fuente en nuestra red.
- Por cada jugador del arquero_out nos conectaremos a vertices jugadores_in con peso 1, para simbolizar pases. Y entre ellos lo mismo.
- Si existe vertices que hacen pase de ida y vuelta entre dos jugadores, separaremos una arista con un vertice para cumplir con la condicion de red. (Si separamos jugador con dos vertices es necesario???)
- Repitiremos asignando pesos entre jugador_out -> jugador_in, hasta llegar a nuestro arquero que en nuestro modelo funciona como sumidero.
- Con esto tendremos una red de flujo que nos permitirá averiguar cual es el corte minimo.

Vamos a tener como entrada un diccionario de jugadores donde cada key es el 'id' del jugador y su valor es una lista de jugadores de los cuales éste hará un pase.
Como salida tendremos una lista de 'caminos' con jugadores que debemos marcar.
"""

from Backtracking.grafo import Grafo

# voy a hacer la suposicion de que sabemos que la key del arquero rival es 'arquero_rival' y nuestro arquero como 'arquero_arg'

def red_pases(jugadas):
    red = Grafo(True, [])

    # Crear los vértices in y out de jugadores y arquero y las aristas 
    for jugador in jugadas.keys():
        if jugador == 'arquero_arg':
            v_arg = ('v_in', jugador)
            red.agregar_vertice(v_arg)
            continue

        v_in = ('v_in', jugador)
        v_out = ('v_out', jugador)
        red.agregar_vertice(v_in)
        red.agregar_vertice(v_out)

        if jugador == 'arquero_rival':            
            red.agregar_arista(v_in, v_out, float('inf'))
        else:
            red.agregar_arista(v_in, v_out, 1)

    # Agregamos los pases de jugadores
    for jugador in jugadas.keys():
        for pase in jugadas[jugador]:
            red.agregar_arista(('v_out', jugador), ('v_in', pase), 1)

    # Creamos el flujo y la red residual
    fuente = ('v_in', 'arquero_rival')
    sumidero = ('v_in', 'arquero_arg')
    flujo_red, red_res = flujo(red, fuente, sumidero)

    visitados = set()
    cola = [fuente]
    visitados.add(fuente)

    while cola:
        actual = cola.pop(0)
        for vecino in red_res.adyacentes(actual):
            if vecino not in visitados and red_res.obtener_peso(actual, vecino) > 0: # Si el vecino in esta en la red
                visitados.add(vecino)
                cola.append(vecino)

    caminos_res = []

    for jugador in jugadas.keys():
        if jugador in ('arquero_rival', 'arquero_arg'):
            continue
        
        v_in = ('v_in', jugador)
        v_out = ('v_out', jugador)

        # Buscamos los jugadores de los cuales en la red residual se corta la capacidad (ya que entro flujo y no salio)
        if v_in in visitados and v_out not in visitados:
            caminos_res.append(jugador)

    return caminos_res