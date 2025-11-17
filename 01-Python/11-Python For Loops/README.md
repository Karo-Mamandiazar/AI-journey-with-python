🔹 README.md

# Python For Loops 🚀

This repository contains beginner-friendly examples of Python for loops.  
It demonstrates how to use loops with lists, strings, ranges, and also covers important concepts like break, continue, else, nested loops, and pass.

---

## 📚 What You Will Learn
- Iterating through lists and strings
- Using break to exit a loop early
- Using continue to skip an iteration
- Generating sequences with range()
- Adding an else block to a loop
- Creating nested loops
- Using pass as a placeholder

---

## 📝 Code Examples

### Looping through a list
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


Looping through a string

for x in "banana":
    print(x)


Using break

for x in fruits:
    if x == "banana":
        break
    print(x)


Using continue

for x in fruits:
    if x == "banana":
        continue
    print(x)


Using range

for x in range(2, 30, 3):
    print(x)


Nested loops

adj = ["red", "yellow", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


---

🎯 Purpose

This project is designed for beginners in Python who want to understand how loops work in practice.
It can also be used as a reference or teaching material for programming basics.

---

📌 Author

Created by Karo Mamandiazar

---