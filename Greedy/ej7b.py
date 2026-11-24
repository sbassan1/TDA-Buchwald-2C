
"""
En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer día. Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten esperar, y cada día debemos comprar uno de los productos.
Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""

# Cada dia que pasa los precios tienen exactamente la mitad
# Precio minimo a comprar todos los productos

# Ordenar precios de menor a mayor por el día 0 y comprar todos los productos
# Si tenemos los precios mas bajos primero maximizamos la cantidad que disminuyen los precios más altos por cada dia que transcurren, por lo tanto minimizamos el precio total a pagar

def precios_deflacion(R):

    r_sorteado = sorted(R , reverse= False) # Menor a mayor, O(n logn)

    dia = 0
    res = 0
    for precio in r_sorteado: # O(n)
        res += precio / (2 ** dia)
        dia+=1

    return res


# Es solucion optima ya que tiene una eleccion local que es elegir el precio en la lista