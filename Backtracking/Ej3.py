"""
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

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
def nreinas(n):
    if n <= 0:
        return []

    campo = [[0] * n for _ in range(n)]

    if nreinas_rec(0, n, campo):
        return conseguir_lista_de_reinas(campo,n)
    return []


def nreinas_rec(x, n, campo):
    if x == n:
        return True

    for y in range(n):
        if es_compatible(n, x, y, campo):
            campo[x][y] = 1

            if nreinas_rec(x + 1, n, campo):
                return True

            campo[x][y] = 0

    return False


def es_compatible(n, x, y, campo):

    for i in range(x):
        if campo[i][y] == 1:
            return False
        if y - (x - i) >= 0 and campo[i][y - (x - i)] == 1:
            return False
        if y + (x - i) < n and campo[i][y + (x - i)] == 1:
            return False

    return True

def conseguir_lista_de_reinas(campo,n):
    sol = []
    for x in range(n):
        for y in range(n):
            if campo[x][y]:
                sol.append((x,y))
    return sol


campo = nreinas(6)
print(campo)
