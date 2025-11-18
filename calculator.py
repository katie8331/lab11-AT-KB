"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# GitHub: https://github.com/katie8331/lab11-AT-KB
# Partner 1: Isabel Tejeda
# Partner 2: Katie Brisson

import math
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("invalid logarithm base")
    if b <= 0:
        raise ValueError("invalid logarithm argument")
    return math.log(b, a)


def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("square root undefined for negative numbers")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


