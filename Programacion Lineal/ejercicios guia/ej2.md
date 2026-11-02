# Ejercicio 2

> Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).

> ejercicio 4 de PD: Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar. Indicar y justificar la complejidad del algoritmo implementado.

--- 

## 1. Parámetros de Entrada

- $ n $ = cantidad de dias disponibles
- $ V_i $ = valor del dia i

---

## 2. Variables de Decisión

$$
x_i = \begin{cases} 
1 & \text{si se trabajo el día } i \\
0 & \text{en caso contrario}
\end{cases}
\quad \forall i \in \{0, \dots, n\}
$$

---

## 3. Función Objetivo

$ max( \sum_{i=0}^{n} x_i * V_i )$

---

## 4. Restricciones

$ \forall i \in  \{0,..,n-1\} \quad x_i + x_{i+1} <= 1$

No podemos elegir más de un día seguido