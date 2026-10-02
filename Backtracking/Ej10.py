"""
Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. ¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?
"""

def sumatoria_dados(n, s):
    if s < n or s > n * 6:
        return []

    resultados = []
    sumatoria_dados_rec(n, s, 0, [], resultados)
    return resultados

def sumatoria_dados_rec(n, s, suma_actual, solucion_actual, resultados):
    if len(solucion_actual) == n:
        if suma_actual == s:
            resultados.append(solucion_actual.copy())
        return

    if suma_actual > s:
        return

    dados_restantes = n - len(solucion_actual)
    if suma_actual + (6 * dados_restantes) < s:
        return

    for num in range(1, 7):
        solucion_actual.append(num)
        sumatoria_dados_rec(n, s, suma_actual + num, solucion_actual, resultados)
        solucion_actual.pop()


print(sumatoria_dados(2, 7))
# Output: [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]
