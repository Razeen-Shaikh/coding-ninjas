from os import *
from sys import *
from collections import *
from math import *

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def totalPrime(S, E):
    prime_count = 0
    for num in range(S, E + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count

S,E = map(int,input().split(' '))
print(totalPrime(S,E))


