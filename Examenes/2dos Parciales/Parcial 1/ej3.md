
> El problema de Camino Hamiltoniano con inicio y fin es el siguiente: Dado un grafo, un vértice de inicio y otro de fin, ¿existe un camino Hamiltoniano dentro del grafo que empiece en el vértice de inicio y termine en el vértice de fin?

> Demostrar que el problema de Camino Hamiltoniano con inicio y fin es un problema NP-Completo. Recomendamos recordar que el problema de Camino Hamiltoniano es un problema NP-Complet

---

Para probar que Camino Hamiltoniano con inicio y fin es NP-Completo debemos probar:

### 1. Que 'Camino Hamiltoniano con inicio y fin' esta dentro de NP
### 2. Que 'Camino Hamiltoniano con inicio y fin' es NP-Hard mediante una reduccion de un problema NP-Completo.
### 3. Demostrar la equivalencia $\iff$

---
### 1) Tenemos que si existe un algoritmo verificador que pruebe en tiempo polinomial $O(N^K)$ para el problema:

Probamos que un Camino es Hamiltoneano si el camino:
- El camino empieza en el vertice de inicio y termina en el de fin
- El camino contiene todos los vertices del grafo
- Un vertice utilizado por el camino no puede repetirse de nuevo.

Todo eso lo podemos probar en O(N^k) facilmente, tenemos una lista de vertices, verificamos que la cantidad de vertices son la misma que las del grafo, y que el primer vertice es el inicio. Luego agregamos el vertice inicio a un set() de ya visitados y iteramos por la lista de vertices del camino. Tenemos que verificar si existe una arista (u,v) en el grafo para cada i < j en $0 <= i <= j <= n$, y iteramos por toda la lista hasta que llegamos al fin, comprobamos que el ultimo vertice del camino es el fin. Si todo cumple entonces tenemos verificado el problema.

La complejidad temporal sería:
```
    verificar que el vertice inicio es el primero O(1)
    Iterar por el camino cada V. O(V)
        Verificar que el vertice esta en el grafo y no esta repetido
        Verificar que el vertice i+1 este en la lista de adjacentes de v.
        Agregar vertice a visitados
```

### 2) Reducir un problema NP-Completo conocido a nuestro problema (NP-Hard)

Para demostrar que el *Camino Hamiltoniano con inicio y fin* es **NP-Hard**, debemos realizar una reducción polinómica desde un problema que ya sabemos que es NP-Completo. Utilizaremos el problema del **Ciclo Hamiltoniano** (HC).

#### Idea de la reducción:
Dado un grafo $G = (V, E)$ en el cual queremos saber si existe un **Ciclo Hamiltoniano**:
1. Elegimos un vértice arbitrario $v \in V$.
2. Construimos un nuevo grafo $G'$ y definimos un vértice de inicio $s$ y un vértice de fin $t$ de la siguiente manera:
   - Eliminamos el vértice $v$ del grafo $G$.
   - Creamos dos nuevos vértices: $s$ (inicio) y $t$ (fin).
   - Para cada vecino $u$ de $v$ en el grafo original $G$, agregamos una arista $(s, u)$ en $G'$.
   - Para cada vecino $w$ de $v$ en el grafo original $G$, agregamos una arista $(w, t)$ en $G'$.
   - El resto de las aristas de $G - \{v\}$ se mantienen intactas en $G'$.

Esta transformación se realiza en tiempo polinómico $O(V + E)$.

---

### 3) Demostración de la equivalencia ($\iff$)

Debemos probar que el grafo original $G$ tiene un Ciclo Hamiltoniano $\iff$ el nuevo grafo $G'$ tiene un Camino Hamiltoniano que empieza en $s$ y termina en $t$.

#### $(\to)$ "Ciclo Hamiltoniano" $\implies$ "Camino Hamiltoniano con inicio y fin ($s, t$)"
Si $G$ tiene un Ciclo Hamiltoniano, este ciclo debe pasar obligatoriamente por el vértice $v$. Por lo tanto, el ciclo entra a $v$ desde uno de sus vecinos $u$ y sale de $v$ hacia otro de sus vecinos $w$. 
Al eliminar $v$, el resto del ciclo forma un camino que visita todos los demás vértices de $G - \{v\}$ exactamente una vez, comenzando en $u$ y terminando en $w$. 
En el grafo $G'$, como conectamos $s$ con $u$ y $w$ con $t$, podemos formar el camino: 
$s \to u \to (\text{camino por todos los vértices restantes}) \to w \to t$. 
Este es un Camino Hamiltoniano válido en $G'$ que empieza en $s$ y termina en $t$.

#### $(\leftarrow)$ "Camino Hamiltoniano con inicio y fin ($s, t$)" $\implies$ "Ciclo Hamiltoniano"
Si $G'$ tiene un Camino Hamiltoniano que empieza en $s$ y termina en $t$, este camino debe tener la forma:
$s \to u \to (\text{camino que visita todos los vértices de } V - \{v\}) \to w \to t$.
Por construcción de $G'$, esto significa que $u$ y $w$ eran vecinos de $v$ en el grafo original $G$, y el segmento intermedio recorre todos los demás vértices de $G$ exactamente una vez. 
Si a este camino le quitamos $s$ y $t$, y reconectamos $u$ y $w$ a través del vértice original $v$ (añadiendo las aristas $(u, v)$ y $(v, w)$), obtenemos un ciclo que pasa por todos los vértices de $V$ exactamente una vez, es decir, un **Ciclo Hamiltoniano** en $G$.

Como el problema del Ciclo Hamiltoniano es NP-Completo, y hemos demostrado que se puede reducir en tiempo polinómico a nuestro problema de *Camino Hamiltoniano con inicio y fin*, concluimos que **Camino Hamiltoniano con inicio y fin es NP-Hard**. Al estar también en NP (por la parte 1), queda demostrado que es **NP-Completo**.