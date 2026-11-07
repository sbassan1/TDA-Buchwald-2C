# Ejercicio 7: 

> Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un grafo. Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas (podés usar notación O para esto, no es importante el número exacto).

---

## 1. Parámetros de Entrada

- $ V \in G$ : Vertices del grafo
---

## 2. Variables de Decisión

- $ Y_i \in \{0,1\} $ : Variable binaria que representará si el vertice i está dentro del clique.

---

## 3. Función Objetivo

Queremos encontrar la maxima cantidad de vertices que cumplan con la condicion de clique en el grafo.

$\max(\sum_{i=0}^{n} Y_i)$

---

## 4. Restricciones

$ Y_i + \sum_{j \in adj(V_i)}^{} Y_j \leq $