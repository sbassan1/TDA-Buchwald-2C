
"""
Sea A una matríz de n × n (con n ≥ 3) con todos valores diferentes. Definimos la vecindad de una celda como las 8 celdas vecinas (arriba, abajo, derecha, izquierda, y las 4 diagonales), siempre que existan (en los bordes algunas no existirán). Un elemento A [i, j] es un máximo local si su valor es estrictamente mayor que el valor de todas las celdas vecinas. Implementar un algoritmo de división y conquista que encuentre un máximo local en tiempo O(n). Justificar adecuadamente la complejidad del algoritmo implementado.
"""

def es_valido(i, j, n):
    return 0 <= i < n and 0 <= j < n

def obtener_vecinos(i, j, matriz):
    n = len(matriz)
    vecinos = []

    direcciones = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    for di, dj in direcciones:
        ni, nj = i + di, j + dj
        if es_valido(ni, nj, n):
            vecinos.append((ni, nj))
    return vecinos

def max_local_rec(matriz, i_inicio, i_fin, j_inicio, j_fin):
    if i_inicio > i_fin or j_inicio > j_fin:
        return None

    mid_i = (i_inicio + i_fin) // 2
    mid_j = (j_inicio + j_fin) // 2

    max_val = float('-inf')
    max_pos = (-1, -1)

    for j in range(j_inicio, j_fin + 1):
        if matriz[mid_i][j] > max_val:
            max_val = matriz[mid_i][j]
            max_pos = (mid_i, j)

    for i in range(i_inicio, i_fin + 1):
        if matriz[i][mid_j] > max_val:
            max_val = matriz[i][mid_j]
            max_pos = (i, mid_j)

    r, c = max_pos

    # 2. Verificar si el máximo de la cruz es un máximo local
    mayor_vecino = (r, c)
    val_actual = matriz[r][c]

    for ni, nj in obtener_vecinos(r, c, matriz):
        if matriz[ni][nj] > val_actual:
            val_actual = matriz[ni][nj]
            mayor_vecino = (ni, nj)

    # Si ningún vecino es estrictamente mayor, encontramos el máximo local
    if mayor_vecino == (r, c):
        return (r, c)

    # 3. Decidir en qué cuadrante continuar según la posición del vecino mayor
    v_i, v_j = mayor_vecino

    nuevo_i_inicio = mid_i + 1 if v_i > mid_i else i_inicio
    nuevo_i_fin    = mid_i - 1 if v_i < mid_i else i_fin
    nuevo_j_inicio = mid_j + 1 if v_j > mid_j else j_inicio
    nuevo_j_fin    = mid_j - 1 if v_j < mid_j else j_fin

    return max_local_rec(matriz, nuevo_i_inicio, nuevo_i_fin, nuevo_j_inicio, nuevo_j_fin)

def max_local(matriz):
    n = len(matriz)
    return max_local_rec(matriz, 0, n - 1, 0, n - 1)

"""
Implementar un algoritmo greedy que dada una lista de intervalos de formato [a, b] (con a <= b) determine el menor conjunto
de intervalos que incluyan el mismo rango que los intervalos originales. Indicar y justificar la complejidad del algoritmo. Justificar
por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.

Ejemplos:
    [1, 3], [5, 7], [2, 4] → [1, 4], [5, 7]
    [3, 5], [1, 2], [2, 3], [7, 10], [5, 7] → [1, 10]
    [5, 8], [3, 7], [4, 5], [10, 15], [9, 13], [11, 14] → [3, 8], [9, 15]
    [1.3, 2.8], [2.97, 3.2], [0, 1.5], [2.95, 3] → [0, 2.8], [2.95, 3.2]

Notar que, por ejemplo, para el primer ejemplo no sería válido definir el intervalo [1, 7] porque incluiría el rango [4, 5] el cual no se encuentra incluído entre los originales.
"""

"""
Es un algoritmo greedy ya que construye la solucion eligiendo paso por paso con una eleccion greedy que da un optimo local, en nuestro caso la eleccion greedy es verificar que el intervalo siguiente esta dentro del actual comparando sus valores a,b. En cada paso el algoritmo decide si el intervalo está separado o no de la solucion.

La solucion es optima ya que al ordenar los intervalos por su inicio nos aseguramos que siempre podremos verificar de forma correcta si el siguiente esta dentro o no del anterior, eso garantiza que siempre podamos tomar en cuenta o no los valores de inicio y fin y siempre cortar con el intervalo actual a solucion y que no se desaproveche un intervalo.
"""

