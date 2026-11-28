"""
El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas.

a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.
"""

def lista_max_invitados_a(relaciones, invitados):
    
    candidatos = set(invitados) # Set de invitados
    
    # Por cada persona, si la persona esta en invitados, sumamos la cantidad de amigos que estan en candidatos
    grado = {
        persona: sum(amigo in candidatos for amigo in amigos)
        for persona, amigos in relaciones.items()
        if persona in candidatos
    }

    # Lista de candidatos que tienen menos 4 amigos candidatos
    cola = [persona for persona in candidatos if grado.get(persona, 0) < 4]

    # Por cada persona de la cola
    while cola:
        # Persona tiene menos de 4 amigos invitados
        persona = cola.pop()
        
        # Si esta persona ya no esta en invitados continuamos
        if persona not in candidatos:
            continue

        # Eliminamos esta persona de invitados
        candidatos.remove(persona)

        # Eliminamos esta persona de las relaciones en sus amigos, bajandole sus rangos
        for amigo in relaciones.get(persona, []):
            if amigo in candidatos:
                grado[amigo] -= 1
                if grado[amigo] == 4 - 1:
                    cola.append(amigo)

    return list(candidatos)

"""
b. Los organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos solicitan que adicionemos una nueva restricción a la invitación: Sólo puede asistir si NO conoce al menos otras 4 personas invitadas. Modifique su propuesta para satisfacer esta nueva solución.
"""

# TODO Esto está mal

def lista_max_invitados_b(relaciones, invitados):
    
    candidatos = set(invitados) # Set de invitados
    
    # Por cada persona, si la persona esta en invitados, sumamos la cantidad de amigos que estan en candidatos
    grado = {
        persona: sum(amigo in candidatos for amigo in amigos)
        for persona, amigos in relaciones.items()
        if persona in candidatos
    }

    # Lista de candidatos que tienen menos 4 amigos candidatos
    cola = [persona for persona in candidatos if grado.get(persona, 0) < 4]

    # Por cada persona de la cola
    while cola:
        # Persona tiene menos de 4 amigos invitados
        persona = cola.pop()
        
        # Si esta persona ya no esta en invitados continuamos
        if persona not in candidatos:
            continue

        # Eliminamos esta persona de invitados
        candidatos.remove(persona)

        # Eliminamos esta persona de las relaciones en sus amigos, bajandole sus rangos
        for amigo in relaciones.get(persona, []):
            if amigo in candidatos:
                grado[amigo] -= 1
                if grado[amigo] == 4 - 1:
                    cola.append(amigo)

    # Grado esta actualizado, contiene la lista de personas que están invitadas al final
    # Buscamos de todos los invitados originales los que contengan menos de 4 personas que si estan invitadas
    invitados_menos_4 = [persona for persona in invitados if grado.get(persona, 0) < 4]

    return invitados_menos_4