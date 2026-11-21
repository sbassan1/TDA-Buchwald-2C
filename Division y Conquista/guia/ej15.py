"""Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

a. Escribir un algoritmo de división y conquista, para determinar cuál es la verdadera joya de la corona. Suponer que hay una función balanza(grupo_de_joyas1, grupo_de_joyas2) que devuelve 0 si ambos grupos pesan lo mismo, mayor a 0 si el grupo1 pesa más que el grupo2, y menor que 0 si pasa lo contrario, y realiza esto en tiempo constante. 

b. Indicar y justificar (adecuadamente) la complejidad de la función implementada."""


# a)

def encontrar_joya(cofre, balanza_fn):
    return rec(cofre, 0, len(cofre))



def rec(cofre,inicio: int, fin: int) -> int:
    cantidad = fin - inicio
    if cantidad == 1:
        return inicio

    mitad = cantidad // 2

    # Dos grupos disjuntos de igual tamaño: 'mitad' elementos cada uno
    g1_ini, g1_fin = inicio, inicio + mitad
    g2_ini, g2_fin = inicio + mitad, inicio + 2 * mitad

    peso = balanza_fn(cofre[g1_ini:g1_fin], cofre[g2_ini:g2_fin])

    if peso > 0:
        return rec(cofre, g1_ini, g1_fin)
    if peso < 0:
        return rec(cofre, g2_ini, g2_fin)

    # Si pesan igual y había cantidad impar, el elemento sobrante es el último
    if cantidad % 2 == 1:
        return fin - 1
    
# b)

"""
Segun el teorema maestro A = 1 , B = 2, C = 1. Ya que dividimos el prob en dos, hacemos una llamada por paso y el mergeo se hace constante con una comparacion o la funcion balanza

T(N) = 1 * T(n/2) + O(1) ==> O(Log n)
"""