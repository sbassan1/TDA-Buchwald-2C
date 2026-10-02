"""
Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin que se solapen los horarios. Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.
"""

from compatibles import *

def es_compatible_con_solucion(curso_candidato, solucion_actual):
    for curso in solucion_actual:
        if not son_compatibles(curso_candidato, curso):
            return False
    return True

def obtener_combinaciones_rec(materias, i, sol_actual, resultado):
    if i == len(materias):
        resultado.append(sol_actual.copy())
        return

    materia_actual = materias[i]
    for curso in materia_actual:
        if es_compatible_con_solucion(curso, sol_actual):
            sol_actual.append(curso)
            obtener_combinaciones_rec(materias, i + 1, sol_actual, resultado)
            sol_actual.pop()

def obtener_combinaciones(materias):
    resultado = []
    obtener_combinaciones_rec(materias, 0, [], resultado)
    return resultado
