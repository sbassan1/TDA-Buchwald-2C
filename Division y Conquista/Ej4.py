"""
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

- Implementar un algoritmo de división y conquista de complejidad O(log n) que encuentre la posición p del pico: func PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.
- Justificar la complejidad del algoritmo mediante el teorema maestro.

"""

def posicion_pico(v, ini, fin):

    if ini == fin:
        return ini

    mitad = (ini + fin) // 2

    if v[mitad-1] < v[mitad] and v[mitad+1] < v[mitad]:
        return mitad

    if v[mitad] < v[mitad+1]:
        return posicion_pico(v,mitad+1,fin)
    else:
        return posicion_pico(v,ini,mitad)


"""
T(n) = 1 T(n/2) + O(1) | a = 1, b = 2, c = 0
(log2 1 == 0) = (C = 0) => Segundo caso de teorema maestro: O(n^0 log n) => O(log n)
"""

v = [1, 2, 3, 1, 0, -2]
print(posicion_pico(v, 0, len(v)-1))
