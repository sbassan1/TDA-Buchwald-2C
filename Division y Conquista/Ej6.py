"""
Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad mejor que O(n^2). Justificar la complejidad del algoritmo mediante el teorema maestro.
"""

def multiplicar(a,b):

    if a < 10 or b < 10:
        return a * b


    n = max(len(str(a)), len(str(b)))
    m = n // 2

    # Num A = (a+b)
    # Num B = (c+d)
    # A * B ==> (a+b) * (c+d) 
    # => (a+b) * c + (a+b) * d
    # => (ac + bc) + (ad + bd)

    mitad_izq_a , mitad_der_a = divmod(a, 10**m)
    mitad_izq_b , mitad_der_b = divmod(a, 10**m)

    ac = multiplicar(mitad_izq_a, mitad_izq_b)
    ad = multiplicar(mitad_izq_a, mitad_der_b)
    bc = multiplicar(mitad_der_a, mitad_izq_a)
    bd = multiplicar(mitad_der_a, mitad_der_b)

    return ac * (10 **(2*m)) + (ad + bc) * (10 ** m) + bd