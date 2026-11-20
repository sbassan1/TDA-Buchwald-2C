
"""
Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario. De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). Se pide: a. una función de orden O(log⁡n)O(logn) que, por división y conquista, encuentre el índice del primer 0, de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests. Si no hay ningún 0 (solo hay unos), debe devolver -1. b. demostrar con el Teorema Maestro que la función es, en efecto, O(log⁡n)O(logn).

[1, 1, 0, 0, 0] →  2
[0, 0, 0, 0, 0] →  0
[1, 1, 1, 1, 1] → -1
"""

def encontrar_primer_cero(lista, izq, der):
    if izq > der:
        return -1

    mid = (izq + der) // 2

    if lista[mid] == 0:
        if mid == izq or lista[mid - 1] == 1:
            return mid
        return encontrar_primer_cero(lista, izq, mid - 1)

    return encontrar_primer_cero(lista, mid + 1, der)

caso_1 = [1, 1, 0, 0, 0]
caso_2 = [0, 0, 0, 0, 0]
caso_3 = [1, 1, 1, 1, 1]


print(encontrar_primer_cero(caso_1, 0, len(caso_1) - 1))
print(encontrar_primer_cero(caso_2, 0, len(caso_2) - 1))
print(encontrar_primer_cero(caso_3, 0, len(caso_3) - 1))