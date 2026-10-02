"""
Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, determine si existen los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez.
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular).
"""

def knight_tour(n):

    if n == 0:
        return False

    if n == 1:
        return True

    matriz_inicial = ([0] * n for _ in range(n)) 
    return knight_tour_rec(matriz_inicial, 0, 0, n, 0)

def knight_tour_rec(matriz, i, j, n, posiciones_usadas):

    if posiciones_usadas == n * n:
        return True

    if i >= n or j >= n or i < 0 or j < 0: 
        return False

    if matriz[i][j] != 0:
        return False
        
    matriz[i][j] = 1
    
    movimientos = [
        (i + 2, j + 1), (i + 2, j - 1),
        (i - 2, j + 1), (i - 2, j - 1),
        (i + 1, j + 2), (i + 1, j - 2),
        (i - 1, j + 2), (i - 1, j - 2)
    ]

    for sig_i, sig_j in movimientos:
        if matriz[sig_i][sig_j] == 0 and knight_tour_rec(matriz, sig_i, sig_j, n, posiciones_usadas + 1):
            return True     

    matriz[i][j] = 0

    return False
    