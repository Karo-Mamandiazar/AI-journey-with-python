# Python String Tutorial
print('=== Python String Tutorial ===\n')

print('    ...---=== part one ===---...    ')

# Strings
print('___ String ___')
"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
"""

# You can display a string literal with the print() function:
print('Hello')
print("Hello")

print("----------------------------------------")

# Quotes Inside Quotes
print('___ quotes Inside Quotes ___')
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("it is alright")
print("He is called 'Karo'")
print('He is called "Karo"')

print("----------------------------------------")

# Assign String to a Variable
print('___ Assign String to a Variable ___')
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
x = "hello"
print(x)

print("----------------------------------------")

# Multiline Strings
print('___ Multiline String ___')

# You can assign a multiline string to a variable by using three quotes:
x = """Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
 sed do eiusmod tempor incididunt
 ut labore et dolore magna aliqua."""
print(x)

print('----------------------------------------')
# Or three single quotes:

x = '''Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
 sed do eiusmod tempor incididunt
 ut labore et dolore magna aliqua.'''
print(x)

print("----------------------------------------")

# Strings are Arrays
print('___ Strings are Arrays ___')
"""
 Like many other popular programming languages, strings in Python are arrays of unicode characters.

 However, Python does not have a character data type, a single character is simply a string with a length of 1.

 Square brackets can be used to access elements of the string.
"""

x = "x = 'Hello, World!'"
print(x)

print('___ Get the character at position 1 ( print(x[1]) ) ___')
# Get the character at position 1 (remember that the first character has the position 0):
print(x[1])

print("----------------------------------------")

# Looping Through a String
print('___ Looping Through a String ___')
"""
 Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""

print('___ Loop through the letters in the word "banana" ___')

for x in "banana":
    # Loop through the letters in the word "banana":
    print(x)

print("----------------------------------------")

# String Length
print('___ String Length ___')
"""
 To get the length of a string, use the len() function.
"""

x = "hello, world"
print(x)

print('___ use the len() function, To getting the length of "hello, world" ___')

print(len(x))  # The len() function returns the length of a string:

print("----------------------------------------")

# Check String
print('___ Check String ___')
"""
 To check if a certain phrase or character is present in a string, we can use the keyword in.
"""

txt = "TXT: (the best thing in life are free!)"
print(txt)

print('___ Check if "free" is present in the following text ___')
# Check if "free" is present in the following text:
print("free" in txt)

# Use it in an if statement:
print('Use it in an statement:')

print('___ Print only if "free" is present ___')
if "free" in txt:
    # Print only if "free" is present:
    print("yes, 'free' is present.")

print(20 * '-')

# Check if NOT
print('___ Check if NOT ___')
"""
 To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
"""

txt= "TXT: (the best thing in life are free!)"
print(txt)

print('___ Check if "expensive" is NOT present in the following text ___')
print("expensive" not in txt)
# Check if "expensive" is NOT present in the following text:

# Use it in an if statement:
print('Use it in an if statement:')

print('___ print only if "expensive" is NOT present ___')
if "expensive" not in txt:
    # print only if "expensive" is NOT present:
    print("no, 'expensive' is NOT present.")

print('    ...---=== part two ===---...    ')

# Python Slicing Strings
print('___ Python Slicing String ___')

print(15 * '-')

print('___ Slicing ___')
"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""

x = "TXT = 'Hello, World!'"
print(x)

print('___ Get the characters from position 2 to position 5 (not included) ___')
x = "Hello, world!"
print(x[2:5])  # Get the characters from position 2 to position 5 (not included):

print(15 * '-')

print('___ Slice From the Start ___')
"""
By leaving out the start index, the range will start at the first character:
"""

x = "TXT = 'Hello, world!'"
print(x)

print('___ Get the characters from the start to position 5 (not included) ___')
x = "Hello, World!"
print(x[:5])  # Get the characters from the start to position 5 (not included):

print(15 * '-')

