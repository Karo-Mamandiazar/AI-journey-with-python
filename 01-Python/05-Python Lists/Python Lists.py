print("---=== Python Lists ===---")

# -- Part One (1) --

mylist = ["apple", "banana", "cherry"]

print('--- List ---')
"""
 Lists are used to store multiple items in a single variable.
 
 Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set,
  and Dictionary, all with different qualities and usage.
"""

# Lists are created using square brackets:

# Create a List:
this_list = ["apple", "banana", "cherry"]
print(this_list)

print('-------------------------')

print('--- List Items ---')

"""
 List items are ordered, changeable, and allow duplicate values.
 
 List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

print('-------------------------')

print('--- Ordered ---')
"""
 When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
 
 If you add new items to a list, the new items will be placed at the end of the list.
"""

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

print('-------------------------')

print('--- Changeable ---')
"""
 The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""

print('-------------------------')

print('--- Allow Duplicate ---')

# Since lists are indexed, lists can have items with the same value:

# Lists allow duplicate values:
this_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(this_list)

print('-------------------------')

print('--- List Length ---')

# To determine how many items a list has, use the 'len()' function:

# Print the number of items in the list:
this_list = ["apple", "banana", "cherry"]
print(len(this_list))

print('-------------------------')

print('--- List Items - Data Types ---')

# List items can be of any data type:

# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# - A list can contain different data types:

# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

print('-------------------------')

print('--- type() ---')

# From Python's perspective, lists are defined as objects with the data type 'list':

# What is the data type of a list?
my_list = ["apple", "banana", "cherry"]
print(type(my_list))

print('-------------------------')

print('--- The list() Constructor ---')
"""
 It is also possible to use the list() constructor when creating a new list.
"""

# Using the list() constructor to make a List:
this_list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(this_list)

print('--------------------------------------------------')

print("---=== Python - Access List Items ===---")

# -- Part Two (2) ---

print('--- Access Items ---')

# List items are indexed and you can access them by referring to the index number:

# Print the second item of the list:
this_list = ["apple", "banana", "cherry"]
print(this_list[1])

# Note: The first item has index 0.

print('-------------------------')

print('--- Negative Indexing ---')
"""
 Negative indexing means start from the end
 
 -1 refers to the last item, -2 refers to the second last item etc.
"""

# Print the last item of the list:
this_list = ["apple", "banana", "cherry"]
print(this_list[-1])

print('-------------------------')

print('--- Range of Indexes ---')
"""
 You can specify a range of indexes by specifying where to start and where to end the range.

 When specifying a range, the return value will be a new list with the specified items.
"""

# Return the third, fourth, and fifth item:
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:

# This example returns the items from the beginning to, but NOT including, "kiwi":
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[:4])

# By leaving out the end value, the range will go on to the end of the list:

# This example returns the items from "cherry" to the end:
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[2:])

print('-------------------------')

print('--- Range of Negative Indexes ---')

# Specify negative indexes if you want to start the search from the end of the list:

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(this_list[-4:-1])

print('-------------------------')

print('--- Check if Item Exists ---')

# To determine if a specified item is present in a list use the in keyword:

# Check if "apple" is present in the list:
this_list = ["apple", "banana", "cherry"]
if "apple" in this_list:
  print("Yes, 'apple' is in the fruits list")

print('--------------------------------------------------')

print("---=== Python - Change List Items ===---")

# -- Part Three (3) ---

print('--- Change Item Value ---')

# To change the value of a specific item, refer to the index number:

# Change the second item:
this_list = ["apple", "banana", "cherry"]
this_list[1] = "blackcurrant"
print(this_list)

print('-------------------------')

print('--- Change a Range of Items Values ---')

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["blackcurrant", "watermelon"]
print(this_list)

# - If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Change the second value by replacing it with two new values:
this_list = ["apple", "banana", "cherry"]
this_list[1:2] = ["blackcurrant", "watermelon"]
print(this_list)

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Change the second and third value by replacing it with one value:
this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)

print('-------------------------')

print('--- Insert Items ---')
"""
 To insert a new list item, without replacing any of the existing values, we can use the insert() method.
"""

