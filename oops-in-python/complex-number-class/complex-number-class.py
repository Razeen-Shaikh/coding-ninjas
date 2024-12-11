from os import *
from sys import *
from collections import *
from math import *



class ComplexNumbers:
    
    #create your class here.
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary


    def plus(self, other):
        self.real += other.real
        self.imaginary += other.imaginary

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        self.real = real_part
        self.imaginary = imaginary_part

    def print(self):
        print(f"{self.real} + i{self.imaginary}")

    
    
    
    
    
    
#Driver's code goes here.
[a, b] = map(int, input().split())
[c, d] = map(int, input().split())
n = int(input())

C1 = ComplexNumbers(a, b)
C2 = ComplexNumbers(c, d)

if n == 1:
    C1.plus(C2)
    C1.print()

if n == 2:
    C1.multiply(C2)
    C1.print()



    
    
    
    
    
    
    
    
    
    
