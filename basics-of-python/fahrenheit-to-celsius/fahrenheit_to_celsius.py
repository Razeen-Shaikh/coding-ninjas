from os import *
from sys import *
from collections import *
from math import *

S = int(input())
E = int(input())
W = int(input())

for f in range(S, E+1, W):
    celcius = (f - 32) * 5 / 9
    celcius = ceil(celcius) if celcius < 0 else floor(celcius)
    print(f, celcius)
