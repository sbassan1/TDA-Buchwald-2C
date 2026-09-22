"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla
tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un
arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla,
e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad
del algoritmo implementado.
"""



def buscar_ultimo_compatible(charlas, inicio):
    izq = 0
    der = len(charlas) - 1
    indice = -1

    while izq <= der: # O(log n)
        medio = (izq + der) // 2
        if charlas[medio][1] <= inicio:
            indice = medio
            izq = medio + 1
        else:
            der = medio - 1

    return indice + 1


def scheduling(charlas):

    if not charlas:
        return 0, []

    charlas = sorted(charlas, key=lambda x: x[1]) # O(n log n)

    n = len(charlas)
    mem = [0] * (n + 1)     # mem[i]: valor maximo de charlas de 0 hasta i
    padre = [0] * (n + 1)   # padre[i]: indice de última charla compatible con i

    for i in range(1, n + 1): # O(n) * O(log n) ==> O(n log n)
        inicio_i, fin_i, valor_i = charlas[i - 1]
        padre[i] = buscar_ultimo_compatible(charlas[:i-1], inicio_i)

        mem[i] = max(mem[i - 1], valor_i + mem[padre[i]])


    charlas_elegidas = []
    i = n
    while i > 0:    # O(n)
        inicio_i, fin_i, valor_i = charlas[i - 1]

        if valor_i + mem[padre[i]] >= mem[i - 1]:
            charlas_elegidas.append(charlas[i - 1])
            i = padre[i]
        else:
            i -= 1

    charlas_elegidas.reverse() # O(n)

    return charlas_elegidas

"""
El algoritmo de encontrar la maxima ganancia tiene una complejidad de O(n log n) debido a la ordenación de las charlas
y la búsqueda binaria para encontrar la última charla compatible.

El algoritmo de reconstrucción de la solución tiene una complejidad de O(n) debido a la recorrida hacia atrás a través de la memoria.

Por lo tanto, el algoritmo de scheduling tiene una complejidad total de O(n log n) + O(n) ==> O(n log n).

La complejidad espacial es de O(n), ya que guardamos en mem y padre los valores de 0 hasta n y las charlas elegidas seran como mucho O(n).
"""
