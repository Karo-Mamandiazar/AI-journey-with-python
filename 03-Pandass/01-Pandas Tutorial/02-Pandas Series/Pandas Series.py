print('---=== Pandas Series ===---')

print('--- What is a Series ---')
"""
 - A Pandas Series is like a column in a table.
 
 - It is a one-dimensional array holing data of any type.
"""

# Create a simple Pandas Series from a list:
import pandas as pd

a = [1, 7, 2]

my_var = pd.Series(a)

print(my_var)

print('-------------------------')

print('--- Labels ---')
"""
 - If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

 - This label can be used to access a specified value.
"""

# Return the first value of the Series:
import pandas as pd

a = [1, 7, 2]

my_var = pd.Series(a)

print(my_var[0])

print('-------------------------')

print('--- Create Labels ---')
"""
 - With the index argument, you can name your own labels.
"""

# Create your own labels:
import pandas as pd

a = [1, 7, 2]

my_var = pd.Series(a, index = ["x", "y", "z"])

print(my_var)

# - When you have created labels, you can access an item by referring to the label.

# Return the value of "y":
import pandas as pd

a = [1, 7, 2]

my_var = pd.Series(a, index = ["x", "y", "z"])

print(my_var["y"])

print('-------------------------')

print('--- Key/Value Objects as Series ---')
"""
 - You can also use a key/value object, like a dictionary, when creating a Series.
"""

# Create a simple Pandas Series from a dictionary:
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

my_var = pd.Series(calories)

print(my_var)

# Note: The keys of the dictionary become the labels.

"""
 - To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
"""

# Create a Series using only data from "day1" and "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

my_var = pd.Series(calories, index = ["day1", "day2"])

print(my_var)