# The insert() method inserts an item at the specified index:

# Insert "watermelon" as the third item:
this_list = ["apple", "banana", "cherry"]
this_list.insert(2, "watermelon")
print(this_list)

# Note: As a result of the example above, the list will now contain 4 items.

print('--------------------------------------------------')

print("---=== Python - Add List Items ===---")

# -- Part Four (4) ---

print('--- Append Items ---')

# To add an item to the end of the list, use the append() method:

# Using the append() method to append an item:
this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
print(this_list)

print('-------------------------')

print('--- Insert Items ---')
"""
 To insert a list item at a specified index, use the insert() method.
"""

# The insert() method inserts an item at the specified index:

# Insert an item as the second position:
this_list = ["apple", "banana", "cherry"]
this_list.insert(1, "orange")
print(this_list)

# Note: As a result of the examples above, the lists will now contain 4 items.

print('-------------------------')

print('--- Extend List ---')
"""
 To append elements from another list to the current list, use the extend() method.
"""

# Add the elements of tropical to this_list:
this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)

# The elements will be added to the end of the list.

print('-------------------------')

print('--- Add Any Iterable ---')
"""
 The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""

# Add elements of a tuple to a list:
this_list = ["apple", "banana", "cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)

print('--------------------------------------------------')

print("---=== Python - Remove List Items ===---")

# -- Part Five (5) ---

print('--- Remove Specified Item ---')
"""
 The remove() method removes the specified item.
"""

# Remove "banana":
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)

# - If there are more than one item with the specified value, the remove() method removes the first occurrence:

# Remove the first occurrence of "banana":
this_list = ["apple", "banana", "cherry", "banana", "kiwi"]
this_list.remove("banana")
print(this_list)

print('-------------------------')

print('--- Remove Specified Index ---')
"""
 The pop() method removes the specified index.
"""

# Remove the second item:
this_list = ["apple", "banana", "cherry"]
this_list.pop(1)
print(this_list)

# - If you do not specify the index, the pop() method removes the last item.

# Remove the last item:
this_list = ["apple", "banana", "cherry"]
this_list.pop()
print(this_list)

# - The del keyword also removes the specified index:

# Remove the first item:
this_list = ["apple", "banana", "cherry"]
del this_list[0]
print(this_list)

# - The del keyword can also delete the list completely.

# Delete the entire list:
this_list = ["apple", "banana", "cherry"]
del this_list

print('-------------------------')

print('--- Clear the List ---')
"""
 The clear() method empties the list.

 The list still remains, but it has no content.
"""

# Clear the list content:
this_list = ["apple", "banana", "cherry"]
this_list.clear()
print(this_list)

print('--------------------------------------------------')

print("---=== Python - Loop Lists ===---")

# -- Part Six (6) ---

print('--- Loop Through a List ---')

# You can loop through the list items by using a for loop:

# Print all items in the list, one by one:
this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)

print('-------------------------')

print('--- Loop Through the Index Numbers ---')
"""
 You can also loop through the list items by referring to their index number.

 Use the range() and len() functions to create a suitable iterable.
"""

# Print all items by referring to their index number:
this_list = ["apple", "banana", "cherry"]
for i in range(len(this_list)):
  print(this_list[i])

# The iterable created in the example above is [0, 1, 2].

print('-------------------------')

print('--- Using a While Loop ---')
"""
 You can loop through the list items by using a while loop.

 Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

 Remember to increase the index by 1 after each iteration.
"""

# Print all items, using a while loop to go through all the index numbers
this_list = ["apple", "banana", "cherry"]
i = 0
while i < len(this_list):
  print(this_list[i])
  i = i + 1

print('-------------------------')

print('--- Looping Using List Comprehension ---')

# List Comprehension offers the shortest syntax for looping through lists:

# A short hand for loop that will print all items in a list:
this_list = ["apple", "banana", "cherry"]
[print(x) for x in this_list]

print('--------------------------------------------------')

print("---=== Python - List Comprehension ===---")

# -- Part Seven (7) ---

print('--- List Comprehension ---')
"""
 List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
 
 Example:
 Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
