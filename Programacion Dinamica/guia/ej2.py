"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.
"""

import bisect

# Charlas : (inicio, fin, valor)
def schedule(charlas):
    if not charlas:
        return [], 0

    n = len(charlas)
    arr = sorted(charlas, key=lambda x: x[1])

    # Extraemos las horas de fin para usar búsqueda binaria (bisect)
    fines = [c[1] for c in arr]

    # p[i] guardará el índice de la última charla compatible que termina antes o a la vez
    # que comienza la charla i-ésima.
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        inicio_actual = arr[i - 1][0]
        # CORRECCIÓN 2: Búsqueda binaria para encontrar el último compatible (en vez de asumir arr[i+1])
        p[i] = bisect.bisect_right(fines, inicio_actual)

    # dp[i] = máxima ganancia considerando las primeras i charlas
    dp = [0] * (n + 1) # Maximizacion hasta la charla i

    for i in range(1, n + 1):
        ganancia_actual = arr[i - 1][2]

        # CORRECCIÓN 3: Recurrencia correcta: incluir (valor + óptimo del compatible p[i]) vs excluir (dp[i-1])
        incluir = ganancia_actual + dp[p[i]]
        excluir = dp[i - 1]

        dp[i] = max(incluir, excluir)

    solucion = reconstruir_sol(arr, dp, p, n)
    return solucion, dp[n]

def reconstruir_sol(arr, dp, p, n):
    i = n
    sol = []
    while i > 0:
        incluir = arr[i - 1][2] + dp[p[i]]
        if dp[i] == incluir:
            sol.append(arr[i - 1])
            i = p[i]
        else:
            i -= 1

    sol.reverse()
    return sol
