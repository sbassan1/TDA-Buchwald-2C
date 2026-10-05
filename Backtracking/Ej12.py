"""
Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.
"""

def sumatorias_n(lista, n):
    max_sol = []
    sumatorias_n_rec(lista, 0, n, [], max_sol)
    return max_sol


def sumatorias_n_rec(lista, i, n, sol_actual, max_sol):
    suma_local = sum(sol_actual)

    if suma_local > n:
        return False

    if suma_local > sum(max_sol):
        max_sol.clear()
        max_sol.extend(sol_actual)

    if suma_local == n:
        return True

    if i == len(lista):
        return False

    sol_actual.append(lista[i])
    encontrado = sumatorias_n_rec(lista, i + 1, n, sol_actual, max_sol)
    sol_actual.pop()
    if encontrado:
        return True
    return sumatorias_n_rec(lista, i + 1, n, sol_actual, max_sol)
