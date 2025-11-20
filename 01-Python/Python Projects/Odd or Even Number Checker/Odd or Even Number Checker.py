"""
Odd or Even Number Checker
"""

# Prompt the user to enter a number and convert the input to an integer
num = int(input("Please insert the number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
    # If the remainder is 0, the number is even
    print("The number is an even number.")
else:
    # Otherwise, the number is odd
    print("The number is an odd number.")