"""
Implementar un algoritmo de división y conquista que reciba un arreglo de K arreglos/listas ordenadas, cada una de H elementos (es decir, en total hay n = K*H elementos) y devuelva un arreglo con todos los elementos, ya ordenados. El algoritmo debe utilizar la información del enunciado para considerarse aprobable. NO utilizar un heap para resolver el problema, se está evaluando división y conquista. 

Una vez implementado, puede que no sea posible utilizar el Teorema Maestro para calcular su complejidad. Explicar por qué es el caso. Dar cuál sería la complejidad con una breve justificación (no es necesario hacer una demostración). En caso que tu implementación sí permita calcular su complejidad con el Teorema Maestro, recomendamos revisar que esté bien hecho y, si lo está, dar su complejidad dada por el teorema.
"""

def merge_k_arreglos(lista_arreglos):
    if not lista_arreglos:
        return []
    return _merge_k_rec(lista_arreglos, 0, len(lista_arreglos) - 1)

def _merge_k_rec(lista_arreglos, inicio, fin):
    if inicio == fin:
        return lista_arreglos[inicio]
    
    mitad = (inicio + fin) // 2
    
    izq = _merge_k_rec(lista_arreglos, inicio, mitad)
    der = _merge_k_rec(lista_arreglos, mitad + 1, fin)
    
    return intercalar_dos_arreglos(izq, der)

def intercalar_dos_arreglos(arr1, arr2):
    i = j = 0
    resultado = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            resultado.append(arr1[i])
            i += 1
        else:
            resultado.append(arr2[j])
            j += 1
            
    resultado.extend(arr1[i:])
    resultado.extend(arr2[j:])
    return resultado


"""
En este ejercicio tenemos que N es K*H y por lo que el teorema maestro nos quedaría como T(K) = 2 T(K/2) + O(K), como K != H
"""


"""
El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un laboratorio farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un catálogo del valor de cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad disponible (medible en ml). Rizzoli sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo bueno es que sabe que puede fraccionar y poner proporciones de los fármacos; y en ese caso lo vendería en su valor proporcional. Implementar un algoritmo greedy que obtenga los fármacos (y cantidades) que Rizzoli debe robarse para obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta familia no se aceptan los robos a medias). Justificar por qué el algoritmo propuesto es Greedy y por qué es, en efecto, óptimo. Indicar y justificar la complejidad del algoritmo implementado.
"""
# farmacos [(valor, cantidad ml)]
def robo_farmacos( farmacos , max_cap ):
    farmacos_con_densidad = [
        (v / p, v, p, idx) for idx, (v, p) in enumerate(farmacos)
    ]
    
    # Ordenamos de mayor a menor según la densidad (v / p)
    farmacos_con_densidad.sort(key=lambda x: x[0], reverse=True)

    sol = []
    cant_restante = max_cap

    for densidad, valor, peso, idx in farmacos_con_densidad:
        if cant_restante == 0:
            break
            
        if peso <= cant_restante:
            sol.append((idx, peso))
            cant_restante -= peso
        else:
            sol.append((idx, cant_restante))
            cant_restante = 0

    return sol

"""
El alogritmo es greedy ya que toma deciciones optimas locales para conseguir un solucion optima, dentro de cada estado local elige una decision greedy que es elegir el peso mas grande posible para cada fármaco en la lista hasta que no quepen más. Esto nos dá la ganancia maxima posible ya que anteriormente ordenamos la lista por su valor descendientemente y al ser posible el fraccionamiento de los farmacos podemos siempre elegir el farmaco con mas valor pero fraccionado para poder maximizar la ganancia. 

La complejidad el O(n log n), ya que primero ordenamos la lista de farmacos para poder tenerla con sus valores mas grandes primero lo cual cuesta O(n log n), luego iteramos por la lista agregando la cantidad maxima posible de cada farmaco considerando la maxima capacidad lo cual es O(n)

por lo que el total nos da O(n log n) + O(n) ==> O(n log n)
"""


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

def set_ind_max_camino(grafo, valores_dict):

    vertices = grafo.obtener_vertices()
    n = len(vertices)

    if n == 0:
        return []
    if n == 1:
        return [vertices[0]]

    dp = [0] * n
    dp[0] = valores_dict[vertices[0]]
    dp[1] = max(valores_dict[vertices[0]], valores_dict[vertices[1]])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + valores_dict[vertices[i]])

    solucion = []
    i = n - 1
    while i >= 0:
        if i == 0:
            solucion.append(vertices[0])
            break
        elif i == 1:
            if dp[1] == valores_dict[vertices[1]]:
                solucion.append(vertices[1])
            else:
                solucion.append(vertices[0])
            break
        else:
            if dp[i] == dp[i - 2] + valores_dict[vertices[i]]:
                solucion.append(vertices[i])
                i -= 2 
            else:
                i -= 1 

    solucion.reverse()
    return solucion

