"""
Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos,
pero vivimos en una era de inflación y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). Implementar un
algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. Indicar y justificar la complejidad del algoritmo implementado.

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. ¿Por qué se trata de un algoritmo Greedy? Justificar
"""

# Solo podemos comprar un producto por día, los productos mas caros seran los que subiran de precio comparados con el dia anterior.
# Por lo tanto una idea seria elegir los productos mas caros primero de mayor a menor todos los dias.

def precios_inflacion(R):

    R.sort(reverse=True) # Productos mas caros a mas chicos
    suma = 0

    for dia, i in enumerate(R):
        R[i] = R[i]**(dia + 1)
        suma += R[i]
        dia += 1

    return suma

"""

La complejidad del algoritmo es O(n log n) ya que el ordenamiento de los productos se realiza en tiempo logarítmico y luego se recorre la lista en tiempo lineal O(n).

Si sabemos que la inflacion de todos los productos siempre dará un R[i]^{j + 1}, entonces los productos mas caros siempre subiran en valor de forma más grande, por lo tanto
si queremos minimizar el costo final, debemos comprar los productos mas caros primero.

"""