def lista_intervalos(intervalos):

    n = len(intervalos)

    if n == 0:
        return []

    intervalos = sorted(intervalos, key= lambda x : x[0])

    inicio, fin = intervalos[0]
    sol = []

    for a,b in intervalos[1:]:

        if a <= fin:
            fin = max(fin,b)
        else:
            sol.append([inicio,fin])
            inicio, fin = a,b

    sol.append([inicio, fin])

    return sol

"""
El problema conocido como Feedback Vertex Set (FVS) indica: Dado un grafo (por simplificación, no dirigido), indicar vértices a
eliminar de dicho grafo de tal manera que el grafo quede acíclico. En nuestro grafo cada vértice i tiene un valor positivo vi.

Implementar un algoritmo que, por backtracking, encuentre el mínimo FVS (es decir, el conjunto de vértices que sea un FVS, y sea de suma mínima). Si bien es obvio, el grafo no cuenta con una primitiva tiene_ciclos (e, incluso, si la tuviera, sería poco conveniente usarla, recomendamos pensar por qué).
"""

def es_valido_agregar(grafo, v, conservados, padre):
    visitados = set()
    # Inicia un DFS desde 'v' considerando solo los vértices en 'conservados'
    return not tiene_ciclo_dfs(grafo, v, None, conservados, visitados)


def tiene_ciclo_dfs(grafo, actual, padre, conservados, visitados):

    visitados.add(actual)

    for vecino in grafo.obtener_vecinos(actual):
        if vecino in conservados or vecino == actual:
            if vecino not in visitados:
                if tiene_ciclo_dfs(grafo, vecino, actual, conservados, visitados):
                    return True
            elif vecino != padre:
                # Si el vecino ya fue visitado y no es el padre, hay un ciclo
                return True

    return False


def calcular_costo(vertices, pesos):
    return sum(pesos[v] for v in vertices)


def fvs_backtracking_rec(grafo, pesos, vertices, indice, eliminados, conservados, estado_optimo):

    costo_actual = calcular_costo(eliminados, pesos)

    if costo_actual >= estado_optimo['mejor_costo']:
        return

    # Caso base: evaluamos todos los vértices
    if indice == len(vertices):
        estado_optimo['mejor_costo'] = costo_actual
        estado_optimo['mejor_fvs'] = set(eliminados)
        return

    u = vertices[indice]

    # OPCIÓN 1: Eliminar el vértice 'u' del grafo
    eliminados.add(u)
    fvs_backtracking_rec(grafo, pesos, vertices, indice + 1, eliminados, conservados, estado_optimo)
    eliminados.remove(u)

    # OPCIÓN 2: Conservar el vértice 'u' en el grafo
    # Solo lo probamos si mantenerlo no genera un ciclo con los vértices ya conservados
    if es_valido_agregar(grafo, u, conservados, None):
        conservados.add(u)
        fvs_backtracking_rec(grafo, pesos, vertices, indice + 1, eliminados, conservados, estado_optimo)
        conservados.remove(u)


def obtener_mínimo_fvs(grafo, pesos):
    """
    Función principal que prepara las estructuras e inicia el backtracking.

    - grafo: Objeto Grafo con el método obtener_vecinos(v) y obtener_vertices().
    - pesos: Diccionario {vértice: peso_positivo}.
    """
    vertices = list(grafo.obtener_vertices())
    estado_optimo = {
        'mejor_costo': float('inf'),
        'mejor_fvs': set()
    }

    fvs_backtracking_rec(
        grafo=grafo,
        pesos=pesos,
        vertices=vertices,
        indice=0,
        eliminados=set(),
        conservados=set(),
        estado_optimo=estado_optimo
    )

    return estado_optimo['mejor_fvs'], estado_optimo['mejor_costo']

"""
Implementar un algoritmo que dado una lista (ordenada) de monedas posibles y una cantidad de cambio a dar, devuelva la cantidad de formas diferentes que hay para dar dicho cambio. El algoritmo a implementar debe ser también por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado.
"""

def cambio_monedas(monedas, cambio):

    n = len(monedas)
    if cambio == 0 or n == 0:
        return []

    tabla = [0] * (cambio + 1)
    tabla[0] = 1  # Caso base: 1 forma de dar cambio 0

    for moneda in monedas:
        for j in range(moneda, cambio + 1): # De moneda a cambio + 1, si
            tabla[j] = tabla[j] + tabla[j - moneda]

    return tabla[cambio]
