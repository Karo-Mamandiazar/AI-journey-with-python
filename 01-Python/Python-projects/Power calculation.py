# Power calculation

# Ask the user to input the base number
base = int(input("Enter the base: "))

# Ask the user to input the exponent (power)
power = int(input("Enter the power: "))

# Define a function to compute the power manually
def compute_power(base, power):
    result = 1
    # Multiply the base 'power' times using a for loop
    for x in range(power):
        result = result * base
    return result

# Call the function and print the result
print(compute_power(base, power))


