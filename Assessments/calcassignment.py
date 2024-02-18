# Write a python program to create a calculator class
# include methods for basic arithmetic operations (i.e)
# addition,subtraction,multiplication,division

class Calculator(object):
    def add (self, x, y):
        return x + y
    def subtract (self, x, y):
        return x - y
    def multiply (self, x, y):
        return x * y
    def divide (self, x, y):
        if y == 0:
            return "Division with 0 is not impossible"
        elif x == 0:
            return "Kindly enter a larger number"
        return x / y

calc = Calculator()
print("Addition =", calc.add(3, 4))
print("Subtraction =", calc.subtract(75.5, 65))
print("Multiplication =", calc.multiply(3, 7))
print("Division =", calc.divide(0, 9))
