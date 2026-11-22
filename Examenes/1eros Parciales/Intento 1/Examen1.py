"""
# Ejercicio 1
    Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor xi. Todos los xi son valores diferentes. Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta (es decir, los hijos que tenga y su padre, si tiene). Implementar un algoritmo por división y conquista que obtenga algún mínimo local del árbol en O(log n). Justificar apropiadamente la complejidad del algoritmo implementado.

    Considerar que el árbol tiene en su estructura el nombre del nodo, su valor, y las referencias a sus hijos izquierdo y derecho.
"""

# Si un nodo no es el minimo nos fijamos en el hijo que tiene menos valor de ellos y continuamos de ese lado hasta conseguir un minimo local
# Supongo que existe una funcion que me devuelva el primer nodo, como maximo tenemos que si buscamos hasta una hoja tendremos O(log n) de pasos

def minimo_local(arbol):
    actual = arbol

    while True:
        menor_hijo = None

        # Si hay hijo izq lo usamos como el menor
        if actual.izq is not None:
            menor_hijo = actual.izq

        # Si hay hijo der
        if actual.der is not None:
            # y es menor al izq -> el menor es el der
            if menor_hijo is None or actual.der.valor < menor_hijo.valor:
                menor_hijo = actual.der

        # Si elegimos menor hijo y este es menor al actual el actual es potencialmente
        # un minimo local, si no es minimo local y devolvemos 
        if menor_hijo is not None and menor_hijo.valor < actual.valor:
            actual = menor_hijo
        else:
            return actual
        

"""
Esto nos dá una complejidad de T(N) = 1T(n/2) + O(n^0) : a = 1, b = 2, c = 0
Por lo que nos da: log2 1 = 0 y c = 0, estamos en el segundo caso por lo que la complejidad nos dará O(n^(0) log n) ==> O(log n)
"""

"""
# Ejercicio 2
    El explorador Roberto se embarcó en una misión para encontrar el legendario Templo de los Vientos. En el vasto desierto, hay oasis donde puede recoger provisiones esenciales como agua y comida. Cada oasis tiene recursos limitados. Sin suficientes provisiones, Roberto no podrá cruzar el desierto. Sólo vamos a considerar el hecho de tener k cantidad de provisiones (no si son una cosa u otra). Implementar un algoritmo greedy que permita a Roberto llegar al templo con la menor cantidad de paradas posibles en los oasis. Indicar y justificar la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo. Datos que se reciben:

    - Una lista de n elementos que nos indica cuántas provisiones (en cantidad) se pueden conseguir en cada uno de los n oasis.
    - Una lista con las distancias del inicio de la travesía al primer oasis, del primero al segundo, del segundo al tercero, y así hasta el f
    inal de la travesía (la lista tiene n + 2 elementos).
    - La cantidad de provisiones iniciales de Roberto.
    - Una constante KM_PROVISION que indica cuántas provisiones se debe consumir para caminar un KM.
"""

"""
Avanzamos añadiendo paradas a un max heap, si no llegamos con nuestras prov actuales, rellenamos las proviciones con las paradas anteriores hasta que podamos avanzar. Esto es optimo ya que nos aseguramos de minimizar la cantidad de paradas posibles con las opciones disponibles hasta el momento con cada avance.
"""

import heapq

def ej2(provisiones, distancias, prov_iniciales, km_provision):
    disponibles = []
    paradas = []
    provisiones_actuales = prov_iniciales

    for i, distancia in enumerate(distancias):
        costo = distancia * km_provision
        provisiones_actuales -= costo

        if i < len(provisiones):
            heapq.heappush(disponibles, (-provisiones[i], i))

        while provisiones_actuales < 0:
            if not disponibles:
                return -1

            _, oasis = heapq.heappop(disponibles)
            provisiones_actuales += provisiones[oasis]
            paradas.append(oasis)

    return paradas

