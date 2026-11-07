# Ejercicio n: 

> Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de estas predicciones en el arreglo pp, para todo día i=1,2,...,ni=1,2,...,n. Osvaldo quiere determinar un día jj en el cuál comprar la casa, y un día kk en el cual venderla (k>jk>j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto, es el de maximizar la ganancia dada por p[k]−p[j]p[k]−p[j].

> Implementar un modelo de programación lineal que determine el día de compra y el día de venta del inmueble. Indicar la cantidad de restricciones implementadas para esto.

---

## 1. Parámetros de Entrada

- $n$ : Cantidad de dias
- $P$ : Arreglo de predicciones
---

## 2. Variables de Decisión

- $ C_i \in \{0,1\}$: Variable binaria que nos dice si se compro el inmueble en el día i
- $ V_i \in \{0,1\}$: Variable binaria que nos dice si se vendio el inmueble en el día i

---

## 3. Función Objetivo

Queremos maximizar la ganancia resultante (lo que ganamos - lo que gastamos) de comprar el inmueble y venderlo despues

$\max( \sum_{i=0}^{n} (V_i - C_i)* P_i )$

---

## 4. Restricciones

Solo podemos hacer una compra y una venta, el dia de la compra debe ser menor o igual al dia de la venta. 

- $ \sum_{i=0}^{n} C_i = 1 $
- $ \sum_{i=0}^{n} V_i = 1 $
- $ \sum_{i=0}^{n} C_i * i  \leq \sum_{i=0}^{n} V_i * i $

- $C_i \in \{0,1\}$ y $V_i \in \{0,1\} \quad \forall i \in {1,..,n} $