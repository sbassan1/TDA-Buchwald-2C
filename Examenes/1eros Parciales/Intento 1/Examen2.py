"""
#Ejercicio 1:
    Implementar una función que, dado un arreglo ordenado y sin repetidos de valores enteros no negativos, obtenga el mínimo valor que no se encuentre en el arreglo. Indicar y justificar adecuadamente la complejidad del algoritmo.

    Por ejemplo:
        minimoExcluido([0, 1, 5]) --> 2
        minimoExcluido([1, 3, 5]) --> 0
        minimoExcluido([0, 1, 2, 3, 4, 5]) --> 6
        minimoExcluido([0, 1, 2, 3, 4, 5, 1234567]) --> 6
"""

# Si todos los elementos estan en orden, si el elemento <= indice, entonces hay que buscar adelante  
# Caso contrario atras, y si tenemos inicio == fin, entonces devolvemos inicio + 1, ya que es el ultimo
# Salvo por el caso donde falte 0, 

def ej1(arr, inicio, fin):
    # Si el elem es >= al fin
    if arr[fin] == fin:
        return fin + 1
    # Si el elem es mayor al indice inicio 
    if arr[inicio] > inicio:
        return inicio

    mid = (inicio + fin) // 2

    if arr[mid] == mid:
        return ej1(arr, mid + 1, fin)
    return ej1(arr, inicio, mid)

"""
# Solucion 1:
    T(n) = 1 T(n/2) + O(1) ==> a = 1 , b = 2, c = 0.
    c = 0 === log2 1 = 0, estamos en el 2do caso del teorema maestro ==> O(n^(log2 1) log n) = O(log n)
"""

"""
# Ejercicio 2:
    Dado un grafo sin ciclos (un bosque, el cual es necesariamente bipartito), implementar un algoritmo greedy que obtenga el matching máximo. Es decir, el subconjunto máximo de aristas tal que ninguna arista comparta vértice entre sí. Indicar y justificar la complejidad del algoritmo. El análisis de la complejidad debe estar completo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.
"""

def matching_maximo_bosque(grafo):
    usados = set()           # vértices ya apareados
    matching = []            # aristas elegidas
    
    for v in grafo.obtener_vertices(): #O(V)
        if v not in usados:
            for w in grafo.adyacentes(v):
                if w not in usados:
                    matching.append((v, w))
                    usados.add(v)
                    usados.add(w)
                    break              # v ya está apareado, pasar al siguiente vértice
    return matching



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
Donde i es la menor cantidad de pasos hasta el array i
OPT(i) = {
    Min(OPT(i+1)+1,OPT(i+2)+1,..,OPT(i+n)+1) : Para todo n en {1,..,arr[i]}
}
"""

def ej4(lista):

    n = len(lista)
    dp = [float('inf')] * n

    dp[0] = 1

    for i in range(n):
        pasos = []
        for j in range(lista[i]):
            if i+j < n:
                pasos.append(dp[i+j]+1)
        dp[i] = min(pasos)

    return dp

def ej4(lista):
    n = len(lista)

    if n == 0:
        return 0, []

    dp = [float("inf")] * n
    siguiente = [-1] * n
    dp[n - 1] = 0

    # De derecha a izquierda
    for i in range(n - 2, -1, -1):
        # Destino es i + lista[i] + 1
        for destino in range(i + 1, min(n, i + lista[i] + 1)):
            candidato = dp[destino] + 1

            if candidato < dp[i]:
                dp[i] = candidato
                siguiente[i] = destino

    if dp[0] == float("inf"):
        return float("inf"), []

    # Reconstrucción
    camino = [0]
    i = 0

    while i != n - 1:
        i = siguiente[i]

        if i == -1:
            return float("inf"), []

        camino.append(i)

    return dp[0], camino