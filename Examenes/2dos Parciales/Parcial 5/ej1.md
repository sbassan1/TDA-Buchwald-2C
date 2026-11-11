
# Ejercicio 1:

> El problema de Bin-Packing es el siguiente: dados n elementos de diferentes pesos pi se quiere ubicar a cada elemento en algún contenedor, donde cada contenedor tiene capacidad máxima M (todos los contenedores tienen la misma capacidad). Suponer que todos los pi son menores o iguales a M.

> Implementar un modelo de programación lineal que permita determinar en qué contenedor va cada elemento, de forma de minimizar la cantidad de contenedores utilizados. Considerar que, como máximo, vas a usar n contenedores (es imposible tener que usar más). Indicar la cantidad de inecuaciones definidas.

---

## 1. Parámetros de Entrada

- $E_i$ : Capacidad del elemento $i$
- $M$ : Capacidad maxima M por cada contenedor

## 2. Variables de Decisión

- $S_{c,i} \in \{0,1\}, \forall c,i \in \{1,..,n\}$ : Nos dice que para el contenedor $c$ el elemento $i$ se encuentra o no dentro de él.

- $ y_c \in \{0,1\}, \forall c \in \{1, \dots, n\}$ : Indica si el conjunto C se está utilizando
## 3. Función Objetivo

Queremos minimizar la cantidad de contenedores posibles tal que todos los elementos esten guardados.

$$\min( \sum_{i=0}^{n} y_c )$$

## 4. Restricciones

Si un elemento se encuentra en un C entonces no puede estar en otro C

$$ \sum_{c \in n}^{} S_{c,i} = 1 \; \forall i:\{1,..,n\} $$

Por cada contenedor la suma de todos sus elementos no pasa de la capacidad máxima

$$\sum_{i=1}^{n} E_i \cdot S_{c,i} \le M \cdot y_c, \quad \forall c \in \{1, \dots, n\}$$

---
