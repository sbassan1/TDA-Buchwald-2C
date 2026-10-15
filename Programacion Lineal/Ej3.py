"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un modelo de programación lineal que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.
"""

"""
F.O:
    min( Sum{i=0,n-1}(Vi) )

Variable de decision:
    v[i] donde v[i] = {
        1 si V_i esta en el vert cover
        0 si V_i NO esta en el vert cover
    }

Restricciones:
    V[i]+Y[j] <=1, para todos los (i,j) en E

Ya que necesitamos que al menos todos los (i,j) existan al menos 1 vez, pero sin aristas innecesarias debemos guardar las aristas ya tomadas y que no se repitan.
"""

import pulp

def vertex_cover_min(grafo):
    vert = grafo.obtener_vertices()
    n = len(vert)
    
    if n == 0:
        return []
        
    vert_to_idx = {v: i for i, v in enumerate(vert)}

    prob = pulp.LpProblem("min_vert_cover", pulp.LpMinimize)

    v = [pulp.LpVariable(f"v_{i}", cat=pulp.LpBinary) for i in range(n)]

    prob += pulp.lpSum(v[i] for i in range(n))

    aristas_procesadas = set()
    for i, u in enumerate(vert):
        for adj in grafo.adyacentes(u):
            j = vert_to_idx[adj]
            # Me daba que aristas se repetian asi que los guardo
            # en aristas procesadas con los vertices ordenados
            arista = tuple(sorted((i, j)))
            if i != j and arista not in aristas_procesadas:
                aristas_procesadas.add(arista)
                prob += v[i] + v[j] >= 1

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    sol = []
    for i in range(n):
        if pulp.value(v[i]) > 0.5:
            sol.append(vert[i])
            
    return sol