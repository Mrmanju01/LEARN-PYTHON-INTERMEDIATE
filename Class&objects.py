1. Classes
A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. Think of a class as a template or a prototype.

Here's a simple example of a class definition in Python:
class Car:
    # Class attribute
    wheels = 4

    # Initializer method (constructor)
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year

    # Method
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Access instance attributes
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)   # Output: 2020

# Call a method on the object
print(my_car.display_info())  # Output: 2020 Toyota Corolla

# Access class attribute
print(Car.wheels)  # Output: 4



class hero:
  heroine=False
  def __init__(self,comedy,thriller,action):
    self.comedy=comedy
    self.thriller=thriller
    self.action=action

  def  manju(self):
    print(f"hey all this is yours {self.action} star mr Mnajunathareddy. sometimes i was {self.comedy} and {self.thriller}")


me=hero("Action","Comic","Thriller")
print(me.comedy)
print(me.thriller)
print(me.action)
print(me.manju())



