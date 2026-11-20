# https://github.com/GoldenSmasher87/lab10-LM-AC
# Partner 1: Lucas Mattos
# Partner 2: Abidul Chowdhury
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# sqrt(a)
# a cannot be negative
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

# hypotenuse with a and b
# can have negative numbers
def hypotenuse(a, b):
    return math.hypot(a, b)

# a plus b
def add(a, b):
    return a + b

# a - b
def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

# log(b) of base a
# a cannot be 1
# a and b cannot be <= 0
def logarithm(a, b):
    if (a <= 0) or (b <= 0) or (a == 1):
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

