"""
#Ejercicio 1:
    Implementar una función que, dado un arreglo ordenado y sin repetidos de valores enteros no negativos, obtenga el mínimo valor que no se encuentre en el arreglo. Indicar y justificar adecuadamente la complejidad del algoritmo.

    Por ejemplo:
        minimoExcluido([0, 1, 5]) --> 2
        minimoExcluido([1, 3, 5]) --> 0
        minimoExcluido([0, 1, 2, 3, 4, 5]) --> 6
        minimoExcluido([0, 1, 2, 3, 4, 5, 1234567]) --> 6
"""

# Son todos valores mayores a 0, ordenados y

def minimoExcluido_recursivo(arr,inicio,fin):

    if inicio+1 == fin:
        if inicio+1 == 1:
            return 0
        else:
            return arr[inicio] + 1

    mitad = (inicio + fin) // 2

    if arr[mitad] > mitad:
        return minimoExcluido_recursivo(arr, inicio, mitad)
    else:
        return minimoExcluido_recursivo(arr, mitad, fin)

def minimoExcluido(arr):
    if not arr:
        return None

    return minimoExcluido_recursivo(arr, 0, len(arr))

"""
# Solucion 1:
    T(n) = 1 T(n/2) + O(1) ==> a = 1 , b = 2, c = 0.
    c = 0 === log2 1 = 0, estamos en el 2do caso del teorema maestro ==> O(n^(log2 1) log n) = O(log n)
"""

"""
# Ejercicio 2:
    Dado un grafo sin ciclos (un bosque, el cual es necesariamente bipartito), implementar un algoritmo greedy que obtenga el matching máximo. Es decir, el subconjunto máximo de aristas tal que ninguna arista comparta vértice entre sí. Indicar y justificar la complejidad del algoritmo. El análisis de la complejidad debe estar completo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.
"""



"""
# Ejercicio 3:
    Un PathSelection de un grafo dirigido G y un conjunto de caminos P1, P2, ..., Pc, es un subconjunto de dichos caminos tal que ninguno de ellos compartan ningún nodo entre sí. Implementar un algoritmo que dado obtenga el PathSelection más grande posible de un Grafo y un conjunto de caminos dado. Obviamente, implementarlo con un algoritmo por bactracking (si te sale hacerlo polinomial con otra técnica, te aseguramos el 10 en la materia, pero no te prometemos darte nada del millón de dólares).
"""

def PathSelection_rec(caminos, i, solucion):
    if i == len(caminos):
        return len(solucion)

    # Ver si el camino actual es elegible a ser agregado a la solucion
    # O(N^2)
    nodos_usados = {nodo for camino in solucion for nodo in camino}
    elegible = not any(nodo in nodos_usados for nodo in caminos[i])

    if elegible:
        # Concatenar [caminos[i]] crea una copia nueva sin alterar 'solucion'
        opcion_incluir = PathSelection_rec(caminos, i + 1, solucion + [caminos[i]])
        opcion_excluir = PathSelection_rec(caminos, i + 1, solucion)
        return max(opcion_incluir, opcion_excluir)
    else:
        return PathSelection_rec(caminos, i + 1, solucion)


def PathSelection(grafo, caminos):
    return PathSelection_rec(caminos, 0, [])



"""
# Ejercicio 4:
    Dado un arreglo de números positivos, donde cada elemento representa el máximo número de pasos que podemos dar desde esa posición, implementar un algoritmo que, utilizando programación dinámica determine la menor cantidad de saltos a realizar para llegar al final del arreglo (comenzamos en la posición 0). También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado.

    Por ejemplo, si el arreglo es [2, 3, 1, 1, 4], la solución óptima es ir desde la posición 0 a la posición 1 (saltando 1 lugar, teniendo máximo 2 desde el inicio), y de allí a la posición 4 (saltando 3 lugares, que es el máximo desde dicha posición), logrando llegar al final en 2 saltos.
"""
"""
arr(i) = {
    Si arr(n) == 0
    Si no:
        arr(i) == min(arr[i-1],arr[arr[i]],arr[arr[i]-1],arr[arr[i]-2],...,arr[arr[i]-m])
}
"""

def saltos_minimos(arr):
    if not arr:
        return 0, []

    n = len(arr)

    mem = [float('inf')] * n
    mem[0] = 0  # Caso base

    # padre[i] guardará desde qué índice j saltamos hacia i
    padre = [-1] * n

    for i in range(n):
        if mem[i] == float('inf'):
            continue

        max_pasos = arr[i]

        # Probamos todos los saltos posibles desde la posición i
        for salto in range(1, max_pasos + 1):
            j = i + salto
            if j < n and mem[i] + 1 < mem[j] :
                mem[j] = mem[i] + 1
                padre[j] = i

    camino = []
    actual = n - 1
    if mem[n - 1] == float('inf'):
        return -1, []
    while actual != -1:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()  # Invertimos para que quede de inicio a fin

    return mem[n - 1], camino
