from os import *
from sys import *
from collections import *
from math import *

def countBits(n):
    return bin(n).count('1')
        
n = int(input())
print(countBits(n))

