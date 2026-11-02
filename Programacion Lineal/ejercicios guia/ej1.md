# Ejercicio 1: 

> Tenemos una mochila con una capacidad $W$. Hay elementos a guardar, cada uno tiene un valor y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 

> Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo.

---

## 1. Parámetros de Entrada

* $n$: Cantidad total de elementos disponibles ($n \in \mathbb{N}$).
* $W$: Capacidad máxima de la mochila ($W \in \mathbb{R}_{\ge 0}$).
* $w_i$: Peso del elemento $i$, para todo $i \in \{1, \dots, n\}$.
* $v_i$: Valor o ganancia del elemento $i$, para todo $i \in \{1, \dots, n\}$.

---

## 2. Variables de Decisión

$$
x_i = \begin{cases} 
1 & \text{si el elemento } i \text{ se incluye en la mochila} \\
0 & \text{en caso contrario}
\end{cases}
\quad \forall i \in \{1, \dots, n\}
$$

---

## 3. Función Objetivo

Maximizar la ganancia total acumulada por los elementos seleccionados:

$$
\max z = \sum_{i = 1}^{n} v_i \cdot x_i
$$

---

## 4. Restricciones

1. **Restricción de Capacidad:** El peso total de los elementos elegidos no debe superar la capacidad de la mochila $W$:

   $$
   \sum_{i = 1}^{n} w_i \cdot x_i \le W
   $$

2. **Dominio de las Variables (Naturaleza Binaria):**

   $$
   x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, n\}
   $$

