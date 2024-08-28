try.
except..
finally...
else....
def add(a,b):
  try:
    k=a%b
    print(k)
  except Exception as e:
    print("zero by divison error is not possible",e)
  else:
    print("i dont the output")
  finally:
    print("finally the calculation is done")
    
 add(5,0)
*******************************************************************✅
try:
    x = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
*******************************************************************✅
class MyClass:
    pass

obj = MyClass()
try:
    obj.my_attr  # Raises AttributeError
except AttributeError:
    print("Attribute not found!")
*******************************************************************✅
try:
    '5' + 5  # Raises TypeError
except TypeError:
    print("Cannot add string and integer!")
*******************************************************************✅
try:
    int("abc")  # Raises ValueError
except ValueError:
    print("Invalid literal for integer conversion!")
*******************************************************************✅
try:
    lst = [1, 2, 3]
    print(lst[5])  # Raises IndexError
except IndexError:
    print("List index out of range!")
*******************************************************************✅
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])  # Raises KeyError
except KeyError:
    print("Key not found in dictionary!")
***************************************************************✅
try:
    open("nonexistent_file.txt")  # Raises FileNotFoundError
except FileNotFoundError:
    print("File not found!")
***************************************************************✅
try:
    import nonexistent_module  # Raises ModuleNotFoundError
except ModuleNotFoundError:
    print("Module not found!")
***************************************************************✅
try:
    print(x)  # Raises NameError if x is not defined
except NameError:
    print("Name not defined!")
***************************************************************✅
def recurse():
    recurse()

try:
    recurse()  # Raises RecursionError
except RecursionError:
    print("Maximum recursion depth exceeded!")
***************************************************************✅
try:
    assert 2 + 2 == 5  # Raises AssertionError
except AssertionError:
    print("Assertion failed!")
***************************************************************✅
