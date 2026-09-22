
"""
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K,
siendo que las operaciones posibles son:

(i) aumentar el valor del operando en 1;
(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones
a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y
justificar la complejidad del algoritmo implementado.

Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente
ecuación de recurrencia.

Devolver un arreglo de las operaciones a realizar en orden.
En texto cada opción es 'mas1' o 'por2'

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por programación dinámica". Por las características de la
herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
"""

def operaciones(k):

    if k == 0:
        return []

    mem = [0] * (k + 1)
    padre = [-1] * (k + 1)


    for i in range(1,k+1):

        if i % 2 == 0:
            mem[i] = min(mem[i], mem[i // 2] + 1)
            padre[i] = "por2"
        else:
            mem[i] = mem[i - 1] + 1
            padre[i] = "mas1"


    pasos = []
    actual = k
    while actual > 0:
        pasos.append(padre[actual])
        if padre[actual] == "por2":
            actual = actual // 2
        else:
            actual = actual - 1
    pasos.reverse()

    return pasos


print(operaciones(6))
