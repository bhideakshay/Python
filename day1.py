# Python - Creator - Guido van Rossum (1991)

# Steps to learn any language -
# 1. Terms - Built in keywords, syntax
# 2. Data Types - to store information
# 3. Actions - Functions
# 4. Best Practices - Good ways to write code 

# Basics -------------------------------------------------------------------------------------------->

# Print your name
print("Akshay")

# Input and Print your name 
name = input('Type your name: ')
print(name)

# Simplified
print(input('Type your name: '))

# String concatenation
print("Hello "+ input('Type your name: '))

# Data Types -------------------------------------------------------------------------------------------->

# Python Data types

    # Fundamental Data Types 
        # Integer
        # Float
        # String
        # List
        # Tuple
        # Set
        # Dictionaries

    # None -> absence of value or nothing
    # Classes -> Custom type 
    # Specialized Data Types -> Not built into python but special packages or modules we can use from libraries
    # Complex - complex numbers 
    
# Int and Float
print(2+4)
print(type(2+4))
print(float((2+4)))

print(2+4)  # Addition
print(2-4)  # Subtraction
print(2*4)  # Multiplication
print(2/4)  # Division
print(type(2/4)) 

# Two raised to four
print(2**4) # Raised to 

# four divided by two -> returns remainder which is zero (Modulo operation)
print(4%2)  # Modulo operation

# Division which returns rounded off division
print(4//3)

# Note - floating point numbers take larger space in memory than integer

# Int + Int ==> Int
# Int + Float ==> Float
# Float + Float ==> Float

# Math functions (google -> 'python3 math functions')

# Round
print(round(3.4456))
print(round(3.4456,2)) # Round to two decimal places 

# Abs - Absolute value of element
print(abs(-20))

# Operator Precedence (BODMAS Rule)
# 1. ()
# 2. **
# 3. *
# 4. /
# 6. +
# 7. -
print((20-3)+2**2)

# Return binary equivalent of number
print(bin(4)) # Returns 0b100

# Return int of number
print(int('0b100',2)) # int(number, base)

# Variables ------------------------------------------------------------------------------------------------------------>
# Assigning a value is also called as binding

# Rules / Best practices for variable naming
# 1. snake_case
# 2. Start with lowercase or underscore
# 3. Letters, Numbers, underscores
# 4. Case sensitive
# 5. Don't overwrite keywords (google -> 'keywords in python)

snake_case = 'Hi I am snake case variable'
_variable_with_underscore = 'Variable with underscore' # Private variable
variable_with_number_123 = 'Variable with numbers'
user_iq = 'This is not equal to user_IQ'

# Variables can be re-assigned
iq = 190
iq = iq/4 
print(iq)

# constants - never change
PI = 3.14 # all capital (convention)
# __file__ -->  Dunder variables (should not create variables with two underscores)

a,b,c = 1,2,3 # Assign values to variables in a single line
print(a)
print(b)
print(c)

# Expression vs Statements
# Expression - Piece of code that produces a value -> 100/5
# Statement - An entire line of code that performs some action -> user_age = 100/5

# Augmented assignment operator 
some_variable = 5
some_variable = some_variable + 2
some_variable += 2 # With use of augmented assignment operator 
some_variable -= 2
some_variable *= 2

# Strings ----------------------------------------------------------------------------------------------------->
# Piece of text -> 'Hello' / "Hello" / 

# Sample Login Form 
username = 'supercocer'
password = 'somepassword'

long_string = '''
Multiline and 
Long String
'''

print(long_string)

first_name = 'John'
last_name = 'Doe'

full_name = first_name + " " + last_name
print(full_name)

# String Concatenation - adding strings together
# print('Hello' + 5)   # will give type error

# Type Conversion
print(int(str(100))) # Type conversion from int --> str --> int --> then print

# Escape sequences
# weather = "It's "kind of" sunny" # without escape sequences 
weather = "\tIt\'s\n \"kind of\" \n sunny\\"
print(weather)

# \t - Tab
# \n - Next line

# Formatted Strings
name = 'John'
age = 50
print('Hi ' + name)

print('Hi ' + name + "." + "You are " + str(age) + " years old.")

print('Hi {}.You are {} years old'.format(name,age)) # Old way in python2
print('Your age is {1}.You are {0}'.format(name,age)) # Old way in python2
print('Hi {new_name}.You are {age} years old'.format(new_name='Doe',age=60)) # Old way in python2

print(f'Hi {name}.You are {age} years old') # New way in python3

# String Indexes
sample_str = 'Hi Johnny'
# Indexes     012345678
print(sample_str[0])    # returns H at first place
print(sample_str[-1])   # returns n at 8th place
print(sample_str[-2])   # returns n at 7th place

# String slicing
# [start:stop:step-over] 
print(sample_str[1:4])   # returns i J at 1st to 3rd place
print(sample_str[0:8:2])
print(sample_str[1:])
print(sample_str[::1])
print(sample_str[::-1]) # Palindrome - Reverse a string
print(sample_str[::-2])

# Immutability
    # Strings in python are immutable
    # sample_str[0] = '1' # Will throw error as strings are immutable
    # Only way to change is re-assign or create new string

