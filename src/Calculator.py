
def fn_addition(a, b):
    return float(a) + float(b)

import math


class Calculator:
    result = 0

    def __init__(self):
        x = 4 + 4
        self.result = x;
        pass

    def add(self, a, b):
        self.result = fn_addition(a, b)
        return self.result

    def subtraction(self, a, b):
        c = a - b
        return c

    def multiply(self, a, b):
        c = a * b
        return c

    def divide(self, a, b,):
        c = a / b
        return c

    def sqrt(self,  a):
        c = math.sqrt(a)
        return c

    def square(self, a):
         c = a**2
         return c
