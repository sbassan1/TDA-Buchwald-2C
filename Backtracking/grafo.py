
import random

class Grafo:
    def __init__(self, dirigido=False, vertices_init=None):
        self.dirigido = dirigido
        # Estructura: { vertice: { adyacente: peso } }
        self.grafo = {}

        if vertices_init:
            for v in vertices_init:
                self.agregar_vertice(v)

    def agregar_vertice(self, v):
        if v not in self.grafo:
            self.grafo[v] = {}

    def borrar_vertice(self, v):
        if v in self.grafo:
            # Eliminar referencias a v en otros vértices
            for ady in list(self.grafo[v].keys()):
                del self.grafo[ady][v]
            del self.grafo[v]

    def agregar_arista(self, v, w, peso=1):
        if v not in self.grafo:
            self.agregar_vertice(v)
        if w not in self.grafo:
            self.agregar_vertice(w)

        self.grafo[v][w] = peso
        if not self.dirigido:
            self.grafo[w][v] = peso

    def borrar_arista(self, v, w):
        if self.estan_unidos(v, w):
            del self.grafo[v][w]
            if not self.dirigido and v in self.grafo[w]:
                del self.grafo[w][v]

    def estan_unidos(self, v, w):
        return v in self.grafo and w in self.grafo[v]

    def peso_arista(self, v, w):
        if self.estan_unidos(v, w):
            return self.grafo[v][w]
        return None

    def obtener_vertices(self):
        """Devuelve una lista con todos los vértices del grafo."""
        return list(self.grafo.keys())

    def vertice_aleatorio(self):
        """Devuelve un vértice aleatorio del grafo."""
        vertices = self.obtener_vertices()
        if not vertices:
            return None
        return random.choice(vertices)

    def adyacentes(self, v):
        """Devuelve una lista con los vértices adyacentes a v."""
        if v in self.grafo:
            return list(self.grafo[v].keys())
        return []

    def __str__(self):
        res = []
        for v in self.grafo:
            ady = ", ".join(f"{w}({peso})" for w, peso in self.grafo[v].items())
            res.append(f"{v} -> [{ady}]")
        return "\n".join(res)
