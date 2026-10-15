"""
Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).

Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

"""


"""
La funcion objetivo es: 
Max( Sum{i = 0, n-1}(trabajos * x[i]))

La variable de decision es:

x[i], donde x[i] = {
    1 si Juan hace el trabajo el dia i
    0 si Juan no hace el trabajo el dia i
}

Restricciones:
x[i] + x[i+1] <= 1 para todo i en trabajos de 0 a n-2

Ya que nos dicen que Juan no quiere trabajar dos dias seguidos, por lo tanto la suma de un dia mas el siguiente siempre debería de ser <= 1
"""

import pulp

def juan_el_vago(trabajos):

    n = len(trabajos)

    if n == 0:
        return []

    if n == 1:
        return [0]

    # Esto define el problema como uno de optimizacion donde maximizamos algo
    prob = pulp.LpProblem("juan_el_vago", pulp.LpMaximize)

    # X es una lista de valores 0,1 que representa si Juan trabajo o no el dia i
    # Creamos n variables x con valor x_1,x_2,..,x_n, donde su valor es binario (0,1)
    x = [pulp.LpVariable(f"x_{i}", cat=pulp.LpBinary) for i in range(n)]

    # Funcion objetivo: maximizar la cantidad de dinero en trabajo con las restricciones
    prob += pulp.lpSum(trabajos[i] * x[i] for i in range(n))

    # Restriccion de que si trabaja un dia el siguiente no puede
    # Por lo tanto si x[i] + x[i+1] <= 1, ya que ambos no pueden ser 1 
    for i in range(n-1):
        prob += x[i] + x[i+1] <= 1

    # Busque como tener el resultado con menos prints, por eso el PULP_CBC_CMD(msg=false)
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    sol = []
    for i in range(n):
        if pulp.value(x[i]) > 0.5:
            sol.append(i)
    
    return sol

print(juan_el_vago([100, 5, 50, 1, 1, 200]))