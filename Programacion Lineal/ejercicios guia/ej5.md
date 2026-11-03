# Ejercicio 5: 

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

Queremos minimizar la cantidad de variables logica que satisfagan la restriccion

$ min (\sum_{i=1}^{n} X_i) $

---

## 4. Restricciones

Todas las Clausulas del 3-SAT deben ser verdaderas entonces, todas las variables logicas con valores 0,1 deben dar en conjunto al menos 1. 

$ \sum_{i \in Pos(C_j)}^{} (X_i)  + \sum_{i\in Neg(C_j)}^{} (1-X_i) >= 1 \quad \forall C_j \in C $
