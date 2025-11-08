---


📘 README.md

# Python While Loops Tutorial

This project contains educational examples for learning while loops in Python.  
It demonstrates different ways to control loop execution using break, continue, and else.


---


## 📂 Contents

1. While Loop  
   Execute a loop while a condition is true.
   ```python
   i = 1
   while i < 6:
       print(i)
       i += 1


1. Break Statement
Stop the loop even if the condition is still true.i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

2. Continue Statement
Skip the current iteration and continue with the next.i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

3. Else Statement
Run a block of code once the loop condition is no longer true.i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


---


🚀 How to Run

Run the script in your terminal:

python while_loops.py


---


🎯 Purpose

This project is intended for beginners who want to learn the basics of Python loops.
It provides clear examples of how while, break, continue, and else work together.


---