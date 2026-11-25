
"""
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
OPT(i) = {
    Max(arr[i] + OPT(i+2), OPT(i+1))
}
"""

def juan_vago(arr):

    n = len(arr)

    if n == 0:
        return 0, []

    dp = [0] * (n+2)

    for i in range(n-1,-1,-1):
        dp[i] = max(dp[i+2] + arr[i], dp[i+1])

    return dp[n], solucion(arr,dp)

def solucion(arr, dp):
    n = len(arr)
    i = 0
    sol = []
    while i < n:
        if i + 2 < len(dp) and dp[i] == arr[i] + dp[i + 2]:
            sol.append(arr[i])
            i += 2  # Saltamos el siguiente día porque no se puede trabajar dos días seguidos
        else:
            i += 1  # N

    return sol