"""
# Ejercicio 3
    Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar la máxima cantidad de charlas a dar de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas (devolviendo las charlas que logran esto). Resolver el problema de Interval Scheduling utilizando backtracking.
"""

def ej3(charlas):
    # Devuelve la lista de charlas elegidas que maximiza la cantidad
    return backtracking_charlas(charlas, 0, [], [])


def es_compatible(charla, solucion):
    # Si no hay charlas elegidas, siempre es compatible
    if not solucion:
        return True
    
    # Supone que cada charla es una tupla/lista: (inicio, fin)
    fin_ultima = solucion[-1][1]
    inicio_nueva = charla[0]
    
    # Es compatible si la nueva empieza cuando o después de que termina la última
    return inicio_nueva >= fin_ultima


def backtracking_charlas(charlas, i, sol, mejor):
    if i == len(charlas):
        if len(sol) > len(mejor):
            return sol.copy()
        return mejor

    if len(sol) + (len(charlas) - i) <= len(mejor):
        return mejor

    charla = charlas[i]

    if es_compatible(charla, sol):
        sol.append(charla)
        mejor = backtracking_charlas(charlas, i + 1, sol, mejor)
        sol.pop()

    mejor = backtracking_charlas(charlas, i + 1, sol, mejor)

    return mejor

"""
# Ejercicio 4
    Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso (para ella) que pueda y que entre en su mochila. Tiene 2 limitaciones. La primera: no puede guardar más peso que lo que permita su mochila (tiene límite hasta W). La segunda: como sabe que puede entrar en un estado de locura e inconciencia temporal, se puso un límite que no comprará por más de P precio en total (es decir, la suma de todo lo comprado). Cada producto tiene 3 valores asociados: su valor (vi, que Laura definió en base a su subjetividad), su precio (pi) y su peso (wi).

    Implementar un algoritmo que, utilizando programación dinámica, permita determinar qué productos debe comprar Laura tal que no superen el peso máximo que puede llevar y el precio máximo dispuesto a pagar, y que logre maximizar el valor obtenido (dados por la suma de los elementos comprados). También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
Dos limitaciones:
- no puede guardar mas W peso que lo que tiene en la mochila
- no gastará mas de P cantodad 
"""

"""
OPT(i,w,p):
    if w >= W or p >= P: OPT(i+1, w , p)
    else : max(OPT(i+1, w + w_i, p + p_i), OPT(i+1, w , p))
"""

def ej4(productos, W, P):
    n = len(productos)

    # dp[i][w][p]: valor máximo desde el ítem i hasta n-1 con peso acumulado w y precio p
    dp = [
        [[0] * (P + 1) for _ in range(W + 1)]
        for _ in range(n + 1)
    ]

    # Llenado bottom-up desde el último producto hacia el primero
    for i in range(n - 1, -1, -1):
        vi, wi, pi = productos[i]
        for w in range(W + 1):
            for p in range(P + 1):
                # Opción 1: no comprar el producto i
                mejor = dp[i + 1][w][p]

                # Opción 2: comprar el producto i si entra en peso y presupuesto
                if w + wi <= W and p + pi <= P:
                    tomar = vi + dp[i + 1][w + wi][p + pi]
                    if tomar > mejor:
                        mejor = tomar

                dp[i][w][p] = mejor

    return dp
    
def recontruccion(productos, W, P, dp):
    n = len(productos)
    # Reconstrucción de los productos elegidos
    seleccionados = []
    w, p = 0, 0
    for i in range(n):
        vi, wi, pi = productos[i]
        if w + wi <= W and p + pi <= P:
            # Si tomar el producto i alcanza el mismo valor óptimo que dp[i][w][p],
            # significa que forma parte de una solución óptima
            if dp[i][w][p] == vi + dp[i + 1][w + wi][p + pi]:
                seleccionados.append(i)
                w += wi
                p += pi

    return dp[0][0][0], seleccionados