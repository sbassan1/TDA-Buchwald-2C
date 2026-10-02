"""
Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.
"""

def sumatorias_n(lista, n):
    if sum(lista) < n:
        return []

    combinaciones = []
    sumatorias_n_rec(lista, 0, n, [], combinaciones)
    return combinaciones

def sumatorias_n_rec(lista, i, n, sol_actual, combinaciones):
    suma_actual = sum(sol_actual)

    if suma_actual == n:
        combinaciones.append(sol_actual.copy())
        return

    if suma_actual > n or i == len(lista):
        return

    if suma_actual + sum(lista[i:]) < n:
        return

    sol_actual.append(lista[i])
    sumatorias_n_rec(lista, i + 1, n, sol_actual, combinaciones)
    sol_actual.pop()
    sumatorias_n_rec(lista, i + 1, n, sol_actual, combinaciones)

# Prueba:
print(sumatorias_n([1, 1, 1, 2, 3], 3))
# Salida esperada: [[1, 1, 1], [1, 2], [1, 2], [3]]
