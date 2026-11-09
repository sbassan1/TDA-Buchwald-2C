
# Ejercicio 1

> Manejamos un negocio que atiende clientes en Atenas y en Roma. Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: A y R, con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad, y al siguiente en una distinta, habrá un costo fijo C por la mudanza. Dados los arreglos de costos de operación en Atenas (A) y Roma (R), implementar un modelo de programación lineal que determine qué meses se operará desde Atenas, y en cuáles desde Roma, de forma de minimizar el costo total. Indicar la cantidad de inecuaciones.

---

### Constantes:

- $A$ : array de Atenas con costos de operación
- $R$ : array de Roma con costos de operación
- $c$ : costo fijo de mudarse



### Variables de Decisión:

- $X_i \in \{0,1\}$ : variable binaria de desición que indica si operamos en el mes i en Atenas
- $Y_i \in \{0,1\}$ : variable binaria de desición que indica si operamos en el mes i en Roma
- $M_{A,i} \in \{0,1\}$: Vale $1$ si en el mes $i$ nos mudamos hacia Atenas (es decir, en $i-1$ estábamos en Roma y en $i$ operamos en Atenas), y $0$ en otro caso.
- $M_{R,i} \in \{0,1\}$: Vale $1$ si en el mes $i$ nos mudamos hacia Roma (en $i-1$ estábamos en Atenas y en $i$ operamos en Roma), y $0$ en otro caso
### Funcion Objetivo:

 - $\min \sum_{i=1}^{n} (A_i \cdot X_i + R_i \cdot Y_i) + \sum_{i=2}^{n} C \cdot (M_{A,i} + M_{R,i})$

### Restricciones:

No podemos estar en ambas ciudades cada mes
- $\forall i \in \{1,..,n\} : X_i + Y_i = 1$

Por cada mes de la mudanza empezando desde el 2do mes, nos mudamos si $X_i - X_{i-1}$ es 0
- $\forall i \in \{2, \dots, n\}: M_{A,i} \geq X_i - X_{i-1}$
- $\forall i \in \{2, \dots, n\}: M_{R,i} \geq Y_i - Y_{i-1}$