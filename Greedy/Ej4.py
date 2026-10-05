"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado.
"""

# Charlas tienen formato (inicio, fin), ordeno por su horario de finalizacion.

def charlas(horarios):
    if not horarios:
        return []

    horarios_ordenados = sorted(horarios, key=lambda x: x[1])
    
    solucion = [horarios_ordenados[0]]
    ultima_charla_agregada = horarios_ordenados[0]
    
    for charla in horarios_ordenados[1:]:
        if ultima_charla_agregada[1] <= charla[0]:
            solucion.append(charla)
            ultima_charla_agregada = charla
            
    return solucion
"""
La complejidad es O(n log n), ya que primero organizamos las charlas por su horario de fin
y luego para conseguir las lista de charlas maxima tenemos que iterar, eligiendo las charlas compatibles
a partir de su horario de fin con el de inicio de la charla siguiente. 
"""
