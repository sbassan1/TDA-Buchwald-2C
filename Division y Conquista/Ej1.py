"""
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo
de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo.
Ejemplos:
    [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
    [5, 3, -5, 4, -1] ->  [5, 3]
    [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
    [5, -4, 2, 4] -> [5, -4, 2, 4]
    [-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
"""

"""
[5, -4, 2, 4]

SUM [5, -4] == [1]
SUM [2,  4] == [6]

[7]

"""

def maxCrossingSum(arr1, arr2):

    # Include elements on the left of mid
    leftSum = float('-inf')
    sum = 0
    for i in range(m, l - 1, -1):
        sum += arr[i]
        leftSum = max(leftSum, sum)

    # Include elements on the right of mid
    rightSum = float('-inf')
    sum = 0
    for i in range(m, h + 1):
        sum += arr[i]
        rightSum = max(rightSum, sum)

    # Return the maximum of left sum, right sum, and their combination
    return max(leftSum + rightSum - arr[m], leftSum, rightSum)

def max_subarray(arr):

    if arr == []:
        return 0
    if len(arr) <= 1:
        return arr[0]


    mid = len(arr) // 2

    left = max_subarray(arr[:mid])
    right = max_subarray(arr[mid:])

    return arr[:]
