
import random
import time

def verificador_relajado(grilla: list[list[str]]) -> bool:
    if not grilla or not grilla[0]:
        return True

    m = len(grilla[0])
    COLORES = ['V', 'C']

    hay_verde_col = [False] * m
    hay_celeste_col = [False] * m
    
    for fila in grilla:
        for j, color in enumerate(fila):

            if color == "V":
                hay_verde_col[j] = True
            elif color == "C":
                hay_celeste_col[j] = True

            # Si una columna tiene ambos colores, es inválida.
            if hay_verde_col[j] and hay_celeste_col[j]:
                return False

    return True


def cant_filas_no_vacias(grilla) -> int:    
    count = 0
    for fila in grilla:
        if any(celda != "." for celda in fila):
            count += 1
    return count


def sol_opt(grilla):
    n = len(grilla)
    l = len(grilla[0])
    COLORES = ['V', 'C']
    puntos = []

    for i in range(n):
        for j in range(l):
            if grilla[i][j] in COLORES:
                puntos.append((i, j))

    return sol_bt(grilla, puntos, 0, len(puntos), None)


def sol_bt(grilla, puntos, idx, total_puntos, mejor_sol):

    # Si mejor_sol ya logró cubrir todas las filas, no se puede mejorar
    if mejor_sol is not None and cant_filas_no_vacias(mejor_sol) == len(grilla):
        return mejor_sol

    # Si llegamos al final y la grilla es valida comparamos con la mejor sol
    if idx == total_puntos:
        if verificador_relajado(grilla):
            if mejor_sol is None or cant_filas_no_vacias(grilla) > cant_filas_no_vacias(mejor_sol):
                return [fila[:] for fila in grilla]
        return mejor_sol

    x, y = puntos[idx]
    color_original = grilla[x][y]

    # Mantenemos la piedra
    mejor_sol = sol_bt(grilla, puntos, idx + 1, total_puntos, mejor_sol)

    # Eliminamos la piedra
    grilla[x][y] = "."
    mejor_sol = sol_bt(grilla, puntos, idx + 1, total_puntos, mejor_sol)

    # Restauramos la piedra para hacer BT
    grilla[x][y] = color_original

    return mejor_sol


tablero_3x3 = [
    ["V", ".", "."],
    [".", "C", "."],
    ["V", ".", "."]
]

tablero_4x4 = [
    ["C", ".", ".", "."],
    [".", "V", ".", "."],
    [".", ".", "V", "."],
    [".", ".", ".", "C"]
]

tablero_5x5 = [
    ["V", ".", ".", ".", "."],
    [".", ".", "C", ".", "."],
    ["V", ".", ".", ".", "."],
    [".", ".", ".", "V", "."],
    [".", ".", ".", ".", "C"]
]

tablero_6x6 = [
    ["C", ".", ".", ".", ".", "."],
    [".", "V", ".", ".", ".", "."],
    [".", ".", "C", ".", ".", "."],
    [".", "V", ".", ".", ".", "."],
    [".", ".", ".", ".", "V", "."],
    [".", ".", ".", ".", ".", "C"]
]

tests = [ 
    ("3x3", tablero_3x3),
    ("4x4", tablero_4x4),
    ("5x5", tablero_5x5),
    ("6x6", tablero_6x6)
]

def agregar_piedras_azar(tablero):

    copia = [fila[:] for fila in tablero]
    n = len(copia)
    m = len(copia[0]) if n > 0 else 0

    for j in range(m):
        # Buscar las filas vacías en la columna j
        vacias = [i for i in range(n) if copia[i][j] == "."]
        
        if vacias:
            # Elegir al azar cuántas agregar (mínimo 1, máximo dejando al menos 1 libre si es posible)
            max_agregar = max(1, len(vacias) - 1)
            cantidad = random.randint(1, max_agregar)
            
            for i in random.sample(vacias, cantidad):
                copia[i][j] = random.choice(["V", "C"])

    return copia


def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)

muestras_por_tamano = 5

for nombre, tablero_base in tests:
    tiempos = []
    print(f"--- Evaluando tableros {nombre} ---")

    print(f"Tablero base: \n")
    mostrar_tablero(tablero_base)
    print("\n")
    
    for i in range(muestras_por_tamano):
        muestra = agregar_piedras_azar(tablero_base)
        
        inicio = time.perf_counter()
        solucion = sol_opt(muestra)
        fin = time.perf_counter()
        
        tiempo_ms = (fin - inicio) * 1000
        tiempos.append(tiempo_ms)
        
        es_valida_col = verificador_relajado(solucion)        
        assert es_valida_col, f"Error: La solución en {nombre} viola la regla de columnas."
        
        print(f"  Muestra {i+1}: {tiempo_ms:8.4f} ms | Correcta: OK ")
        
    promedio = sum(tiempos) / len(tiempos)
    print(f"Promedio {nombre}: {promedio:.4f} ms\n")