"""

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
  if "a" in x:
    new_list.append(x)

print(new_list)

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]

print(new_list)

# The Syntax
# new_list = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

print('-------------------------')

print('--- Condition ---')
"""
 The condition is like a filter that only accepts the items that evaluate to True.
"""

# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if x != "apple"]

print(new_list)

"""
 The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
"""

# The condition is optional and can be omitted:

# With no if statement:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits]

print(new_list)

print('-------------------------')

print('--- Iterable ---')
"""
 The iterable can be any iterable object, like a list, tuple, set etc.
"""

# You can use the range() function to create an iterable:
new_list = [x for x in range(10)]

print(new_list)

# - Same example, but with a condition:

# Accept only numbers lower than 5:
new_list = [x for x in range(10) if x < 5]

print(new_list)

print('-------------------------')

print('--- Expression ---')
"""
 The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
"""

# Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x.upper() for x in fruits]

print(new_list)

# - You can set the outcome to whatever you like:

# Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = ['hello' for x in fruits]

print(new_list)

# - The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x if x != "banana" else "orange" for x in fruits]

print(new_list)

"""
 The expression in the example above says:

 "Return the item if it is not banana, if it is banana return orange".
"""

print('--------------------------------------------------')

print("---=== Python - Sort Lists ===---")

# -- Part Eight (8) ---

print('--- Sort List Alphanumerically ---')

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Sort the list alphabetically:
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)

# Sort the list numerically:
this_list = [100, 50, 65, 82, 23]
this_list.sort()
print(this_list)

print('-------------------------')

print('--- Sort Descending ---')

# To sort descending, use the keyword argument reverse = True:

# Sort the list descending:
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse = True)
print(this_list)

# Sort the list descending:
this_list = [100, 50, 65, 82, 23]
this_list.sort(reverse = True)
print(this_list)

print('-------------------------')

print('--- Customize Sort Function ---')
"""
 You can also customize your own function by using the keyword argument key = function.
"""

# The function will return a number that will be used to sort the list (the lowest number first):

# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

this_list = [100, 50, 65, 82, 23]
this_list.sort(key = myfunc)
print(this_list)

print('-------------------------')

print('--- Case Insensitive Sort ---')

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Case sensitive sorting can give an unexpected result:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort()
print(this_list)

# Luckily we can use built-in functions as key functions when sorting a list.

# - So if you want a case-insensitive sort function, use str.lower as a key function:

# Perform a case-insensitive sort of the list:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key = str.lower)
print(this_list)

print('-------------------------')

print('--- Reverse Order ---')
"""
 What if you want to reverse the order of a list, regardless of the alphabet?

 The reverse() method reverses the current sorting order of the elements.
"""

# Reverse the order of the list items:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.reverse()
print(this_list)

print('--------------------------------------------------')

print("---=== Python - Copy Lists ===---")

# -- Part Nine (9) ---

print('--- Copy a List ---')
"""
 You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
"""

print('-------------------------')

print('--- Use the copy() method ---')
"""
 You can use the built-in List method copy() to copy a list.
"""

# Make a copy of a list with the copy() method:
this_list = ["apple", "banana", "cherry"]
my_list = this_list.copy()
print(my_list)

print('-------------------------')

print('--- Use the list() method ---')
"""
 Another way to make a copy is to use the built-in method list().
"""

# Make a copy of a list with the list() method:
this_list = ["apple", "banana", "cherry"]
my_list = list(this_list)
print(my_list)

print('-------------------------')

print('--- Use the slice Operator ---')
"""
 You can also make a copy of a list by using the : (slice) operator.
"""

# Make a copy of a list with the : operator:
this_list = ["apple", "banana", "cherry"]
my_list = this_list[:]
print(my_list)

print('--------------------------------------------------')

print("---=== Python - Join Lists ===---")

# -- Part Ten (10) ---

print('--- Join Two Lists ---')
"""
 There are several ways to join, or concatenate, two or more lists in Python.

 One of the easiest ways are by using the + operator.
"""

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# - Another way to join two lists is by appending all the items from list2 into list1, one by one:

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# - Or you can use the extend() method, where the purpose is to add elements from one list to another list:

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
