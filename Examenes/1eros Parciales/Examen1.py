"""
# Ejercicio 1
    Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor xi. Todos los xi son valores diferentes. Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta (es decir, los hijos que tenga y su padre, si tiene). Implementar un algoritmo por división y conquista que obtenga algún mínimo local del árbol en O(log n). Justificar apropiadamente la complejidad del algoritmo implementado.

    Considerar que el árbol tiene en su estructura el nombre del nodo, su valor, y las referencias a sus hijos izquierdo y derecho.
"""

# Si un nodo no es el minimo nos fijamos en el hijo que tiene menos valor de ellos y continuamos de ese lado hasta conseguir un minimo local

def ej1(arbol):
    if not arbol:
        return None
    return minimo_local(arbol, None)

def minimo_local(arbol, padre):
    val_padre = padre.valor if padre else float('inf')
    val_izq = arbol.izq.valor if arbol.izq else float('inf')
    val_der = arbol.der.valor if arbol.der else float('inf')

    if arbol.valor < val_padre and arbol.valor < val_izq and arbol.valor < val_der:
        return arbol.valor

    if val_izq < arbol.valor and val_izq < val_der:
        return minimo_local(arbol.izq, arbol)
    else:
        return minimo_local(arbol.der, arbol)

"""
Esto nos dá una complejidad de T(N) = 1T(n/2) + O(n^0) : a = 1, b = 2, c = 0
Por lo que nos da: log2 1 = 0 y c = 0, estamos en el segundo caso por lo que la complejidad nos dará O(n^(0) log n) ==> O(log n)
"""

"""
# Ejercicio 2
    El explorador Roberto se embarcó en una misión para encontrar el legendario Templo de los Vientos. En el vasto desierto, hay oasis donde puede recoger provisiones esenciales como agua y comida. Cada oasis tiene recursos limitados. Sin suficientes provisiones, Roberto no podrá cruzar el desierto. Sólo vamos a considerar el hecho de tener k cantidad de provisiones (no si son una cosa u otra). Implementar un algoritmo greedy que permita a Roberto llegar al templo con la menor cantidad de paradas posibles en los oasis. Indicar y justificar la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo. Datos que se reciben:

    - Una lista de n elementos que nos indica cuántas provisiones (en cantidad) se pueden conseguir en cada uno de los n oasis.
    - Una lista con las distancias del inicio de la travesía al primer oasis, del primero al segundo, del segundo al tercero, y así hasta el
    final de la travesía (la lista tiene n + 2 elementos).
    - La cantidad de provisiones iniciales de Roberto.
    - Una constante KM_PROVISION que indica cuántas provisiones se debe consumir para caminar un KM.
"""

# distancias_oasis[0] = 0, distancias_oasis[n] = fin
# Queremos la menor cantidad de paradas usadas
# Si no es posible llegar al punto entonces devolvemos -1

def ej2(provisiones_oasis, distancias, prov_iniciales, KM_PROVISION):
    req_tramos = [d * KM_PROVISION for d in distancias]

    paradas = []
    prov_actuales = prov_iniciales

    for i in range(len(req_tramos)):
        req = req_tramos[i]

        if prov_actuales < req:
            if i == 0 or provisiones_oasis[i - 1] == 0:
                return -1 # Imposible llegar

            # Recargamos en el oasis i-1 (el último que alcanzamos)
            prov_actuales += provisiones_oasis[i - 1]
            provisiones_oasis[i - 1] = 0 # Marcamos como usado
            paradas.append(i)

            if prov_actuales < req:
                return -1

        prov_actuales -= req

    return paradas

"""
# Ejercicio 3
    Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar la máxima cantidad de charlas a dar de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas (devolviendo las charlas que logran esto). Resolver el problema de Interval Scheduling utilizando backtracking.
"""

def ej3(charlas):
    return backtracking_charlas(charlas, 0, [])

def backtracking_charlas(charlas, i, seleccionadas):

    if i == len(charlas):
        return list(seleccionadas)

    opcion_sin = backtracking_charlas(charlas, i + 1, seleccionadas)
    charla_actual = charlas[i]

    se_solapa = False
    if seleccionadas and charla_actual[0] < seleccionadas[-1][1]:
        se_solapa = True

    opcion_con = []
    if not se_solapa:
        opcion_con = backtracking_charlas(charlas, i + 1, seleccionadas + [charla_actual])

    if len(opcion_con) > len(opcion_sin):
        return opcion_con
    else:
        return opcion_sin

"""
# Ejercicio 4
    Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso (para ella) que pueda y que entre en su mochila. Tiene 2 limitaciones. La primera: no puede guardar más peso que lo que permita su mochila (tiene límite hasta W). La segunda: como sabe que puede entrar en un estado de locura e inconciencia temporal, se puso un límite que no comprará por más de P precio en total (es decir, la suma de todo lo comprado). Cada producto tiene 3 valores asociados: su valor (vi, que Laura definió en base a su subjetividad), su precio (pi) y su peso (wi).

    Implementar un algoritmo que, utilizando programación dinámica, permita determinar qué productos debe comprar Laura tal que no superen el peso máximo que puede llevar y el precio máximo dispuesto a pagar, y que logre maximizar el valor obtenido (dados por la suma de los elementos comprados). También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado.
"""
"""
Ecuacion de recurrencia

mem[i][w][p] = {
    Si wi < w and pi < p => MAX(mem[i-1][w][p], vi + dp[i - 1][w - wi][p - pi])
    Si no mem[i-1][w][p]
}

Complejidad temporal es O(N*W*P)
Complejidad espacial es O(N+W+P)
"""

# Productos: (vi,pi,wi)
# Queremos maximizar el v_total de los productos comprados

def ej4(productos, W):

    n = len(productos)

    # 1. Crear la tabla DP de dimensiones (n+1) x (W+1) x (P+1) inicializada en 0
    dp = [[[0 for _ in range(1000 + 1)] for _ in range(W + 1)] for _ in range(n + 1)]

    # 2. Llenar la tabla Bottom-Up
    for i in range(1, n + 1):
        vi, wi, pi = productos[i - 1]
        for w in range(W + 1):
            for p in range(1000 + 1):
                # Opción por defecto: no incluir el producto i
                dp[i][w][p] = dp[i - 1][w][p]

                # Si entra en el peso y precio actual, evaluamos la mejor opción
                if wi <= w and pi <= p:
                    opcion_comprar = vi + dp[i - 1][w - wi][p - pi]
                    dp[i][w][p] = max(dp[i][w][p], opcion_comprar)

    valor_maximo = dp[n][W][1000]

    comprados = []
    w_restante = W
    p_restante = 1000
    for i in range(n, 0, -1):
        if dp[i][w_restante][p_restante] != dp[i - 1][w_restante][p_restante]:
            vi, wi, pi = productos[i - 1]
            comprados.append(productos[i - 1])
            w_restante -= wi
            p_restante -= pi

    comprados.reverse()
    return valor_maximo, comprados
