"""
Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima? Justificar
"""


def min_cant_faros(matriz):
    n = len(matriz)
    m = len(matriz[0])

    # Corrección limpia para la matriz de booleanos:
    iluminadas = [[False for _ in range(m)] for _ in range(n)]

    faros = []

    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 1 and not iluminadas[i][j]:
                
                faro_i = min(i + 2, n - 1)
                faro_j = min(j + 2, m - 1)
                
                faros.append((faro_i, faro_j))

                # Iluminar en radio de dos 
                for r in range(max(0, faro_i - 2), min(n, faro_i + 3)):
                    for c in range(max(0, faro_j - 2), min(m, faro_j + 3)):
                        iluminadas[r][c] = True

    return faros
