"""
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar, utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n. Indicar y justificar la complejidad del algoritmo implementado.
Ejemplos:
    n = 0 --> Debe devolver 1 (no moverse)
    n = 1 --> Debe devolver 1 (paso de 1)
    n = 2 --> Debe devolver 2 (dos pasos de 1, o un paso de 2)
    n = 3 --> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
    n = 4 --> Debe devolver 7
    n = 5 --> Debe devolver 13
"""

"""
rec(i) == {

rec[0] = 1
rec[1] = 1
rec[2] = 2
else => rec[i] = rec[i-1] + rec[i-2] + rec[i-3]
}

Complejidad espacial : O(n)
Complejidad temporal : O(n)
"""


def escalones(n):

    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]
