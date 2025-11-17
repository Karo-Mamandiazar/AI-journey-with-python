print('---=== Python While Loops ===---')

# --- Python Loops ---
"""
Python has two primitive loop commands:
 
 - while loops
 - for loops
  
"""

print("--- The while Loop ---")
"""
With the (while) loop we can execute a set of statements as long as a condition it true.
"""

# print (i) as long as (i) is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

print(i)

print('--------------------')

print("--- The break Statement ---")

# With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print(i)

print('--------------------')

print("--- The continue Statement ---")

# With the (continue) statement we can stop the current iteration, and continue with the next:

# Continue to the next interation if (i) is 3:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print("i is no longer less than 6")
# Note that number 3 is missing in the result.

print('--------------------')

print("--- The else Statement ---")

# With the (else) statement we can run a block of code once when the condition no longer is true:

# print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
