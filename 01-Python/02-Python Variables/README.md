# 🐍 Python Variables Tutorial

This repository contains a beginner-friendly Python script that demonstrates how variables work in Python.

## 📚 Topics Covered

- Creating variables
- Variable naming rules
- Checking variable types
- Assigning multiple values
- Unpacking collections
- Output formatting
- Global vs local variables

## 🧠 Key Concepts

### ✅ Creating Variables
```python
x = "Karo"
y = 18


✅ Variable Naming Rules

Valid:

• myvar, my_var, _my_var, myVar, MYVAR, myvar2


Invalid:

• 2myvar (starts with number)
• my var (contains space)
• my-var (contains hyphen)


✅ Checking Types

print(type(x))  # str
print(type(y))  # int


✅ Assigning Multiple Values

x, y, z = "Karo", "Mamandi", 18


✅ Unpacking Collections

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits


✅ Output Formatting

print(x, y, z)
print(x + " " + y + " " + z)


✅ Global vs Local Variables

x = "awesome"

def show_local():
    x = "fantastic"
    print("Python is " + x)

show_local()
print("Python is " + x)  # Still prints global value


✅ Using global Keyword

def make_global():
    global x
    x = "fantastic"


🚀 How to Run

Just clone the repo and run the script:

python variables_tutorial.py
