"""
Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido). 

Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?
"""


def cobertura(casas, R, K):
    if not casas:
        return []

    casas = sorted(casas)

    solucion = []
    i = 0
    n = len(casas)
    pos_antena = 0
    
    while i < n or pos_antena + R >= K:
        pos_antena = casas[i] + R # La primera casa sin covertura + el radio de la antena
        solucion.append(pos_antena)

        while i < n and casas[i] <= pos_antena + R:
            i += 1

    return solucion

"""
Este algoritmo es greedy ya que toma la mejor decision local en cada paso individual, en el caso de este ejericicio, el algoritmo elije la ubicacion de una antena desde la casa sin covertura mas el rango y desde allí itera por las casas siguientes hasta que encuentre una que no tenga covertura o encuentre el fin de la ruta.

Complejidad = O(n log n), ya que primero ordenamos ascendientemente las distancias de las casas que costará O(n log n) y luego iteraremos por la lista que nos costará O(n).

El algoritmo siempre eligira la solucion optima local, lo puedo demostrar con un induccion:
    - Las distancias de casas siempre son de menor a mayor => casas[i] <= casas[j] <= casas[n] para cada i < j < n
    - Lo mismo para las antenas solucion[i] <= solucion[j] <= solucion[n] para cada i < j < n

Tenemos dos soluciones:
    La Sg (solucion greedy) y la So (solucion optima)

Vamos a demostrar por induccion que para cada Sg[i], la antena esta >= a la derecha que la So[i] 

Caso Base N = 1:
    C1 es la primera casa, si solo tenemos la solucion[0] entonces cubriría casa[0] + R, por lo que es optimo en el caso base.
    
Hipotesis Inductiva: 
    Asumimos que Sg[i-1] >= So[i-1]
    
Paso Inductivo:
    - La antena Sg[i-1] cubre casas hasta Sg[i-1] + R, lo mismo para So (So[i-1] cubre casas hasta So[i-1] + R). 
    - Como Sg[i-1] >= So[i-1] => Sg[i-1] + R >= So[i-1] + R => La cobertura greedy alcanza o se pasa de la optima. 
    - Sea Pc la primera casa no cubierta por Sg[i-1], dado que Sg[i-1] cubre al menos todo lo que cubre So[i-1] la casa Pc no estará cubierta por So[i-1]
    - Para cubrir Pc es necesario que lo cubra la siguiente antena So[i] <= Pc + R, el Sg[i] = Pc + R, por lo tanto Sg[i] >= So[i]

"""