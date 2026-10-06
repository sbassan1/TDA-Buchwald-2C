"""
Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. Tener en cuenta que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia.
"""


"""
La complejidad del algoritmo es O(n*m) === O(n) + O(m) + O(n*n) + O(n+m)
La complejidad espacial es O(n*m) y

Si existen obstaculos que detectamos deberemos guardar el estado actual y ir por abajo o la derecha en busca de un camino al rededor. dp[i+1][j] ó dp[i][j+1]
"""

def laberinto(matriz):
    if not matriz or not matriz[0]:
        return 0, []

    n = len(matriz)
    m = len(matriz[0])

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = matriz[0][0]

    # Lleno los bordes
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + matriz[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]

    # Lleno la tabla por adentro
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = matriz[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    camino = []
    i, j = n - 1, m - 1
    camino.append((i, j))

    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            # Si la casilla de arriba es mejor que la otra
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        camino.append((i, j))

    camino.reverse()

    return dp[n - 1][m - 1]
