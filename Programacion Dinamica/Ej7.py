"""
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
rec(i,w) == {
    si i == 0 o w == 0 => 0
    si elementos[i][1] > W => rec(i-1, w)
    otro caso ==> max(rec[i - 1][w], elementos[i - 1][0] + rec[i - 1][w - elementos[i - 1][1]])
}

"""

# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):

    n = len(elementos)

    mem = [ [0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        valor, peso = elementos[i - 1]
        for w in range(1, W + 1):
            if peso > w: # Si no hay espacio
                mem[i][w] = mem[i - 1][w] # Pasamos al siguiente
            else:
                mem[i][w] = max(mem[i - 1][w], valor + mem[i - 1][w - peso]) # Elegimos entre tomarlo o no

    solucion = []
    peso_restante = W
    for i in range(n, 0, -1):
        if mem[i][peso_restante] != mem[i - 1][peso_restante]:
            valor, peso = elementos[i - 1]
            solucion.append(elementos[i - 1])
            peso_restante -= peso

    solucion.reverse()

    return solucion
