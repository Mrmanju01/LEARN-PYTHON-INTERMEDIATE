types:
1 method overloading

Compile-Time Polymorphism (Method Overloading):

Python does not support method overloading by default like languages such as Java. However, you can achieve a similar effect using default parameters or handling arguments inside a method.

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # Output: 5
print(calc.add(1, 2, 3))    # Output: 6
print(calc.add())           # Output: 0

2.method override
class Actor:
    def expressions(self):
        print("Generic expressions")

class Hero(Actor):
    def expressions(self):
        print("He has good expressions")

class Heroine(Actor):
    def expressions(self):
        print("She has worst expressions")

# Using method overriding
def expressions(actor):
    actor.expressions()

hero = Hero()
heroine = Heroine()

expressions(hero)      # Output: He has good expressions
expressions(heroine)   # Output: She has worst expressions
