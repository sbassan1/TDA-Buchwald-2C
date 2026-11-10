# Ejercicio 1: 

> El 2-Partition Problem como problema de optimización se describe tal que: Dado un conjunto de n números positivos T = {T1,T2,...,Tn}, se particionan los números en dos subconjuntos S1 y S2 (con intersección vacía y unión = T) de forma de minimizar la sumatoria de cualquiera de los subconjuntos (mínmáx(S1,S2)).

> Implementar un modelo de programación lineal que dados los valores de los Ti nos permita obtener la asignación óptima para S1 y S2. Indicar la cantidad de inecuaciones definidas en el modelo.

---

## 1. Parámetros de Entrada

- $T$ : Conjunto de numeros positivos
- $n$ : Cantidad de elementos en T 

## 2. Variables de Decisión

- $S_{1,i} \in \{0,1\}, \forall i \in \{1,..,n\}$ : Nos dice si el numero i esta en el conjunto de S1
- $S_{2,i} \in \{0,1\}, \forall i \in \{1,..,n\}$ : Nos dice si el numero i esta en el conjunto de S1
- $z \geq 0$ : Cota superior del maximo de S1 y S2


## 3. Función Objetivo

Queremos minimizar el valor maximo entre S1 y S2, para lograr esto debemos definir el maximo entre S1 y S2 en las restricciones.

$$\min(z)$$

## 4. Restricciones

Queremos que todos los i del T esten usados en S1 y S2 al menos una vez 

$$ \forall i : \{1,..,n\} : S_{1,i} + S_{2,i} = 1  $$

Cotas de Z para $S_1$ y $S_2$

$$ z \ge \sum_{i=1}^{n} T_i \cdot S_{1,i} $$
$$ z \ge \sum_{i=1}^{n} T_i \cdot S_{2,i} $$


Esto es equivalente a $ z = \max(\sum_{i=1}^{n} T_i \cdot S_{1,i},\sum_{i=1}^{n} T_i \cdot S_{1,i})$, el Z es el maximo entre $S_1$ y $S_2$ ya que como ambas estan compitiendo para ser las mas grandes.

Al tener todos los T usados al menos una vez, y que S1 y S2 no tomen el mismo i, entonces tenemos cubierto los casos donde la interseccion es vacia y la union es T

---
