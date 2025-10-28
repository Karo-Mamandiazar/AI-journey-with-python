# Multiplication Table – Python Mini Project

# Outer loop: iterates through numbers 1 to 10
for i in range(1, 11):
    # Inner loop: multiplies 'i' by numbers 1 to 10
    for j in range(1, 11):
        # Prints the multiplication result in the format "i * j = result"
        print(f"{i} * {j} = {i * j}")
    
    # Prints a separator line after each set of multiplications
    print("-" * 10)

