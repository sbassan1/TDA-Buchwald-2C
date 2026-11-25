

"""
 Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar, utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n. Indicar y justificar la complejidad del algoritmo implementado. Ejemplos: n = 0 –> Debe devolver 1 (no moverse) n = 1 –> Debe devolver 1 (paso de 1) n = 2 –> Debe devolver 2 (dos pasos de 1, o un paso de 2) n = 3 –> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2) n = 4 –> Debe devolver 7 n = 5 –> Debe devolver 13
"""
"""
OPT(i) = {
    0 : i == 0
    1 : i == 1
    2 : i == 2
    4 : i == 3
    (OPT(i-1)+OPT(i-2)+OPT(i-3)) : i >= 4
}
"""

def maneras_distintas(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    a = 1  # Formas para n=1
    b = 2  # Formas para n=2
    c = 4  # Formas para n=3

    for _ in range(4, n + 1):
        siguiente = a + b + c
        a = b
        b = c
        c = siguiente

    return c

print(maneras_distintas(20))
