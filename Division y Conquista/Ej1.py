"""
Se cuenta con un arreglo de enteros ordenado de manera ascendente que contiene exactamente un número duplicado (es decir, todos los demás elementos son distintos, sin duplicados). Implementar una función que encuentre dicho número utilizando división y conquista. Indicar y justificar la complejidad del algoritmo, utilizando el Teorema Maestro.
"""


def encontrar_num(arr, inicio, fin):
    if inicio >= fin:
        if arr[inicio] == arr[inicio+1]:
            return arr[inicio]
        else:
            return None

    mitad = (inicio + fin) // 2

    # Caso base: encontramos los adyacentes iguales
    if mitad < fin and arr[mitad] == arr[mitad + 1]:
        return arr[mitad]
    if mitad > inicio and arr[mitad] == arr[mitad - 1]:
        return arr[mitad]

    # Búsqueda binaria recursiva
    # Buscamos en la mitad izquierda
    izq = encontrar_num(arr, inicio, mitad - 1)

    # Si lo encontramos en la izquierda, lo devolvemos
    if izq is not None:
        return izq

    # Si no, está en la derecha
    return encontrar_num(arr, mitad + 1, fin)


def elemento_duplicado(arr):
    return encontrar_num(arr, 0, len(arr) - 1)

"""
Utilizando teorema maestro:
    T(n) = 2 T(n/2) + O(n^1)

    a = 2, b = 2, c = 1

    Como Log2 2 == 1 crece igual que O(n^1) entonces, estamos en el 
    2do caso del teorema maestro ==> O(n^log2 2 log n) ==> O(n log n)
"""


arr = [5, 5, 12]
print("\n")
print(elemento_duplicado(arr), 5)

arr = [10, 15, 20, 20, 30]
print("\n")
print(elemento_duplicado(arr), 20)

arr = [1, 4, 9, 16, 25, 40, 40]
print("\n")
print(elemento_duplicado(arr), 40)

arr = [3, 8, 8, 15, 23, 42, 50, 61, 70, 88]
print("\n")
print(elemento_duplicado(arr), 8)

arr = [2, 5, 8, 11, 14, 17, 20, 20, 26, 29, 32, 35, 38, 41, 44]
print("\n")
print(elemento_duplicado(arr), 20)

arr = [-100, -80, -60, -40, -20, -10, -5, 0, 5, 10, 15, 20, 25, 30, 30, 45, 50, 60, 70, 80]
print("\n")
print(elemento_duplicado(arr), 30)

arr = [i * 3 for i in range(15)] + [42] + [i * 3 for i in range(15, 49)]
print("\n")
print(elemento_duplicado(arr), 42)

arr = list(range(10, 109)) + [108]
print("\n")
print(elemento_duplicado(arr), 108)
