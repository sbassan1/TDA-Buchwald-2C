"""
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. Justificar la complejidad de la solución.
Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. Para hacer interesante el ejercicio, resolver puramente por división y conquista.Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces. Justificar la complejidad de la solución.
"""

def obtener_candidato_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio], 1

    medio_izq = (inicio + fin) // 3
    medio_der = 2 * ((inicio + fin) // 3)

    

def mas_de_dos_tercios(arr):

    if not arr:
        return False

    candidato, _ = obtener_candidato_rec(arr, 0, len(arr) - 1)
    ocurrencias = sum(1 for x in arr if x == candidato)

    return ocurrencias >  2 * (len(arr) // 3)
