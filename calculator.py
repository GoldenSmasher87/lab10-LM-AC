"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/GoldenSmasher87/lab10-LM-AC
# Partner 1: Lucas Mattos
# Partner 2: Abidul Chowdhury

import math

# a plus b
def add(a, b): 
    return a + b

# a - b
def subtract(a, b):
    return a - b

# a times b
def multiply(a, b):
    return a * b

# b divided by a 
# a cannot be 0
def divide(a, b):
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

# a to the power of b
def exponent(a, b):
    return a ** b