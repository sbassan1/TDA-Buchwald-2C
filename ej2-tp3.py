
"""
Los hermanos siguieron creciendo. Mateo también aprendió sobre programación dinámica, y cada uno aplicaba la lógica sabiendo que el otro también lo hacía. El juego de las monedas se tornó aburrido en cuánto notaron que siempre ganaba quien empezara, o según la suerte. Los años pasaron, llegó la adolescencia y empezaron a tener gustos diferentes. En general, jugaban a juegos individuales. En particular, Sophia estaba muy enganchada con el siguiente juego de tipo puzzle: El juego consiste de una grilla de n×mn×m celdas. Cada celda puede estar vacía, estar ocupada por una piedra verde, o estar ocupada por una piedra celeste. El objetivo original del juego es remover algunas de las piedras de tal forma que las piedras que quedan cumplan las siguientes condiciones:

    Cada fila tiene al menos una piedra.
    Ninguna columna tiene piedras de ambos colores.

Para algunos estados iniciales esto puede ser imposible. Por ejemplo, el siguiente tablero no tiene solución:

*Imagen de tablero*

La segunda fila obliga a que la primera columna quede celeste, con lo cual la primera fila solo puede quedar con la piedra celeste de la tercera columna. Pero la tercera fila solo tiene la piedra verde de la tercera columna, por lo que esa columna tendría que quedar con ambos colores.

A Sophia le interesa tanto esta versión, como también aquella que relaja la primera restricción, obteniendo una solución que maximice la cantidad de fila que cumplen la restricción (manteniendo siempre la segunda restricción). Es decir, minimizar la cantidad de filas que quedan vacías.
"""

# En este verificamos que solo aplique la 2da condicion:
#   Ninguna columna tiene piedras de ambos colores.

def verificador_relajado(grilla: list[list[str]]) -> bool:
    if not grilla or not grilla[0]:
        return True

    m = len(grilla[0])
    COLORES = ['V', 'C']

    hay_verde_col = [False] * m
    hay_celeste_col = [False] * m
    
    for fila in grilla:
        for j, color in enumerate(fila):
            if color not in COLORES and color != ".":
                return False

            if color == "V":
                hay_verde_col[j] = True
            elif color == "C":
                hay_celeste_col[j] = True

            # Si una columna tiene ambos colores, es inválida.
            if hay_verde_col[j] and hay_celeste_col[j]:
                return False

    return True

def sol_opt(grilla):

    n = len(grilla)
    l = len(grilla[0])

    COLORES = ['V' , 'C']

    puntos = []

    for i in range(n):
        for j in range(l):
            if grilla[i][j] in COLORES:
                puntos.append((i,j))

    

    return sol_bt(grilla, puntos, i,len(puntos), [])

def cant_filas_validas(grilla):    
    i = 0
    for fila in grilla:
        tiene_piedra = any(celda != "." for celda in fila)
        if tiene_piedra:
            i += 1
            
    return i

def sol_bt(grilla, puntos, i, n, mejor_sol):

    if i == n:
        if verificador_relajado(grilla):
            if mejor_sol is None or cant_filas_validas(grilla) > cant_filas_validas(mejor_sol):
                return [fila[:] for fila in grilla] # Es una copia exacta de grilla, ya que grilla es mutable
        return mejor_sol # Si hay optima la devolvemos

    x, y = puntos[i]
    color_original = grilla[x][y]  # Guardamos el color para restaurarlo después

    # Mantener la piedra
    mejor_sol = sol_bt(grilla, puntos, i + 1, n, mejor_sol)

    #Remover la piedra
    grilla[x][y] = "."
    mejor_sol = sol_bt(grilla, puntos, i + 1, n, mejor_sol)

    grilla[x][y] = color_original

    return mejor_sol