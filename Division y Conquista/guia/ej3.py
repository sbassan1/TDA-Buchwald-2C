
"""
Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(logn). Por ejemplo, para n=10 debe devolver 3, y para n=25 debe devolver 5. Justificar la complejidad del algoritmo.
"""

# parte_entera(10) -> 3
# parte_entera(25) -> 5


def entero_de_raiz_cuadrada(n):
    if n < 0:
        raise ValueError("El argumento n debe ser un entero no negativo.")
    if n < 2:
        return n
    return rec(n,1,n,1)

def rec(n,low,high,ans):
    if low > high:
        return ans

    mid = low + (high - low) // 2
    if mid <= n // mid:
        return rec(n,mid + 1, high, mid)
    return rec(n,low, mid - 1, ans)

print(entero_de_raiz_cuadrada(10))
print(entero_de_raiz_cuadrada(25))