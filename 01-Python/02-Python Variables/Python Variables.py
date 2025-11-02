# Python Variables Tutorial
"""
This script demonstrates how to work with variables in Python.
Topics covered:
- Creating variables
- Variable naming rules
- Checking variable types
- Assigning multiple values
- Unpacking collections
- Output formatting
- Global vs local variables
"""
"""
Variables:
Variables are containers for storing data values.
"""

print('--- Creating Variables ---')

x = "karo"
y = 18
print(x)
print(y)

print('--- Variable Naming Rules ---')
"""
A variable can have a short name (like x and y) or
 a more descriptive name (age, carname, total_volume).

Rules for Python variables:

   A variable name must start with a letter or the underscore character
   A variable name cannot start with a number
   A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
   Variable names are case-sensitive (age, Age and AGE are three different variables)
   A variable name cannot be any of the Python keywords.

Valid variable names:
myvar = "Karo"
my_var = "Karo"
_my_var = "Karo"
myVar = "Karo"
MYVAR = "Karo"
myvar2 = "Karo"

Invalid variable names:
# 2myvar = "Karo"     # Starts with number
# my var = "Karo"     # Contains space
# my-var = "Karo"     # Contains hyphen
"""

print('--- Checking Variable Types ---')

x = "karo"
y = 18
print(type(x))  # str
print(type(y))  # int

print('--- Assigning Multiple Values ---')
# Many Value to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x , y , z = "Karo" , "Mamandi" , 18
print(x)
print(y)
print(z)

print('--- Assigning One Value to Multiple Variables ---')
x = y = z = "Karo"
print(x)
print(y)
print(z)

print('--- Unpacking a Collection ---')
"""
If you have a collection of values in a list, tuple etc.
 Python allows you to extract the values into variables. This is called unpacking.
"""
# Unpack a list:
fruits = ["apple", "banana", "cherry"]
X , Y , Z = fruits
print(X)
print(Y)
print(Z)

print('--- Output Variables ---')
x = "python is awesome"
print(x)

x = "python"
y = "is"
z = "awesome"
print(x , y , z)

x = "python "
y = "is "
z = "awesome"
print(x + y + z)

x = 10
y = 20
print(x)
print(y)
print(x + y)

x = "karo"
y = 18
print(x , y)

print('--- Global vs Local Variables ---')
# Global Variables:
"""
 Variables that are created outside of
  a function (as in all of the examples in the previous pages) are known as global variables.

 Global variables can be used by everyone, both
  inside of functions and outside.
"""

# Create a variable outside of a function, and use it inside the function:
x = "awesome"

def myfunc():
    print("Python is awesome")

myfunc()

"""
 If you create a variable with the same name inside a function,
  this variable will be local, and can only be used inside the function.
 The global variable with the same name will remain as it was,
  global and with the original value.
"""

print('--------------------')

# Example:
# Create a variable inside a function, with the same name as the global variable:
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

print('--------------------')

# The global Keyword
"""
Normally, when you create a variable inside a function, that
 variable is local, and can only be used inside that function.

To create a global variable inside a function, you
 can use the global keyword.
"""

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

print('--------------------')

# Also, use the global keyword if you want to change a global variable inside a function.

# Example:
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
