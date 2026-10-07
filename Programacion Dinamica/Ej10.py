"""
Manejamos un negocio que atiende clientes en Londres y en California. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo M por la mudanza. Dados los arreglos de costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación. Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado.
"""

def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)
    if n == 0:
        return [], 0

    dp_L = [0] * n # Precio terminar en L en i
    dp_C = [0] * n # Precio terminar en C en i
    dp_L[0] = arreglo_L[0]
    dp_C[0] = arreglo_C[0]

    # Calcular las memo, nos quedamos en la ciudad o nos mudamos
    for i in range(1, n):
        dp_L[i] = arreglo_L[i] + min(dp_L[i - 1], dp_C[i - 1] + costo_M)
        dp_C[i] = arreglo_C[i] + min(dp_C[i - 1], dp_L[i - 1] + costo_M)

    # Ver que ciudad combiene al final
    if dp_L[n - 1] <= dp_C[n - 1]:
        ciudad_actual = 'londres'
        costo_total = dp_L[n - 1]
    else:
        ciudad_actual = 'california'
        costo_total = dp_C[n - 1]

    # Reconstruccion solucion
    secuencia = [''] * n
    secuencia[n - 1] = ciudad_actual
    for i in range(n - 1, 0, -1):
        if ciudad_actual == 'londres':
            if dp_L[i] == dp_L[i - 1] + arreglo_L[i]:
                ciudad_actual = 'Londres'
            else:
                ciudad_actual = 'california'
        else:
            if dp_C[i] == dp_C[i - 1] + arreglo_C[i]:
                ciudad_actual = 'londres'
            else:
                ciudad_actual = 'california'

        secuencia[i - 1] = ciudad_actual

    return secuencia

"""
La complejidad es:
    O(n) para llenar los dp_l y dp_c
    +
    O(n) para reconstruir la solucion
    ----
    O(n)
"""
