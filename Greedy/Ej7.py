"""
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""

# Solo podemos comprar un producto por día, los productos mas caros seran los que subiran de precio comparados con el dia anterior.
# Por lo tanto una idea seria elegir los productos mas caros primero de mayor a menor todos los dias.

def precios_inflacion(R):

    R.sort(reverse=True) # Productos mas caros a mas chicos

    sum = 0
    dia = 0
    for producto in R:
        producto = producto**(dia + 1)
        sum += producto
        dia += 1

    return sum


print(precios_inflacion([1,1,1,1,1,1,1,10]))
