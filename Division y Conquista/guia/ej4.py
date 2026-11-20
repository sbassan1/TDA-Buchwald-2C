
"""
Se tiene un arreglo de N >=3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N−1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p=2. Se pide: a. Implementar un algoritmo de división y conquista de complejidad O(logn) que encuentre la posición p del pico. b. Justificar la complejidad del algoritmo mediante el teorema maestro.
"""

[1,2,3,1]

[1, 2, 3, 1, 0, -2]

[1,2,3][1, 0, -2]

def encontrar_pico(l: list[int | float]) -> int:
    if len(l) < 3:
        raise ValueError("El arreglo debe tener al menos 3 elementos.")

    return rec(l, 1, len(l) - 2)

def rec(l, izq: int, der: int) -> int:
    if izq == der:
        return izq

    mid = izq + (der - izq) // 2

    if l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
        return mid

    if l[mid] > l[mid - 1]:
        return rec(l, mid + 1, der)

    return rec(l, izq, mid - 1)
