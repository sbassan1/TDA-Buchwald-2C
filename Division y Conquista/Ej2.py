"""
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de complejidad O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.
"""

def prim_cero_rec(arr, inicio, fin):
    if inicio == fin:
        if arr[inicio] == 0:
            return inicio
        else:
            return -1

    mitad = (inicio + fin) // 2

    if arr[mitad] == 1:
        return prim_cero_rec(arr, mitad + 1, fin)
    else:
        return prim_cero_rec(arr, inicio, mitad)


def indice_primer_cero(arr):
    if not arr:  # Manejo de arreglo vacío
        return -1
    return prim_cero_rec(arr, 0, len(arr) - 1)


"""
T(n) = 1 T(n/2) + O(1) | a = 1, b = 2, c = 0
Como (Log2 1 = 0) = (c == 0) ==> Segundo caso: O(n^(log2 1) log n) ==> O(log n), cumple con la complejidad requerida.
"""
