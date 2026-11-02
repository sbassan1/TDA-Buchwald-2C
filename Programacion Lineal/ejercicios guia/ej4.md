# Ejercicio 4: 

> Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT).

> ejercicio 14 de BT: Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

---

## 1. Parámetros de Entrada
- $ n $ : Cantidad de Vertices en G
- $ V $ : Vertice de G
- $ E $ : Arista de G

---

## 2. Variables de Decisión

- $ X_i \in \{0,1\} $ : Variable que representa si el vertice $i$ fue elegido o no en el dominating set

---

## 3. Función Objetivo

$min( \sum_{i = 0}^{n} X_i ) $

---

## 4. Restricciones

$ X_v + \sum_{j\in adj(v)}^{} => 1  \quad  \forall v \in V$