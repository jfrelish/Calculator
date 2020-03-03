import math


def addition(a, b):
    return float(a) + float(b)

def subtraction(a, b):
    return float(a) - float(b)


class Calculator:
    result = 0

    def __init__(self):
        x = 4 + 4
        self.result = x;
        pass

    def addition(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = subtraction(a, b)
        return self.result

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
