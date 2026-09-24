"""
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer,
y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene
la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas
sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. Implementar un algoritmo que, mediante programación
dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor
cantidad de espacios vacíos). Indicar y justificar la complejidad del algoritmo.

Para esta resolución en RPL, devolver una lista con los valores de los grupos a ubicar, en el orden original en el que se encontraban en el vector P.
"""


def bodegon_dinamico(P, W): # P es un array con la cantidad de personas de cada grupo y W es la cantidad de lugares disponibles en total

    if not P or W <= 0:
        return []

    n = len(P)
    mem = [[0] * (W + 1) for _ in range(n + 1)] # mem[i][w]: es la cantidad maxima de personas que se pueden sentar con los primeros i grupos y w lugares disponibles

    for i in range(1, n + 1):
        cant_personas_grupo = P[i - 1]
        for w in range(W + 1):
            if cant_personas_grupo <= w: # Si la mesa tiene al menos W lugares disponibles para el grupo i, se puede sentar o no se sienta
                mem[i][w] = max(mem[i - 1][w], cant_personas_grupo + mem[i - 1][w - cant_personas_grupo])
            else:  # Si no hay suficientes lugares disponibles, no se sienta
                mem[i][w] = mem[i - 1][w]

    grupos_elegidos = []
    w = W
    for i in range(n, 0, -1): # Vemos que grupos son diferentes al comparar los lugares disponibles
        if mem[i][w] != mem[i - 1][w]:
            grupos_elegidos.append(P[i - 1])
            w -= P[i - 1]

    grupos_elegidos.reverse()

    return grupos_elegidos

"""
La complejidad del algoritmo es O(n * W) + O(n) == O(n * W), donde n es la cantidad de grupos y W es la cantidad de lugares disponibles.
Esto es debido a que el algoritmo cubre un doble bucle para llenar la matriz de memoria y luego itera por cada grupo para saber si se debe incluir o no en la solución.
"""
