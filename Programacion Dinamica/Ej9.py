"""
Tenemos un conjunto de números v_1, v_2, …, v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o menor a un valor V, tratando de aproximarse lo más posible a V. Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. Indicar y justificar la complejidad del algoritmo implementado.
"""

def subset_sum(elementos, v):
    n = len(elementos)
    if v == 0 or n == 0:
        return []

    dp = [[0] * (v + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        elem = elementos[i - 1]
        for j in range(1, v + 1):
            if elem <= j:
                dp[i][j] = max(dp[i - 1][j], elem + dp[i - 1][j - elem])
            else:
                dp[i][j] = dp[i - 1][j]

    sol = []
    i, j = n, v
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            elem = elementos[i - 1]
            sol.append(elem)
            j -= elem
        i -= 1

    sol.reverse()
    return sol

"""
La complejidad del algoritmo es O(n*v) ya que iteramos por la cantidad de monedas y la cantidad de valor posible que podamos hallar
"""
