"""
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

Ejemplo:
Para: [100, 5, 50, 1, 1, 200]
Devolver: [0, 2, 5]
"""

"""
Complejidad temporal = O(n) + O(n) ==> O(N)

rec(n) = {
n == 0: []
n == 1: [0]
else => max(trabajos[n] + trabajos[n-2], trabajos[n-1])
}

"""

def juan_el_vago(trabajos):

    n = len(trabajos)
    if n == 0:
            return []
    if n == 1:
        return [0]

    dp = [0] * n
    dp[0] = trabajos[0]
    dp[1] = max(trabajos[0], trabajos[1])

    for i in range(2, n):
        dp[i] = max(trabajos[i] + dp[i - 2], dp[i - 1])

    sol = []
    i = n - 1
    while i >= 0:

        # Casos Base
        if i == 0:
            sol.append(0)
            break

        elif i == 1:
            if trabajos[1] > trabajos[0]:
                sol.append(1)
            else:
                sol.append(0)
            break

        # Caso Inductivos
        if trabajos[i] + dp[i - 2] >= dp[i - 1]:
            sol.append(i)
            i -= 2
        else:
            i -= 1

    sol.reverse()
    return sol
