"""
Tito trabaja para la mafia. Debe llevar en camiones de caudales el dinero recaudado por la organización a modo de devolver favores a diferentes estaciones de policía. Entre diferentes rutas puede tener que cambiar de camión (para no ser fácilmente detectado), donde cada camión puede tener diferente capacidad. Además, en algunos puntos (escondites de la mafia) puede recoger más dinero. Tito entonces cuenta con un grafo dirigido con las diferentes rutas, y puntos donde pueda tener que ir cambiando de camión según como cambie de ruta. El grafo es pesado y las aristas tienen como peso la capacidad del camión de caudales a usar por esa ruta. En cada vértice tenemos un punto donde podría (o no) poder recoger dinero o tener que dejar un agradecimiento, lo cual está modelado con un valor w(v) (si es positivo, al pasar por allí podemos recoger dinero, si es negativo es que debemos dejar un agradecimiento, si es 0, es simplemente un punto de cambio de camión y nada más). Tito puede comenzar cada recorrido desde donde desee, si bien tiene sentido ir empezando desde algún escondite. Usando redes de flujo, implementar un algoritmo que reciba dicho grafo y determine si es posible pagar todos los agradecimientos correspondientes. No es necesario indicar cómo serían los recorridos. Indicar y justificar la complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo
"""


"""
Intentaré modelar la red con esta representacion:

Tendremos vertices fuente, sumidero y puntos de oferta/demanda/neutros.

- Los puntos de oferta y demanda son los vertices (que no son fuente y sumidero) donde los camiones deben pagar o depositar dinero.
- Las aristas representan la capacidad de camion en la cual transportan dinero

Tendremos una superfuente y un super sumidero donde conectaremos con pesos los valores para que en el trancurso Tito pague o reciba dinero, de tal modo que por cada vertice oferta (recibe dinero) tendremos una arista con peso correspondiente a la cantidad de dinero recibido, y en cada vertice demanda tendremos una arista al super sumidero que indicará cuanto dinero deberán depositar.

Esto funciona ya que:
- Si tenemos aristas oferta para los vertices de oferta entonces cuando usemos un camion que le falte dinero el algoritmo llevará dinero de las aristas oferta para rellenar la capacidad que falte
- Si tenemos que pagar, como tenemos aristas que van de vertices demandas a super sumideros, entonces tendremos que llevar un poco del dinero por ellos, ya que es el camino más corto


"""


def verificar_pagos_mafia(grafo_original, w):

    S = "SuperFuente"
    T = "SuperSumidero"
    
    grafo_original.agregar_vertice(S)
    grafo_original.agregar_vertice(T)
    
    demanda_total = 0

    for v in vertices:
        red.agregar_vertice(v)

    for vert in grafo_original.obtener_vertices():
        val = w.get(vert, 0)

        if val < 0:
            demanda_total += -val
            grafo_original.agregar_arista(vert, T, -val) # Valor va a ser negativo, asi que lo damos vuelta 
        elif val > 0:
            grafo_original,agregar_arista(S,vert, val)


    flujo = flujo(grafo_original,S,T)

    return flujo[T] > demanda_total