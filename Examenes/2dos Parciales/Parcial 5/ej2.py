"""
Un plan de piso consiste de n interruptores y n luces con sus ubicaciones. Además, un diseño de iluminación es una asignación de interruptores y luces (qué luces controla cada interruptor). Un plan de piso es ergonómico si para él existe al menos un diseño de iluminación ergonómico. Que un diseño sea ergonómico significa que, para cada interruptor de luz que haya, este maneje una única luz (lámpara, lamparita, etc.), y esa luz sea además visible desde el lugar donde está el interruptor. En los ejemplos del dorso de este enunciado, el ejemplo de la izquierda es ergonómico, pero el de la derecha no. Implementar, utilizando redes de flujo, un algoritmo ergonomicidad(interruptores, luces) que permita determinar si el plan es ergonómico, o no. En caso que lo sea, devolver las asignaciones de (interuptor, luz) que correspondan. Suponer que existe una función visible(interruptor, luz) que determina si la luz es visible desde el interruptor, y que dicha función ejecuta en tiempo constante.Indicar y justificar la complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo.
"""

"""
Tenemos:

- Set de N interruptores
- Set de N luces
- Diseño de iluminacion que asigna interruptores con luces

Piden encontrar un diseño ergonomico:
- Cada interruptor controla una sola luz
- La luz es visible desde el lugar donde esta el interruptor

Nos piden hacer un algoritmo de red de flujo que nos diga si tenemos es posible encontrar un diseño economico con un diseño de iluminacion y si lo es que interruptores correponden a cada luz.

Nos dan una funcion visible(interruptor, luz) que da vewrdadero si la luz es visible desde el intrruptor

Modelemos una red:

Tenemos un vertice fuente, desde el tendremos aristas de peso 1 a N interruptores, estos tienen aristas hacia vertices luces que están conectadas conforme a dos condiciones:

- El interruptor tiene asignado esa luz
- El visible(interruptor, luz) es verdadero

Si ambas cumplen entonces habra una arista (interruptor, luz, 1) que representará una posible conexion, de allí todas las luces conectan con el sumidero con peso 1.

Para saber si existe un diseño de iluminacion ergonomico, el flujo que pasa por el vertice 't' debe ser == N
"""

from Backtracking.grafo import Grafo

def ergonomicidad(interruptores, luces):
    if len(interruptores) != len(luces):
        return {}

    red = Grafo(True, [])
    s = 's'
    t = 't'

    red.agregar_vertice(s)
    red.agregar_vertice(t)

    for luz in luces:
        v_luz = ('luz', luz)
        red.agregar_vertice(v_luz)
        red.agregar_arista(v_luz, t, 1)

    for interruptor in interruptores:
        v_interruptor = ('interruptor', interruptor)
        red.agregar_vertice(v_interruptor)
        red.agregar_arista(s, v_interruptor, 1)

        for luz in luces:
            v_luz = ('luz', luz)
            if visible(interruptor, luz): 
                red.agregar_arista(v_interruptor, v_luz, 1)

    valor_flujo, dic_flujos = flujo_maximo(red, s, t)

    if valor_flujo != len(interruptores):
        return {} # No es posible obtener un diseño ergonómico

    asignaciones = {}

    for interruptor in interruptores:
        v_interruptor = ('interruptor', interruptor)
        for v_luz in red.adyacentes(v_interruptor):
            if dic_flujos.get((v_interruptor, v_luz), 0) == 1:
                asignaciones[interruptor] = v_luz[1] # v_luz[1] es la luz original

    return asignaciones
