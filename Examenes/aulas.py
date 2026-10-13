"""
Planteamos otra variante del problema de interval scheduling. Tenemos una secuencia de charlas a dar con horario de inicio y fin (fin > inicio). En este caso, queremos dar todas las charlas, por lo que necesitaremos más de un auditorio/aula para darlas, y que no hayan solapamientos. Nos interesa minimizar cantidad de aulas que necesitamos para dar todas las charlas, de tal forma que en una misma aula no hayan dos charlas que se solapen entre sí. Implementar un algoritmo que devuelva la conformación de estas aulas. Este problema puede resolverse de forma óptima, y se espera que así se resuelva. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar. Si no lo es, dar un contraejemplo. Justificar por qué es un algoritmo Greedy. Indicar y justificar la complejidad.
"""

# Charlas: (inicio,fin)
def auditorios(charlas):

    n = len(charlas)
    if n == 0:
        return []

    charlas = sorted(charlas, key= lambda x : x[0])
    aulas = []
    aulas.append(charlas[0])

    for ch in charlas[1:]:
        colocada = False
        for a in aulas:
            if a[-1][1] < ch[0]:
                a.append(ch)
                colocada = True
                break

        if not colocada:
            aulas.append(ch)

    return aulas

"""
La complejidad sera:
    O(n log n) para ordenar las charlas por su horario de fin
    Dentro del for loop O(N):
        En el peor caso tenemos una aula para cada charla, si todas se sobrelapan y tienen el mismo horario de fin. O(N)
    Por lo tanto el doble for nos daría O(n^2)
En el peor caso O(n^2)
"""


"""
Implementar un algoritmo que, dado un grafo no dirigido, obtenga el clique de mayor tamaño dentro del mismo (utilizando backtracking).
"""

def es_valido(grafo, sol_actual, v):
    for u in sol_actual:
        if not grafo.hay_arista(u, v):
            return False
    return True

def clique(grafo):
    vert = list(grafo.obtener_vertices())
    if not vert:
        return set()

    mejor_sol = set()
    clique_rec(grafo, vert, 0, set(), mejor_sol)
    return mejor_sol

def clique_rec(grafo, vert, i, sol_actual, mejor_sol):

    if len(sol_actual) + (len(vert) - i) <= len(mejor_sol):
        return

    if i == len(vert):
        if len(sol_actual) > len(mejor_sol):
            mejor_sol.clear()
            mejor_sol.update(sol_actual)
        return

    v = vert[i]

    if es_valido(grafo, sol_actual, v):
        sol_actual.add(v)
        clique_rec(grafo, vert, i + 1, sol_actual, mejor_sol)
        sol_actual.remove(v) 

    clique_rec(grafo, vert, i + 1, sol_actual, mejor_sol)

"""
Patricio es el hermano de Juan (sí, el vago), y tiene una filosofía muy parecida a la de él. El problema es que la lleva a un extremo: no le interesa en lo más mínimo el dinero. Si fuera por Patricio, no agarraría la pala ningún día de su vida pero, por mala suerte, la vida no es tan sencilla. Su jefe ya le ha llamado la atención, por lo que sabe que no puede estar dos días seguidos sin trabajar. Tiene un arreglo de n valores, donde el elemento i indica el esfuerzo de trabajar el día i (cada día demanda un esfuerzo diferente). Patricio puede elegir trabajar un día, o no trabajar. Implementar un algoritmo que, por programación dinámica, obtenga el mínimo esfuerzo total (suma de esfuerzos) a trabajar en el período de n días, con la restricción que Patricio no puede estar dos días seguidos sin trabajar. También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado (el de programación dinámica, y también el de la reconstrucción).
"""

# Lista de ints para esfuerzos 
def patricio_vago(esfuerzos):
    
    n = len(esfuerzos)
    if n == 0:
        return []

    dp_T = [0] * n  # Mínimo esfuerzo hasta i TRABAJANDO en i
    dp_N = [0] * n  # Mínimo esfuerzo hasta i NO TRABAJANDO en i

    dp_T[0] = esfuerzos[0]
    dp_N[0] = 0

    for i in range(1, n):
        dp_T[i] = esfuerzos[i] + min(dp_T[i - 1], dp_N[i - 1])
        dp_N[i] = dp_T[i - 1] # Si no trabajo, tiene que trabajar el sig

    dias_trabajados = []
    if dp_T[n - 1] <= dp_N[n - 1]:
        trabajo = True
    else:
        trabajo = False

    i = n - 1
    while i >= 0:
        if trabajo:
            dias_trabajados.append(i)  # Guardamos el índice del día trabajado
            # Averiguamos si en i-1 venía de trabajar o descansado
            if i > 0:
                if dp_T[i - 1] <= dp_N[i - 1]:
                    trabajo = True
                else:
                    trabajo = False
        else:
            # Si en el día i descansó, obligatoriamente en i-1 tuvo que trabajar
            trabajo = True

        i -= 1

    dias_trabajados.reverse()
    return dias_trabajados