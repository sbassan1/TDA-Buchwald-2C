"""
Dada una matriz de 9x9, implementar un algoritmo por backtracking que llene la matriz con números del 1 al 9, dadas las condiciones del Sudoku (si es posible). Las condiciones son:
(i) Las celdas están dispuestas en 9 subgrupos de 3x3.
(ii) Cada columna y cada fila no puede repetir número.
(iii) Cada subgrupo de 3x3 no puede repetir número.

Las posiciones de la matriz con valor 0 se espera que se completen, las posiciones con valores entr 1 y 9 no deben modificarse.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

Métodos del grafo:
Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str
"""

def resolver_sudoku(matriz):
    resolver_sudoku_rec(matriz, 0, 0)
    return matriz


def resolver_sudoku_rec(matriz, x, y):

    if y == 9: # Si llegamos al fin de la matriz sin dar False terminamos con el sudoku completo
        return True

    if x == 8: # Si llegamos al final de la columna bajamos a la sig file
        siguiente_x = 0
        siguiente_y = y + 1
    else: # Si no avanzamos a la sig columna
        siguiente_x = x + 1
        siguiente_y = y

    if matriz[x][y] != 0: # Si la posicion ya contiene un numero, avanzamos al sig casillero
        return resolver_sudoku_rec(matriz, siguiente_x, siguiente_y)

    valores_posibles = chequear_valores_faltan(x, y, matriz) # Chequeamos que numeros faltan para cumplir

    for num in valores_posibles:
        matriz[x][y] = num
        if resolver_sudoku_rec(matriz, siguiente_x, siguiente_y):
            return True
        matriz[x][y] = 0

    return False


def chequear_valores_faltan(x: int, y: int, matriz: list[list[int]]) -> list[int]:
    numeros_tomados = set()
    for i in range(9):
        if matriz[x][i] != 0:
            numeros_tomados.add(matriz[x][i])
        if matriz[i][y] != 0:
            numeros_tomados.add(matriz[i][y])

    inicio_fila = (x // 3) * 3
    inicio_col = (y // 3) * 3

    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if matriz[i][j] != 0:
                numeros_tomados.add(matriz[i][j])

    todos_los_numeros = set(range(1, 10))
    return list(todos_los_numeros - numeros_tomados)
