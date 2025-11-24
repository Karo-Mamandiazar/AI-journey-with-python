print("---=== Python Tuples ===---")

# Part One

my_tuple = ("apple", "banana", "cherry")

print('--- Tuple ---')
"""
 Tuples are used to store multiple items in a single variable.

 Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
 
 A tuple is a collection which is ordered and unchangeable.
 
 Tuples are written with round brackets.
"""

# Create a Tuple:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)

print('------------------------------')

print('--- Tuple Items ---')
"""
 Tuple items are ordered, unchangeable, and allow duplicate values.

 Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
"""

print('------------------------------')

print('--- Ordered ---')
"""
 When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
"""

print('------------------------------')

print('--- Unchangeable ---')
"""
 Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
"""

print('------------------------------')

print('--- Allow Duplicates ---')
"""
 Since tuples are indexed, they can have items with the same value:
"""
# Tuples allow duplicate values:

this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)

print('------------------------------')

print('--- Tuple Length ---')

# To determine how many items a tuple has, use the len() function:

# Print The number of items in the tuple:
this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple))

print('------------------------------')

print('--- Create Tuple With One Item ---')
"""
 To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""

# One item tuple, remember the comma:
this_tuple = ("apple",) # remember the comma

print('------------------------------')

print('--- Tuple Items - Data Types ---')

# Tuple items can be of any data type:

# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print('------------------------------')

print('--- A tuple can contain different data types: ---')

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

print('------------------------------')

print('--- type() ---')

# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# What is the data type of tuple?
my_tuple = ("apple", "banana", "cherry")
print(type(my_tuple))

print('------------------------------')

print('--- The tuple() Constructor ---')
"""
 It is also possible to use the tuple() constructor to make a tuple.
"""

# Using the tuple() method to make a tuple:
this_tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(this_tuple)

print('------------------------------')

print("---=== Python - Access Tuple Items ===---")

# Part Two

print('--- Access Tuple Items ---')

# You can access tuple items by referring to the index number, inside square brackets:

# Print the second item in the tuple:
this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])

# Note: The first item has index 0.

print('------------------------------')

print('--- Negative Indexing ---')
"""
 Negative indexing means start from the end.

 -1 refers to the last item, -2 refers to the second last item etc.
"""

# Print the last item of the tuple:

this_tuple = ("apple", "banana", "cherry")
print(this_tuple[-1])

print('------------------------------')

print('--- Range of Indexes ---')
"""
 You can specify a range of indexes by specifying where to start and where to end the range.

 When specifying a range, the return value will be a new tuple with the specified items.
"""

# Return the third, fourth, and fifth item:
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Remember that the first item has index 0.


# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to, but NOT included, "kiwi":
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[:4])


# By leaving out the end value, the range will go on to the end of the tuple:
# This example returns the items from "cherry" and to the end:
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:])

print('------------------------------')

print('--- Range of Negative Indexes ---')

# Specify negative indexes if you want to start the search from the end of the tuple:

# This example returns the items from index -4 (included) to index -1 (excluded)
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])

print('------------------------------')

print('--- Check if Item Exists ---')

# To determine if a specified item is present in a tuple use the in keyword:

# Check if "apple" is present in the tuple:
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
  print("Yes, 'apple' is in the fruits tuple")

print('------------------------------')

print("---=== Python - Update Tuples ===---")

# Part Three

"""
 Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

 But there are some workarounds.
"""

print('--- Change Tuple Values ---')
"""
 Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

 But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print('------------------------------')

print('--- Add Items ---')
"""
 Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
"""

"""
 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
"""
# Convert the tuple into a list, add "orange", and convert it back into a tuple:
this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.append("orange")
this_tuple = tuple(y)

"""
 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""
# Create a new tuple with the value "orange", and add that tuple:
this_tuple = ("apple", "banana", "cherry")
y = ("orange",)
this_tuple += y

print(this_tuple)

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

print('------------------------------')

print('--- Remove Items ---')

# Note: You cannot remove items in a tuple.

"""
 Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
"""

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.remove("apple")
this_tuple = tuple(y)


# - Or you can delete the tuple completely:


# The del keyword can delete the tuple completely:
this_tuple = ("apple", "banana", "cherry")
del this_tuple
# print(this_tuple)
#
# #this will raise an error because the tuple no longer exists

print('------------------------------')

print("---=== Python - Unpack Tuples ===---")

# Part Four

print('--- Unpacking a Tuple ---')

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

#Packing a tuple:
fruits = ("apple", "banana", "cherry")


# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":


# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

print('------------------------------')

print('--- Using Asterisk ---')

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

"""
 If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
"""

# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print('------------------------------')

print("---=== Python - Loop Tuples ===---")

# Part Five

print('--- Loop Through a Tuple ---')
"""
 You can loop through the tuple items by using a for loop.
"""

# Iterate through the items and print the values:
this_tuple = ("apple", "banana", "cherry")
for x in this_tuple:
  print(x)

print('------------------------------')

print('--- Loop Through the Index Numbers ---')
"""
 You can also loop through the tuple items by referring to their index number.

 Use the range() and len() functions to create a suitable iterable.
"""

# Print all items by referring to their index number:
this_tuple = ("apple", "banana", "cherry")
for i in range(len(this_tuple)):
  print(this_tuple[i])

print('------------------------------')

print('--- Using a While Loop ---')
"""
 You can loop through the tuple items by using a while loop.

 Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

 Remember to increase the index by 1 after each iteration.
"""

# Print all items, using a while loop to go through all the index numbers:
this_tuple = ("apple", "banana", "cherry")
i = 0
while i < len(this_tuple):
  print(this_tuple[i])
  i = i + 1

print('------------------------------')

print("---=== Python - Join Tuples ===---")

# Part Six

print('--- Join Two Tuples ---')

# To join two or more tuples you can use the + operator:

# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print('--- Multiply Tuples ---')

# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2

print(my_tuple)
