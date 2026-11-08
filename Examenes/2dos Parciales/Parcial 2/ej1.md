
# Ejercicio 1

> Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político. Cada uno de los n clubes debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones: 

- cada partido político no puede tener más de n/2 simpatizantes en la comisión, y además queremos minimizar la cantidad simpatizantes a un mismo partido político; 
- cada persona puede representar a solo un club, 
- cada club debe estar representado por un miembro.

> Implementar un modelo de programación lineal que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen), nos permita obtener los representantes válidos, que además minimicen la cantidad de simpatizantes a un mismo partido político. Indicar la cantidad de inecuaciones definidas en el modelo.

---

### Constantes:

- $M \in \{1,..,n_m\}$ : Miembros 
- $C \in \{1,..,n_m\}$ : Clubes
- $P \in \{1,..,n_m\}$ : Partidos politicos
- $A_{i,j} \in \{0, 1\}$: matriz constante donde $A_{i,j} = 1$ si la persona $i$ pertenece al club $j$, y $0$ en otro caso.
- $B_{i,p} \in \{0, 1\}$: matriz constante donde $B_{i,p} = 1$ si la persona $i$ pertenece al partido $p$, y $0$ en otro caso.



### Variables de Decisión:

- $Y_{i,j} \in \{0,1\}$ : Variable binaria que decide si el miembro i, es miembro del club j y representante 
- $K \geq 0$ : Cantidad de simpatizantes de cualquier partido 

### Funcion Objetivo:

- min(K)

### Restricciones:

Cada persona puede representar a solo un club
- $ \sum_{i \in M}^{} Y_{i,j} * A_{i,j} = 1 \quad \forall j \in C$

Cada club debe estar representado por un miembro
- $ \sum_{j \in C}^{} Y_{i,j} \leq 1 \quad \forall i \in M$

La cantidad total de representantes de un partido $p$ no puede superar $\lfloor n_c / 2 \rfloor$:
- $\sum_{i \in M} \sum_{j \in C} B_{i,p} \cdot X_{i,j} \le \left\lfloor \frac{n_c}{2} \right\rfloor \quad \forall p \in P$

Cota de variable K:
- $\sum_{i \in M} \sum_{j \in C} B_{i,p} \cdot X_{i,j} \le K \quad \forall p \in P$