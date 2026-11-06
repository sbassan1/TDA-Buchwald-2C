# Ejercicio 6: 

> Implementar un modelo de programación lineal que resuelva el problema de Independent Set Máximo.

> A maximum independent set (MIS) is the largest possible subset of vertices in an undirected graph such that no two vertices in the subset are connected by an edge

---

## 1. Parámetros de Entrada

- $n$ : Cantidad de vertices en el grafo
- $X$ : Vertices en el grafo
- $(u,v) \in E , \forall u,v \in X $ : Aristas del grafo 

---

## 2. Variables de Decisión

$ X_i \in \{0,1\}, \forall i \in \{1,..,n\}$ : Nos dice si el vertice i del grafo esta dentro de la solucion o no.

---

## 3. Función Objetivo

Queremos maximizar la cantidad de vertices elegidos que cumplan con las restricciones de independent set.

$ \max(\sum_{i=0}^{n} X_i )$

--- 

## 4. Restricciones

$ X_u + X_v \leq 1 \quad \forall (u,v) \in E $