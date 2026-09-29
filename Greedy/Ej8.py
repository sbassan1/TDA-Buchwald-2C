"""
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):

    elementos = sorted(elementos, key=lambda x: x[0], reverse=True)
    peso_actual = 0
    valor_actual = 0

    solucion = []
    for elemento in elementos:
        if elemento[1] <= W - peso_actual:
            peso_actual += elemento[1]
            valor_actual += elemento[0]
            solucion.append(elemento)

    return solucion

"""
Este problema no puede ser resuelto de forma optima usando greedy ya que el problema es NP-hard. Existen estrategias para intentar acercarse a la solucion optima tal como:
    - Elegir el elemento de mayor valor en cada paso (La que elegi yo)
    - Elegir el elemento de menor peso en cada paso
    - Elegir el elemento de mayor (valor/peso) en cada paso
Pero ninguna asegura que sea una solucion optima que garantice el mayor valor posible. El algoritmo es greedy ya que elige desde un estado local de forma voraz con una estrategia sin memorizar o guardar estados pasados.
La complejidad de este algoritmo es O(n log n) ya que ordenamos la lista y luego iteramos por ella.
"""
