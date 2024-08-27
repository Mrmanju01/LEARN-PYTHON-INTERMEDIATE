encapsulation is nothing a binding of modules,methods into one unit..
its containing getter and setter methods..
class Salary:
  def __init__(self,salary,name):
    self.salary=salary
    self.name=name
  def get_salary(self):
    return self.salary

  def set_salary(self):
    if salary > 0:
      self.salary = salary
    else:
      print("Invalid salary amount")

  def display_info(self):
    print(f"Employee: {self.name}, Salary: {self.salary}")

sal=Salary("Manju",2000)
print(sal.name)
sal.display_info()
print(sal.get_salary())
sal.set_salary(15000)
sal.display_info()
***************************************
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500

