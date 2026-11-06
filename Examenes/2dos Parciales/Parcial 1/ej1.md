# Ejercicio n: 

> Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar la máxima cantidad de charlas a dar de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas. Implementar un modelo de programación lineal que resuelva el problema de Interval Scheduling. Indicar la cantidad de inecuaciones definidas en el modelo. Pueden asumir que hay una función solapamientos(intervalo), que da todos los intervalos que se solapan con el intervalo, y la pueden usar en el modelo.

---

## 1. Parámetros de Entrada

- $n$ : Cantidad de intervalos
- $Y$ : Intervalos de charlas, donde cada charla Y_i es un intervalo de tiempo (inicio,fin)

---

## 2. Variables de Decisión

$ X_i \in \{0,1\}, \forall i \in \{1,..,n\}$ : Nos dice si la charla i esta en el scheduling

---

## 3. Función Objetivo

Queremos maximizar la cantidad de charlas elegidos que no se solapen.

$ \max(\sum_{i=0}^{n} X_i )$

--- 

## 4. Restricciones

Queremos que para cada charla 'i' elegida no tenga solapamientos con las charlas dentro de ellas

$ \forall i : \quad X_i + (\sum_{j \in solapa(Y_i)}^{} X_j) <= 1 + M(1-X_i) $


---
Tenemos $n^2$ restricciones, ya que por cada charla verificamos que haya ninguna otra que se solape, y en el peor caso todas las charlas se solapan entre si y verifican con tamaño 'n' en cada i.