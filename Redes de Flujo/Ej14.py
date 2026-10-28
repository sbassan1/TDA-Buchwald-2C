
"""
Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante |es miembro de 0 o más clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: 
    - cada partido político no puede tener más de n/2 simpatizantes en la comisión, 
    - cada persona puede representar a solo un club, 
    - cada club debe estar representado por un miembro. 

Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos dé una lista de representantes válidos (Para RPL, lo volvemos diccionario para que el orden no afecte los resultados de las pruebas, y poder consultar fácilmente). Indicar y justificar la complejidad del algoritmo implementado.
Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp) ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.
Información de los miembros

miembro: {
    nombre: string con el nombre del miembro -> 1
    clubes: lista con los nombres (strings) de los clubes a los que pertenece -> 0 ... *
    partido_politico: nombre (string) del partido político al que está afiliado -> 1
}

Se puede asumir que cada club tiene al menos un miembro asociado. 
"""

"""
Voy a modelar la red de esta manera:

Tendre un nodo fuente y sumidero, y nodos clubes, miembros, partidos:

- El nodo tendra aristas a todos los clubes de peso 1
- Cada club se conectará con peso 1 a sus miembros
- Cada miembro se conectará con peso 1 a sus partidos
- Y por ultimo cada partido se conectara al sumidero con capacidad n/2. 

Esto nos dará un flujo que determinara que miembro es compatible para ser representantes, considerando el limite de alifiados de un solo partido politico. Para encontrar los representantes de cada club tendremos que aplicar el algoritmo de flujo máximo y tomar los vertices miembros tales que la arista (miembro, partido) ó (club, miembro), seá 1.

"""

from ff import flujo
from grafo import Grafo


def agregar_vert(vert, usados, red):
    if vert not in usados:
        red.agregar_vertice(vert)
        usados.add(vert)

def representantes(miembros):

    n = len(miembros) # Cantidad total de miembros

    if n == 0:
        return {}

    red = Grafo(True)
    s, t = 'S', 'T'
    
    vert_usados = set() 
    agregar_vert(s, vert_usados, red)
    agregar_vert(t, vert_usados, red)

    clubes_unicos = set()
    partidos = set()

    for miembro in miembros:  # O(M)

        nombre_miem = ('miembro', miembro.nombre)
        agregar_vert(nombre_miem, vert_usados, red)

        partido = ('partido', miembro.partido_politico)
        agregar_vert(partido, vert_usados, red)
        red.agregar_arista(nombre_miem, partido, 1)
        partidos.add(miembro.partido_politico)

        for club_nombre in miembro.clubes: # O(C) con C <= M
            club = ('club', club_nombre)
            clubes_unicos.add(club_nombre)
            agregar_vert(club, vert_usados, red)
            
            red.agregar_arista(club, nombre_miem, 1)
    # O(M*C) => O(M^2)

    for club_nombre in clubes_unicos: # O(C) con C <= M
        club = ('club', club_nombre)
        red.agregar_arista(s, club, 1)
    # O(C)

    limite_partido = len(clubes_unicos) // 2

    for p in partidos: # O(P) con P <= M
        partido = ('partido', p)
        red.agregar_arista(partido, t, limite_partido)
    # O(P)

    f = flujo(red, s, t) # O( (C+M+P) + E^2) ==> O(V + E^2) 
    
    flujo_total = sum(f.get((s, ('club', c)), 0) for c in clubes_unicos)
    if flujo_total < len(clubes_unicos):
        return None
    
    representantes_dict = {}
    for club_nombre in clubes_unicos: # O(C)
        club = ('club', club_nombre)
        encontro_representante = False
        
        for miembro_vert in red.adyacentes(club): # O(M)
            if f.get((club, miembro_vert), 0) > 0:
                nombre_representante = miembro_vert[1] # Arista ('miembro', nombre)
                representantes_dict[nombre_representante] = club_nombre
                encontro_representante = True
                break
        
        if not encontro_representante:
            return None
    # O(M^2) por O(C*M) 

    return representantes_dict 

# El algoritmo tiene una complejidad de O(M^2 + M*E^2)