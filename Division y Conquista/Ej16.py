
"""
Sea una matriz A de tamaño n x n, con todos valores distintos. Un índice (i, j) es un máximo local si A[i, j] es estrictamente mayor que todos su vecinos que existan (arriba, abajo, izquierda, derecha). Implementar un algoritmo de División y Conquista que permita encontrar algún máximo local en tiempo O(n). Justificar adecuadamente la complejidad del algoritmo. Prestar mucha atención a la ecuación de recurrencia escrita, ya que esto puede develar un error en el algoritmo planteado.
"""

def es_max_local(x,y,matriz):
    return False

def encontrar_mas_grande(x,y,matriz):
    return x,y

def maximo_local(matriz):
    # devolvemos posiciones i, j donde esta el maximo local
    return (0, 0)

def maximo_local_rec(matriz, ini_x,ini_y,fin_x,fin_y):

    if ini_x == ini_y: # Una matriz de 1 valor
        return ini_x, ini_y

    mid_x = (ini_x + fin_x) // 2
    mid_y = (ini_y + fin_y) // 2

    valor_max = matriz[mid_x][mid_y]
    punto_max = (mid_x, mid_y)

    for x in range(fin_x-ini_x):
        if matriz[x][mid_y] > valor_max:
            punto_max = (x,mid_y)
            valor_max = matriz[x][mid_y]
        
    for y in range(fin_y-ini_y):
        if matriz[mid_x][y] > valor_max:
            punto_max = (mid_x,y)
            valor_max = matriz[mid_x][y]

    if es_max_local(punto_max, valor_max, matriz):
        return punto_max

    ini_x, ini_y, fin_x, fin_y = encontrar_mas_grande(punto_max,matriz) # Si no es el max local busco el cuadrante con el punto mas grande
    
    return maximo_local_rec(matriz, ini_x,ini_y,fin_x,fin_y)