print('___ Slice To the End ___')
"""
By leaving out the end index, the range will go to the end:
"""

x = "TXT = 'Hello, world!'"
print(x)

print('___ Get the characters from position 2, and all the way to the end ___')
x = "Hello, World!"
print(x[5:])  # Get the characters from position 2, and all the way to the end:

print(15 * '-')

print('___ Negative Indexing ___')
"""
Use negative indexes to start the slice from the end of the string:
"""

x = "TXT = 'Hello, world!'"
print(x)

x = "Hello, World!"
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
print(x[-5:-2])

print('    ...---=== part three ===---...    ')

# Python - Modify Strings
print('___ Python - Modify Strings ___')
"""
Python has a set of built-in methods that you can use on strings.
"""

# Upper Case
print('___ Upper Case ___')

A = "hello, world!"
# The upper() method returns the string in upper case:
print('Upper: ',A.upper())

# Lower Case
print('___ Lower Case ___')

A = "HELLO, WORLD"
# The lower() metod returns the string in lower case:
print('lower: ',A.lower())

# Remove Whitespace
print('___ Remove Whitespace ___')
"""
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
"""
A = "      Hello, World!       "
# The strip() method removes any whitespace from the beginning or the end:
print('Strip: ',A.strip()) # # returns "Hello, World!"


# Replace String
print('___ Replace String ___')

x = "Maro"
print(x)
# The replace() method replaces a string with another string:
print('Replace: ',x.replace("M", "K"))


# Split String
print('___ Split String ___')
"""
The split() method returns a list where the text between the specified separator becomes the list items.
"""
x = "Hello, World!"
# The split() method splits the string into substrings if it finds instances of the separator:
print('Split by comma: ',x.split()) # returns ['Hello', ' World!']

print('    ...---=== part four ===---...    ')

# String Concatenation
print('___ Strip Concatenation ___')
"""
To concatenate, or combine, two strings you can use the + operator.
"""

x = "Hello"
z = "World"
c = x + z # Merge variable a with variable b into variable c:
print('Without space: ', x + z)
print('With space: ', x + " " + z)

print('    ...---=== part five ===---...    ')

# Python - Format - Strings
print('___ Python - Format - Strings ___')

# String Format
"""
As we learned in the Python Variables Chapter, we cannot combine strings and numbers like this:

age = 18
# This will produce an error:

txt = "my name is Karo, I am " + age
print(txt)
"""

# But we can combine strings and numbers by using f-strings or the format() method!

# F-Strings
print('___ F-Strings ___')
"""
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and
 add curly brackets {} as placeholders for variables and other operations.
"""

age = 18
txt = f"My name is Karo, I am {age} years old"
print(txt)


# Placeholders and Modifiers
"""
A placeholder can contain variables, operations, functions, and modifiers to format the value.
"""
# Add a placeholder for the price variable:
price = 80
txt = f"The price is {price} dollars"
print(txt)
# A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type,
# like .2f which means fixed point number with 2 decimals:

price = 98
# Display the price with 2 decimals:
txt = f"The price is {price:.2f} dollars"
print(txt)

# A placeholder can contain Python code, like math operations:

txt = f"The price is {20 * 59} dollars "
print(txt)

print('    ...---=== part six ===---...    ')

# Python - Escape Characters
print('___ Python - Escape Characters')

# Escape Character
print('___ Escape Characters ___')
"""
To insert characters that are illegal in a string, use an escape character.
"""

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
"""
txt = "We are the so-called "Vikings" from the north."
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
print(txt)
"""

# To fix this problem, use the escape character \":

txt = "We are the so-called\"vikings\" from the north."
# The escape character allows you to use double quotes when you normally would not be allowed:
print(txt)


"""
# Escape Characters

Other escape characters used in Python:

Code:                              Result:

 \'                                Single Quote
 \\                                Backslash
 \n                                New Line
 \r                                Carriage Return
 \t                                Tab
 \b                                Backslash
 \f                                From Feed
"""
