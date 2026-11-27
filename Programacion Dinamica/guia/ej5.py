"""
Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. Pasar por un casillero determinado (i,j)(i,j) nos da una ganancia de Vi,j. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?
"""

"""
OPT(I,J) => {
    grilla[i][j]+ max(OPT(i+1,j),OPT(i,j+1)) : Si no estamos en un borde inferior o derecho
    grilla[i][j]+ OPT(i,j+1) : Si x == n
    grilla[i][j]+ OPT(i+1,j) : Si y == n
}
"""

def gananciaMax(arr):

    n = len(arr)
    m = len(arr[0])

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # Caso base: origen
            if i == 0 and j == 0:
                dp[i][j] = arr[i][j]
            elif i == 0:
                dp[i][j] = arr[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = arr[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = arr[i][j] + max(dp[i - 1][j], dp[i][j - 1])


    return dp[0][0], reconstruccion(arr,dp)


def reconstruccion(arr, dp):
    n = len(arr)
    m = len(arr[0])

    i, j = n - 1, m - 1
    sol = [(i, j)]

    # Nos devolvemos desde la meta (n-1, m-1) hasta el origen (0,0)
    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

        sol.append((i, j))

    sol.reverse()
    return sol
