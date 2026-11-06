# Ejercicio 7: 

> Implementar un modelo de programación lineal que determine la cantidad mínima de colores a utilizar para poder pintar a un grafo de colores, de tal forma que ningún adyacente comparta color entre sí.

---

## 1. Parámetros de Entrada

- $ P $ : Paises en el grafo
- $ C $ : Colores

---

## 2. Variables de Decisión

- $ X_{p_i,c} \in \{0,1\} $: Coloreo el grafo i con color c 

- $ Y_c \in \{0,1\} $ : Vale 1 si el color c se ha utilizado en almenos 1 pais del grafo

---

## 3. Función Objetivo

Queremos encontrar la menor cantidad de colores para cada pais

$\min (\sum_{c}^{C} Y_C)$

---

## 4. Restricciones

Por cada pais, su pais adjacente no contenga el mismo color.

$ X_{p_i,c} + \sum_{p_j \in adj(p_i)}^{} X_{p_j,c} \leq 1 + M(1-X_{p_i,c})$

Cada pais solo tiene un color

$\forall pais \in V : \sum_{c}^{} X_{pais,c} = 1$
