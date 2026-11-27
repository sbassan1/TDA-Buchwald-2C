
"""
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas. 

Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. Indicar y justificar la complejidad del algoritmo implementado.
"""

# Nos piden minimizar la cantidad de bosas usadas, ergo maximizar el espacio utilizado por bolsa,
# Bolsas de supermercado tienen max peso P y tenemos una bolsa con lista de pesos de N productos

def cant_min_bolsas(arr, P):

    arr = sorted(arr, reverse=True) # Ordenar de mayor a menor
    print(arr)

    sol = [] # Array de bolsas para solucion

    for elem in arr: # O(N) * O(N) => O(N^2)

        sin_bolsa = True
        for bolsa in sol: # O(N)
            if sum(bolsa) + elem <= P:
                bolsa.append(elem)
                sin_bolsa = False

        if sin_bolsa:
            sol.append([elem])

    return sol

print(cant_min_bolsas([ 4, 2, 1, 3, 5], 5))

# Es optimo ya que al tener la lista de elementos de mayor a menor, aseguraremos de llenar la bolsa minimizando la cantidad de resto de cada bolsa, siempre podremos