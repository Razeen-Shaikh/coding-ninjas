from os import *
from sys import *
from collections import *
from math import *

MOD = 10**9 + 7

def matrix_multiply(A, B):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
        ]
    ]

def matrix_exponentiation(matrix, power):
    result = [[1, 0], [0, 1]]
    base = matrix
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    
    return result

def fibonacciNumber(n):
    if n == 1 or n == 2:
        return 1
    
    transformation_matrix = [[1, 1], [1, 0]]
    
    result_matrix = matrix_exponentiation(transformation_matrix, n - 1)
    
    return result_matrix[0][0]
    
