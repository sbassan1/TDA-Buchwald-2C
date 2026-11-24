"""
Implementar un algoritmo greedy que dada una lista de intervalos de formato [a, b] (con a <= b) determine el menor conjunto
de intervalos que incluyan el mismo rango que los intervalos originales. Indicar y justificar la complejidad del algoritmo. Justificar
por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.

Ejemplos:
    [1, 3], [5, 7], [2, 4] → [1, 4], [5, 7]
    [3, 5], [1, 2], [2, 3], [7, 10], [5, 7] → [1, 10]
    [5, 8], [3, 7], [4, 5], [10, 15], [9, 13], [11, 14] → [3, 8], [9, 15]
    [1.3, 2.8], [2.97, 3.2], [0, 1.5], [2.95, 3] → [0, 2.8], [2.95, 3.2]

Notar que, por ejemplo, para el primer ejemplo no sería válido definir el intervalo [1, 7] porque incluiría el rango [4, 5] el cual no se encuentra incluído entre los originales.
"""

caso1 = [ [1, 3], [5, 7], [2, 4] ]
caso2 = [ [3, 5], [1, 2], [2, 3], [7, 10], [5, 7] ]
#print(sorted(, key=lambda x: x[0]))
#print(sorted([ [5, 8], [3, 7], [4, 5], [10, 15], [9, 13], [11, 14] ], key=lambda x: x[0]))
#print(sorted([ [1.3, 2.8], [2.97, 3.2], [0, 1.5], [2.95, 3] ], key=lambda x: x[0]))

def unir_intervalos(arr):
    if not arr:
        return []
    
    arr = sorted(arr, key=lambda x: x[0])   # ordenar PRIMERO
    sol = []
    ini, fin = arr[0]
    
    for i in range(1, len(arr)):
        a, b = arr[i]
        if a > fin:                # hay hueco → cerrar intervalo actual
            sol.append([ini, fin])
            ini, fin = a, b
        else:                       # solapamiento o contacto → extender
            fin = max(fin, b)       # ← max, no asignación directa
    sol.append([ini, fin])
    return sol

print(unir_intervalos(caso1))