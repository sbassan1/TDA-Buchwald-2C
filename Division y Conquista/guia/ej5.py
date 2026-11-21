"""
Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.
"""

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])

    return merge(izq, der)

def merge(izq, der):
    res = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            j += 1

    res.extend(izq[i:])
    res.extend(der[j:])
    return res