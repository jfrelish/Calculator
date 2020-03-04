import math
from math import pow


def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def divide(a, b):
    return float(a) / float(b)


def sqrt(a):
    return math.sqrt(float(a))


def square(a):
    return  pow(float(a), 2)


class Calculator:
    result = 0

    def __init__(self):
        self.result = 8
        pass

    def addition(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtraction(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b,):
        self.result = divide(a, b)
        return self.result

    def sqrt(self,  a):
        self.result = sqrt(a)
        return self.result

    def square(self, a):
         self.result = square(a)
         return self.result
