"""
Implementar un algoritmo de división y conquista que reciba un arreglo de K arreglos/listas ordenadas, cada una de H elementos (es decir, en total hay n = K*H elementos) y devuelva un arreglo con todos los elementos, ya ordenados. El algoritmo debe utilizar la información del enunciado para considerarse aprobable. NO utilizar un heap para resolver el problema, se está evaluando división y conquista. 

Una vez implementado, puede que no sea posible utilizar el Teorema Maestro para calcular su complejidad. Explicar por qué es el caso. Dar cuál sería la complejidad con una breve justificación (no es necesario hacer una demostración). En caso que tu implementación sí permita calcular su complejidad con el Teorema Maestro, recomendamos revisar que esté bien hecho y, si lo está, dar su complejidad dada por el teorema.
"""

def merge(arr1, arr2):

    res = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res


def ej1(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]          # hoja: una de las K listas, ya ordenada

    mid = (inicio + fin) // 2
    izq = ej1(arr, inicio, mid)
    der = ej1(arr, mid + 1, fin)
    return merge(izq, der)

"""
En este ejercicio tenemos que N es K*H y por lo que el teorema maestro nos quedaría como T(K) = 2 T(K/2) + O(K), como K != H
"""


"""
El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un laboratorio farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un catálogo del valor de cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad disponible (medible en ml). Rizzoli sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo bueno es que sabe que puede fraccionar y poner proporciones de los fármacos; y en ese caso lo vendería en su valor proporcional. Implementar un algoritmo greedy que obtenga los fármacos (y cantidades) que Rizzoli debe robarse para obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta familia no se aceptan los robos a medias). Justificar por qué el algoritmo propuesto es Greedy y por qué es, en efecto, óptimo. Indicar y justificar la complejidad del algoritmo implementado.
"""

# Farmacos : lista de tuplas (precio, cant_mL)

def mochila_fraccionaria(farmacos, L):

    # Ordenar por valor específico (valor por ml) descendente
    farmacos_ord = sorted(farmacos, key=lambda f: f[0] / f[1], reverse=True)

    sol = []
    ganancia = 0
    capacidad = L          # L ya está en ml, no convertir

    for valor_total, cant_ml in farmacos_ord:
        if cant_ml <= capacidad:
            # me llevo todo el fármaco
            sol.append((valor_total, cant_ml))
            ganancia += valor_total
            capacidad -= cant_ml
        else:
            # me llevo solo 'capacidad' ml (fracción)
            fraccion = capacidad / cant_ml
            valor_frac = valor_total * fraccion
            sol.append((valor_frac, capacidad))
            ganancia += valor_frac
            capacidad = 0
            break
        if capacidad == 0:
            break

    return sol, ganancia

"""
El problema conocido como Feedback Edge Set (FES) (cómo problema de optimización) indica: Dado un grafo dirigido, obtener la menor cantidad de aristas a eliminar de dicho grafo de tal manera que el grafo quede acíclico. Implementar un algoritmo que, por backtracking, resuelva el problema. Podés considerar que existe una función tiene_ciclo(grafo, vértices) que devuelve true si el grafo tiene algún ciclo en la componente débilmente conexa definida por los vértices pasados por parámetro, y también la función componentes_debilmente_conexas(grafo, vertices) que devuelve una lista de listas, cada una con una componente débilmente conexa del grafo entre los vértices definidos por parámetro.
"""

def feedback_edge_set(grafo):
    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            aristas.append((v, w))

    return backtracking_fes(grafo, aristas, 0, 0, float('inf'))

def backtracking_fes(grafo, aristas, idx, eliminadas, mejor_cant):
    if eliminadas >= mejor_cant:
        return float('inf')
    
    if not tiene_ciclo(grafo, grafo.vertices()):
        return eliminadas
    
    if idx == len(aristas):
        return float('inf')
        
    u, v = aristas[idx]
    
    grafo.remover_arista(u, v)
    res_eliminar = backtracking_fes(grafo, aristas, idx + 1, eliminadas + 1, mejor_cant)
    mejor_cant = min(mejor_cant, res_eliminar)
    grafo.agregar_arista(u, v)
    res_conservar = backtracking_fes(grafo, aristas, idx + 1, eliminadas, mejor_cant)
    
    return min(res_eliminar, res_conservar)


def tiene_ciclo(grafo, vert):
    return True


"""
Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)). Cada vertice tiene un valor (positivo). Implementar un algoritmo que, utilizando programación dinámica, obtenga el Set Independiente de suma máxima dentro de un grafo de dichas características. También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado (el de programación dinámica, y también el de la reconstrucción).
"""

# Set independiente es un subconjunto de vertices tal que ningun par de vertices dentro del subconjunto están conectados entre sí
# Nos piden encontrar el set independiente tal que cada elemento del vertice dentro del conjunto dé una suma máxima 
# Como el grafo es un camino, entonces el set optimo elije si el elemento está o no dentro de este, hay dos formas 

# Tenemos dos opciones, si agarramos el vertice i => debemos agarrar si o si el (i + 2) ó (i + 3), ya que para que sea un IS tenemos que cubrir todas los vertices.

"""
OPT(i) == {
    Max(valor_i + OPT[i+2], OPT(i+1))
}
"""

def ej4(grafo):

    vert = grafo.obtener_vertices()
    valores = []
    for id,valor in vert:
        valores.append(id,valor)

    n = len(valores)
    OPT = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        OPT[i] = max(valores[i][1] + OPT[i + 2], OPT[i + 1])
    return OPT[0], OPT

def reconstruir(valores, OPT):
    sol = []
    n = len(valores)
    i = 0
    while i < n:
        
        if valores[i][0] + OPT[i + 2] >= OPT[i + 1]:
            sol.append(i)       # tomo el vértice i
            i += 2              # salto i+1 (prohibido)
        else:
            i += 1              # no tomo i
    return sol