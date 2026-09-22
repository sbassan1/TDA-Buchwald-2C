"""
Ecuacion de recurrencia:

fib(i) = {
    Si i == 0 entonces 1
    Si i == 1 entonces 1
    Si no entonces fib(i-1) + fib(i-2)
}

Complejidad Temporal:

    asignar array y valores iniciales ==> O(1)
    iterar por n, mapeando valores de mem ==> O(n)

Total: O(n)

"""

def fibonacci(n):

    if n == 0:
        return 1
    if n == 1:
        return 1

    mem = [0] * (n + 1)
    mem[0] = 1
    mem[1] = 1

    for i in range(2, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]

    return mem[n]

print(fibonacci(3))
