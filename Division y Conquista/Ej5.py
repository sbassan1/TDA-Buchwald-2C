
"""
Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.
"""

def combinar(arr1, arr2):
    nuevo_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            nuevo_arr.append(arr1[i])
            i += 1
        else:
            nuevo_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        nuevo_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        nuevo_arr.append(arr2[j])
        j += 1

    return nuevo_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2

    arr1 = merge_sort(arr[:mitad])
    arr2 = merge_sort(arr[mitad:])

    return combinar(arr1, arr2)

"""
T(n) = 2 T(n/2) + O(n^1), a = 2, b = 2, c = 1
Como (c == 1) == (log2 2 = 1) => Estamos en el segundo caso del teorema maestro por lo tanto la complejidad es O(n^(log2 2) log n) == O(n log n)
"""

