print("...---=== Part one ===---...")

print("=== Python Functions ===")

# Python Function
"""
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.
"""

# --- Creating a Function ---

# In Python, a function is defined using the def keyword, followed by
#  a function name and parentheses:

def greet():
    print("Hello from a function")

greet()

print("-----------------------------")

print("--- Calling a Function ---")

# To call a function, write its name followed by parentheses:

def my_function():
    print("Hello from a function")

my_function()

print("- You can call the same function multiple times:")

def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()

# -----------------------------

# --- Function Names ---
"""
 Function names follow the same rules as variable names in Python:

 - A function name must start with a letter or underscore
 - A function name can only contain letters, numbers, and underscores
 - Function names are case-sensitive (myFunction and myfunction are different)
"""

# -----------------------------

# --- Why Use Functions? ---

# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program.
# Without functions, you would have to write the same calculation code repeatedly:

# - Without functions - repetitive code:

# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

# - With functions, you write the code once and reuse it:

# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))

print("-----------------------------")

print("--- Return Values ---")
"""
Functions can send data back to the code that called them using the return statement.
"""

# When a function reaches a return statement, it stops executing and sends the result back:

# A function that returns a value:

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

print("- You can use the returned value directly:")

# Using the return value directly:

def get_greeting():
  return "Hello from a function"

print(get_greeting())

# -----------------------------

# --- The pass Statement ---

# Function definitions cannot be empty.
# If you need to create a function placeholder without any code, use the pass statement:

def my_function():
  pass


# The pass statement is often used when developing, allowing you to define the structure first
# and implement details later.

print("-----------------------------")

print("...---=== Part two ===---...")
print("=== Python Function Arguments ===")

print("--- Arguments ---")
"""
 Information can be passed into functions as arguments.

 Arguments are specified after the function name, inside the parentheses.
  You can add as many arguments as you want, just separate them with a comma.
"""

# The following example has a function with one argument (fname).
# When the function is called, we pass along a first name, which is used inside the function to print the full name:

# A function with one argument:

def my_function(fname):
    print(fname + " Engineer")

my_function("AI")
my_function("Data")
my_function("Machine Learning")

print("-----------------------------")

print("--- Parameters vs Arguments ---")
"""
The terms parameter and argument can be used for the same thing: information that are passed into a function.
"""

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("World!") # "World!" is an argument

print("----------------------------")

print("--- Number of Arguments ---")
"""
By default, a function must be called with the correct number of arguments.

If your function expects 2 arguments, you must call it with exactly 2 arguments.
"""

# This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("NumPy", "Pandas")

# If you try to call the function with the wrong number of arguments, you will get an error:

"""This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

 my_function("NumPy")"""

print("----------------------------")

print("--- Default Parameter Values ---")

# You can assign default values to parameters.
# If the function is called without an argument, it uses the default value:

def my_function(name = "Python"):
  print("Hello", name)

my_function("NumPy")
my_function("Pandas")
my_function()
my_function("Seaborn")

print(15 * '-')
# Default value for country parameter:

def my_function(country = "Australia"):
  print("I am from", country)

my_function("Germany")
my_function("England")
my_function()
my_function("America")

print("----------------------------")

print("--- Keyword Arguments ---")

# You can send arguments with the key = value syntax.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Rex")

print(15 * '-')
# This way, with keyword arguments, the order of the arguments does not matter.

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Rex", animal = "dog")

print("----------------------------")

print("--- Positional Arguments ---")
"""
When you call a function with arguments without using keywords, they are called positional arguments.
"""

# Positional arguments must be in the correct order:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Rex")

print(15 * '-')
# The order matters with positional arguments:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Rex", "dog")

print("----------------------------")

print("--- Mixing Positional and Keyword Arguments ---")
"""
You can mix positional and keyword arguments in a function call.
"""

# However, positional arguments must come before keyword arguments:
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Rex", age = 5)

print("----------------------------")

print("--- Passing Different Data Types ---")
"""
You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
"""

# The data type will be preserved inside the function:

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Sending a dictionary as an argument:

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

The_person = {"name": "Karo", "age": 18}
my_function(The_person)

print("----------------------------")

print("--- Return Values ---")

# Functions can return values using the return statement:

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

print("----------------------------")

print("--- Returning Different Data Types ---")
"""
Functions can return any data type, including lists, tuples, dictionaries, and more.
"""

# A function that returns a list:

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# A function that returns a tuple:

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

print("----------------------------")

print("--- Positional-Only Arguments ---")
"""
You can specify that a function can have ONLY positional arguments.
"""

# To specify positional-only arguments, add , / after the arguments:

def my_function(name, /):
  print("Hello", name)

my_function("World!")

# Without the ( , / ) you are actually allowed to use keyword arguments even if the function expects positional arguments:

def my_function(name):
  print("Hello", name)

my_function(name = "World!")

print("----------------------------")

print("-- Keyword-Only Arguments ---")

# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("Hello", name)

my_function(name = "World!")

# Without ( *, ), you are allowed to use positional arguments even if the function expects keyword arguments:

def my_function(name):
  print("Hello", name)

my_function("World!")

print("----------------------------")

print("--- Combining Positional-Only and Keyword-Only ---")
"""
You can combine both argument types in the same function.
"""

# Arguments before / are positional-only, and arguments after * are keyword-only:

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

print("----------------------------")

print("...---=== Part three ===---...")

print("=== Python Advanced Functions ===")


# --- *args and **kwargs ---
def demo_args(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo_args(1, 2, 3, name="Karo", age=18)

# --- Lambda Functions ---
square = lambda x: x ** 2
print("Square of 5:", square(5))

# --- Recursive Functions ---
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))