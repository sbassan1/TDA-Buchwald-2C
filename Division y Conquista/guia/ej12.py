"""
Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad). Indicar y justificar su complejidad temporal.
"""

# Idea: Separar en mitades hasta tener valores de 1 elem y juntar intercalando, repetir
# [C1, C2, D1, D2] --> C1,D1

def intercalar(arr, inicio, fin):
    # fin - inicio + 1 es el tamaño del subarreglo actual (que será de la forma 2k)
    k = (fin - inicio + 1) // 2

    # Caso base: si el bloque es de tamaño 2 (ej: [C, D]), ya está intercalado
    if k <= 1:
        return

    # El punto medio exacto del subarreglo
    medio = inicio + k

    # El bloque izquierdo de C tiene tamaño k/2 y el derecho también.
    # Queremos cruzar la segunda mitad de las C con la primera mitad de las D.
    mitad_k = k // 2

    # Intercambiamos los bloques del medio:
    # Movemos las D que están al principio de la segunda mitad hacia el final de la primera mitad.
    for i in range(mitad_k):
        # Intercambiamos arr[medio - mitad_k + i] con arr[medio + i]
        # (Esto es equivalente al truco de entrelazar cartas de una baraja)
        idx1 = medio - mitad_k + i
        idx2 = medio + i
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    # Llamadas recursivas para ordenar las subpartes izquierda y derecha
    intercalar(arr, inicio, medio - 1)
    intercalar(arr, medio, fin)


# Función wrapper principal
def intercalar_arreglo(arr):
    if not arr:
        return arr
    intercalar(arr, 0, len(arr) - 1)
    return arr
