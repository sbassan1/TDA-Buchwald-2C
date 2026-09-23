"""
Implementar una función (que utilice división y conquista) de complejidad O(n) que dado un arreglo de n números enteros devuelva true o false según si existe algún
elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución.
Aclaración: Este ejercicio puede resolverse, casi trivialmente, utilizando una tabla de hash. Para hacer interesante el ejercicio, resolver puramente por división y conquista.
"""

def obtener_candidato_rec(arr, inicio, fin):

    if inicio == fin:
        return arr[inicio], 1

    medio = (inicio + fin) // 2

    num_izq, cantidad_izq = obtener_candidato_rec(arr, inicio, medio)
    num_der, cantidad_der = obtener_candidato_rec(arr, medio + 1, fin)

    # Combinación O(1)
    if num_izq == num_der: # Si ambos candidatos son iguales, sumamos sus ocurrencias
        return num_izq, cantidad_izq + cantidad_der
    elif cantidad_izq >= cantidad_der: # Si el candidato izquierdo aparece más veces, restamos las ocurrencias del derecho
        return num_izq, cantidad_izq - cantidad_der
    else: # O viseversa
        return num_der, cantidad_der - cantidad_izq

def mas_de_la_mitad(arr):
    
    if not arr:
        return False

    candidato, _ = obtener_candidato_rec(arr, 0, len(arr) - 1)
    ocurrencias = sum(1 for x in arr if x == candidato)

    return ocurrencias > len(arr) // 2
