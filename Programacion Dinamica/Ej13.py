"""
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer,
y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene
la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas
sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, mediante programación
dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor
cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.

Para esta resolución en RPL, devolver una lista con los valores de los grupos a ubicar, en el orden original en el que se encontraban en el vector P.
"""

# Tenemos P = [p1, p2, ..., pn] con pi la cantidad de personas del grupo i
# W es la cantidad de lugares disponibles en la mesa
# Los familiares se deben sentar todos juntos, no separados

# La idea es usar programacion dinamica para minimizar la cantidad de espacios vacios,
# es decir, maximizar la cantidad de personas que se sienten en la mesa.

# Por lo tanto, tenemos dos opciones, una familia se sienta en la mesa entera, o no se sienta.
# Si se sienta sumamos pi a la cantidad de personas que se sentaron.


def bodegon_dinamico(P, W):
    if not P or W <= 0:
        return []

    n = len(P)
    mem = [[0] * (W + 1) for _ in range(n + 1)] # mem[i][w]: es la cantidad maxima de personas que se pueden sentar con los primeros i grupos y w lugares disponibles

    for i in range(1, n + 1):

        personas = P[i - 1]
        for w in range(W + 1):
            if personas <= w:
                mem[i][w] = max(mem[i - 1][w], personas + mem[i - 1][w - personas])
            else:
                mem[i][w] = mem[i - 1][w]


    grupos_elegidos = []
    w = W
    for i in range(n, 0, -1):
        if mem[i][w] != mem[i - 1][w]:
            grupos_elegidos.append(P[i - 1])
            w -= P[i - 1]

    grupos_elegidos.reverse()

    return grupos_elegidos
