"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/GoldenSmasher87/lab10-LM-AC
# Partner 1: Lucas Mattos
# Partner 2: Abidul Chowdhury

import math

# sqrt(a)
# a cannot be negative
def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        print("Cannot take square root of a negative number.")

# hypontenuse with a and b
# can have negative numbers
def hypotenuse(a, b):
    return math.hypot(a, b)

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
    try:
        if a == 0:
            raise ZeroDivisionError
        return b / a
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# log(b) of base a
# a cannot be 1
# a and b cannot be <= 0
def logarithm(a, b):
    try:
        if (a <= 0):
            raise ValueError("a cannot be less than or equal to 0.")
        elif (b <= 0):
            raise ValueError("b cannot be less than or equal to 0.")
        elif (a == 1):
            raise ValueError("a cannot be 1.")
        return math.log(b, a)
    except ValueError as e:
        print(f"Cannot take logarithm: {e}")

# a to the power of b
def exponent(a, b):
    return a ** b