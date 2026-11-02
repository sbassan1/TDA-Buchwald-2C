# Ejercicio 3: 

> Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

> Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo (es decir, que sea el conjunto de tamaño mínimo).

---

## 1. Parámetros de Entrada

- $V$ : Vertices del grafo
- $E$ : Aristas del grafo

---

## 2. Variables de Decisión

- $X_i \in \{0,1 \}$: Decide si el vertice i del grafo es elegido o no

---

## 3. Función Objetivo

$ min(\sum_{i\in V}^{} X_i)$

---

## 4. Restricciones

- $X_u + X_v >= 1 \quad \forall (u,v) \in E $