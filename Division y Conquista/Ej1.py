"""
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo
de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo.
Ejemplos:
    [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
    [5, 3, -5, 4, -1] ->  [5, 3]
    [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
    [5, -4, 2, 4] -> [5, -4, 2, 4]
    [-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
"""

"""
[5, -4, 2, 4]

SUM [5, -4] == [1]
SUM [2,  4] == [6]

[7]

"""

def suma_mitades(arr, inicio, medio, fin):
    suma_izq = 0
    suma_izq_max = float("-inf")
    indice_izq = medio
    for i in range(medio, inicio - 1, -1):
        suma_izq += arr[i]
        if suma_izq > suma_izq_max:
            suma_izq_max = suma_izq
            indice_izq = i

    suma_der = 0
    suma_der_max = float("-inf")
    indice_der = medio + 1
    for i in range(medio + 1, fin + 1):
        suma_der += arr[i]
        if suma_der > suma_der_max:
            suma_der_max = suma_der
            indice_der = i

    return (suma_izq_max + suma_der_max, indice_izq, indice_der)

def sublista_maxima(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio], inicio, fin

    medio = (inicio + fin) // 2

    max_izq, inicio_izq, fin_izq = sublista_maxima(arr, inicio, medio)
    max_der, inicio_der, fin_der = sublista_maxima(arr, medio + 1, fin)
    max_mitades, idx_izq, idx_der = suma_mitades(arr, inicio, medio, fin)

    if max_izq >= max_der and max_izq >= max_mitades:
        return max_izq, inicio_izq, fin_izq
    elif max_der >= max_izq and max_der >= max_mitades:
        return max_der, inicio_der, fin_der
    else:
        return max_mitades, idx_izq, idx_der

def max_subarray(arr):
    if not arr:
        return []

    _, inicio, fin = sublista_maxima(arr, 0, len(arr) - 1)
    return arr[inicio : fin + 1]


"""
Complejidad usando division y conquista segun el teorema maestro:

    O(n) = a * T(n/b) + C

    Donde:
        a = 2 # Tenemos dos llamados recursivos
        b = 2 # Dividimos el tamaño del problema a la mitad 
        C = O(n) # Cuando juntamos los resultados de las mitades sumandolas

        Como C == n^(log2 2) entonces O(n) = O(n^(log2 2) log n): O(n log n)
"""