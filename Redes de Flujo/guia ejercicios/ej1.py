
print(
"""
Explicar para cada uno de los siguientes casos, qué modificaciones se deben aplicar sobre una red para convertirla en una red de flujo apta para la utilización del algoritmo de Ford-Fulkerson.

a. En la red existen bucles.
b. En la red hay ciclos de dos vértices (aristas antiparalelas).
c. En la red hay más de una fuente.
d. En la red hay más de un sumidero.

---

A) Debemos eliminar aristas que causen un ciclo dentro de la red 
B) Dividir una de las dos aristas agregando un vertice de por medio con la capacidad original de la arista
C) Introducimos un nodo fuente padre que se conecte a todos los vertices fuente, la capacidad de todas las aristas del nodo padre a las fuentes debe ser infinita.
D) Introducimos un sumidero total que es conectada de todos los sumideros, que existen, su capacidad debe ser infinita.

"""
)