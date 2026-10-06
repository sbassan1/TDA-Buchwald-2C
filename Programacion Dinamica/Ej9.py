"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda. Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
La complejidad es O(n*m), ya que iteramos por la cantidad de monedas y luego por la cantidad
de monto posible para cada combinacion.
"""

def cambio(monedas, monto):
    INF = monto + 1
    mem = [INF] * (monto + 1)
    mem[0] = 0 
    
    # parent[j] guardará la moneda usada para llegar al monto j
    parent = [-1] * (monto + 1)

    # Rellenar la tabla DP
    for j in range(1, monto + 1):
        for moneda in monedas:
            if j - moneda >= 0:
                if mem[j - moneda] + 1 < mem[j]:
                    mem[j] = mem[j - moneda] + 1
                    parent[j] = moneda

    # Si no se puede formar el monto objetivo
    if mem[monto] == INF:
        return []

    # Reconstrucción de las monedas utilizadas
    sol = []
    curr = monto
    while curr > 0:
        moneda_usada = parent[curr]
        sol.append(moneda_usada)
        curr -= moneda_usada

    return sol