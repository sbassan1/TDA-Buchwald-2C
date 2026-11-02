# Ejercicio n: 

> Implementar un modelo de programación lineal que resuelva el problema de 3-SAT mínimo: que encuentre una solución que satisfaga, utlizando la menor cantidad de variables en true posible.

---

## 1. Parámetros de Entrada

- $n$ : Cantidad de variables booleanas
- $X$ : Conjunto de variables logicas
- $C_j \in C $ : Clausula j con tres variables logicas $ X_i \in X$  

---

## 2. Variables de Decisión

- $X_i \in \{0,1\}, \; i \in \{1,.n\}$ : Nos dice si la variable logica i es verdadera o falsa.  

---

## 3. Función Objetivo

$\sum_{i=1}^{n} X_i $

---

## 4. Restricciones

#TODO 