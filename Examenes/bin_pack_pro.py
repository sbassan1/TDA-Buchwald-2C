
"""
Una empresa de logística necesita optimizar el transporte de una lista de paquetes. Todos los camiones (contenedores) disponibles tienen la misma capacidad máxima. Para minimizar los costos de transporte, se requiere un algoritmo basado en Backtracking (búsqueda con retroceso) que encuentre la distribución exacta que utilice la menor cantidad posible de camiones.
"""


def bin_packing_backtracking(items, capacity):
    if not items:
        return 0, []

    mejor = [[item] for item in items]

    mejor_solucion = bin_packing_backtracking_rec(
        items, capacity, 0, [], mejor
    )

    return len(mejor_solucion), mejor_solucion


def bin_packing_backtracking_rec(items, capacity, i, conten, mejor):
    if i == len(items):
        if len(conten) < len(mejor):
            mejor = [c.copy() for c in conten]
        return mejor

    if len(conten) >= len(mejor):
        return mejor

    item = items[i]

    for c in conten:
        if sum(c) + item <= capacity:
            c.append(item)
            mejor = bin_packing_backtracking_rec(items, capacity, i + 1, conten, mejor)
            c.pop()

    if len(conten) + 1 < len(mejor):
        conten.append([item])
        mejor = bin_packing_backtracking_rec(items, capacity, i + 1, conten, mejor)
        conten.pop()

    return mejor
