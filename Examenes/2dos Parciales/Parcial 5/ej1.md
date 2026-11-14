
# Ejercicio 1

> El problema de Hitting Set Relajado es el mismo problema que Hitting Set, pero en el cual se permite que hayan hasta K conjuntos que no hayan sido “hitteados” (es decir, que ninguno de sus elementos sea parte del Hitting Set). Implementar un modelo de programación lineal que permita obtener un Hitting Set Relajado de tamaño mínimo (el valor de K pueden asumir que está definido en algún lado como una constante). Indicar la cantidad de inecuaciones definidas.

---

### Constantes:

- $ U $ : El universo de elementos 
- $ C $ : El conjunto de elementos  $\in U$
- $ K $ : Cantidad máxima de conjuntos que se permite no hittear

### Variables de Decisión:

- $X_i \in \{0,1\}$ : Decide si se selecciona el conjunto i $\in U$
- $Y_i \in \{0,1\}, \forall j \in \{1,..,m\}$ : Decide si el conjunto j $\in C$ fue hitteado  

### Funcion Objetivo:

$$ min (\sum_{i \in U}^{} X_i) $$

### Restricciones:

$\forall j \in C: \sum_{i \in S_j} x_i + y_j \ge 1 \quad \forall j \in \{1, \dots, m\}$

La cantidad de elementos hitteados no pueden ser mayores a K

$\sum_{j=1}^{m} y_j \le K$
