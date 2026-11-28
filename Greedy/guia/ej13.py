
"""
Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido). Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?
"""

def cobertura_red(casas, r):
    if not casas:
        return []

    casas = sorted(casas)

    antenas = []
    i = 0
    n = len(casas)

    while i < n:
        casa_izquierda = casas[i]
        ubicacion_antena = casa_izquierda + r

        antenas.append(ubicacion_antena)

        # Mientras no lleguemos al final y el km de la casa llegue al radio de la antena
        while i < n and casas[i] <= ubicacion_antena + r:
            i += 1

    return antenas

"""
Este algoritmo es voraz ya que toma la decision de buscar la siguiente antena sin calcular estados diversos, lo hace con un estado local.

Es optimo, ya que minimizamos la cantidad de antenas buscando por el radio de la casa más izq tomando en cuenta todas las casas que lleguen a tal radio antes de colocar otra antena.

La complejidad es O(n log n) por el ordenamiento previo de las casas, luego iterar por cada casa es O(N) y pasar por las casas dentro de cada iteracion es O(N), pero ya que avanzamos el i al realizar el calculo no tomamos en cuenta el coste, por lo que amortiguado el primer while es O(N).

Complejidad espacial es O(N)
"""
