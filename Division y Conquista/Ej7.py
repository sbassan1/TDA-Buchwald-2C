
from math import sqrt


def distancia_entre_puntos(a,b):
    return sqrt((a[1]-a[0])^2 + (b[1]-b[0])^2)


def puntos_mas_cercanos(puntos):

    puntos = sorted(puntos, key= lambda x : x[0]) # Ordenamos los puntos por el eje x

    return [(0,0), (0,0)]


def puntos_mas_cercanos(puntos, inicio, fin):

    # Si la cantidad de puntos es dos comparo,
