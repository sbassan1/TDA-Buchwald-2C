
"""
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco.

Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular.
Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa.

Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a
la casa n-1, que nos daría gn-1. Toda casa se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son
vecinas.

El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían
muy rápido. No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos.

El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia,
vamos a buscar el óptimo a este problema.

Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles.
Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.
"""

"""
- Ganancia es una lista de enteros que representa las ganancias obtenibles en cada casa.
- i es el indice de la casa actual.
- Si elijo una casa para robar se me inabilita las adjacentes a esa casa. incluyendo de n-1 a 0 y viceversa.

Opciones:
    - Si robo la casa i, no puedo robar las casas i-1 o i+1, asi que paso a la casa i+2 o i-2
    - Si no robo la casa i, puedo pasar a la casa i+1 o i-1

Tenemos que agarrar entonces:
    lunatico(ganancias, i) = max(ganancias[i] + lunatico(ganancias, i+2), lunatico(ganancias, i+1))

Para tomar en cuenta, si robe la primera casa obligatoriamente no puedo robar la última casa.

"""
def lunatico(ganancias):
    n = len(ganancias)

    if n == 0:
        return []

    if n == 1:
        return [0]

    # Caso 1: Robamos la 1ra casa, no podemos robar la última ni la segunda.
    ganancia_robando_primera, casas_robando_primera = lunatico_pd(ganancias[2:-1])
    ganancia_robando_primera += ganancias[0]
    casas_robando_primera = [0] + [idx + 2 for idx in casas_robando_primera]

    # Caso 2: No robamos la 1ra casa, empezamos desde la 2da casa.
    ganancia_no_robando_primera, casas_no_robando_primera = lunatico_pd(ganancias[1:])
    casas_no_robando_primera = [idx + 1 for idx in casas_no_robando_primera]

    if ganancia_robando_primera >= ganancia_no_robando_primera:
        return casas_robando_primera
    else:
        return casas_no_robando_primera


def lunatico_pd(sub_ganancias):
    m = len(sub_ganancias)

    if m == 0:
        return 0, []

    mem = [0] * (m + 2)

    for i in range(m - 1, -1, -1):
        mem[i] = max(mem[i + 1], sub_ganancias[i] + mem[i + 2])

    casas_robadas = []
    i = 0
    while i < m:
        if sub_ganancias[i] + mem[i + 2] >= mem[i + 1]:
            casas_robadas.append(i)
            i += 2
        else:
            i += 1

    return mem[0], casas_robadas

# --- Ejemplo de prueba ---
ganancias = [1,1]
casas = lunatico(ganancias)
print(f"Casas Robadas (índices): {casas}")  # Output: [0, 2]

"""
Ecuacion de recurrencia para el caso de dp:

OPT(i) = {
Si i = 0, OPT(i) = 0
Si i = 1, OPT(i) = sub_ganancias[0]
Si i > 1, OPT(i) = max(OPT(i-1), sub_ganancias[i-1] + OPT(i-2))
}
"""
