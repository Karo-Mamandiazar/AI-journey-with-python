# Python Data Types

"""
 Python Built-in Data Types:

 In programming, data type is an important concept.

 Variables can store data of different types, and different types can do different things.
"""

# Python has the following data types built-in by default, in these categories:
#  Text Type:  str
#  Numeric Types:  int, float, complex
#  Sequence Types:  list, tuple, range
#  Mapping Type:  dict
#  Set Types:  set, frozenset
#  Boolean Type:  bool
#  Binary Types:  bytes, bytearray, memoryview
#  None Type:  NoneType

print('___Checking Python Data Types___')

# Getting the Data Type
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

print('--------------------')

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

a = "Hello World"  #str
b = 20  #int
c  = 20.5  #float
d = 1j  #complex
e = ["apple", "banana", "cherry"]  #list
f = ("apple", "banana", "cherry")  #tuple
g = range(6)  #range
h = {"name" : "John", "age" : 36}  #dict
i = {"apple", "banana", "cherry"}  #set
j = frozenset({"apple", "banana", "cherry"})  #frozenset
k = True  #bool
l = b"Hello"  #bytes
m = bytearray(5)  #bytearray
n = memoryview(bytes(5))  #memoryview
x = None  #NoneType

print('--------------------')

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

A = str("Hello World")  #str
B = int(20)  #int
C = float(20.5)  #float
D = complex(1j)  #comple
E = list(("apple", "banana", "cherry"))  #list
F = tuple(("apple", "banana", "cherry"))  #tuple
G = range(6)  #range
H = dict(name="John", age=36)  #dict
I = set(("apple", "banana", "cherry"))  #set
J = frozenset(("apple", "banana", "cherry"))  #frozenset
K = bool(5)  #bool
L = bytes(5)  #bytes
M = bytearray(5)  #bytearray
N = memoryview(bytes(5))  #memoryview