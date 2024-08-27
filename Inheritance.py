types
1.Single Inheritance

class Parent:
    def display(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        print("This is the child class.")

c = Child()
c.display()  # Output: This is the parent class.
c.show()     # Output: This is the child class.
------------------------
class hero:
  def movie(self):
    print("hey hero")

class heroine(hero):
  def cinemas(self):
    print("hey heroine")
z=heroine()
z.movie()
z.cinemas()
*************************************************************
2.Multiple Inheritance
class vehicle:
  def car(self):
    print("car")

class toy:
  def toy_car(self):
    print("Toy car")

class bomma(toy,vehicle):
  def bomma_car(self):
    print("bomma car")

cc=bomma()
cc.car()
cc.toy_car()
cc.bomma_car()

----------------
class Parent1:
    def show(self):
        print("This is Parent1.")

class Parent2:
    def display(self):
        print("This is Parent2.")

class Child(Parent1, Parent2):
    pass

c = Child()
c.show()     # Output: This is Parent1.
c.display()  # Output: This is Parent2.

*******************************************************************


3.Multilevel Inheritance
class vehicle:
  def car(self):
    print("car")

class toy(vehicle):
  def toy_car(self):
    print("Toy car")

class bomma(toy):
  def bomma_car(self):
    print("bomma car")

cc=bomma()
cc.car()
cc.toy_car()
cc.bomma_car()
*****************************************
4.Hierarchical Inheritance
class parent:
  def parent1(self):
    print("this is parent1")

class mother(parent):
  def mother1(self):
    print("this is mother")

class son(parent):
  def son1(self):
    print("this is son1")

kk=mother()
kk.parent1()
kk.mother1()
ll=son()
ll.son1()
***********************************************
5.Hybrid Inheritance
class Grandparent:
    def greet(self):
        print("This is the grandparent class.")

class Parent1(Grandparent):
    pass

class Parent2(Grandparent):
    pass

class Child(Parent1, Parent2):
    pass

c = Child()
c.greet()  # Output: This is the grandparent class.

--------------
class gold:
  def high(self):
    print("gold is high")

class platinum(gold):
  def very(self):
    print("platinum is very high")
class diamond()

class silver(platinum):
  def cheap(self):
    print("silver is very cheap")

ch=silver()
ch.high()
ch.very()
ch.cheap()
