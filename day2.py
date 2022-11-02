# Built in functions / methods --------------------------------------------------------------------------------------------------->
print(len('Hello')) # Length does't start with 0 , it starts ith 1

greet = 'Hello'
print(greet[0:len(greet)])

# String methods - specifically for strings
# .format()

quote = 'To be or not to be'

print(quote.upper())    # Capitalize whole string
print(quote.capitalize())   # Capitalize start of string
print(quote.lower())    # Lower case whole string
print(quote.find('be')) # Find first instance
print(quote.replace('be','me')) # replace string by another string

print(quote)    # Strings are immutable


# Booleans --------------------------------------------------------------------------------------------------->
# True / False
# Useful in logical programming
name = 'Your name'
is_cool = False
is_cool = True

print(bool(1))
print(bool(0))

# Exercise type conversions ---------------------------------------------------------------------------------->

# Program that guesses your age
birth_year = int(input('What year you were born? : '))
curr_year = 2022
print(f'Your age is: {curr_year-birth_year}')

# Simplified
age = 2022-int(input('What year you were born? : '))
print(f'Your age is: {age}')

# Commenting your code --------------------------------------------------------------------------------------->
# Add valuable comments 
# Reference (Real Python - Writing comments in python)

# Password checker
    # Ask for username
    # Ask for password
    # Print - Hey {username}, your password {****} is {4} letters long

username = input('Please enter username: ')
password = input('Please enter password: ')
secret_password = '*' * len(password)
print(f'Hey {username.capitalize()}, Your password {secret_password} is {len(password)} letters long.')

# Lists -------------------------------------------------------------------------------------------------------->
# Sequence of objects of any type (form of arrays)
# Collection of items
# Lists are mutable
# Data Structures - way to organize data
 
li = ['Hello' , 'World', 1, 2, 3, 4, True]
amazon_cart = ['notebooks','gadgets','sunglasses']

print(amazon_cart[0])
# print(amazon_cart[3])   # Will return exception - list index out of range as list has only 3 elements and count starts from 0

# List slicing
print(amazon_cart[0:1])
print(amazon_cart[::-1]) # Reverse list items

amazon_cart = [
    'item_one',
    'item_two',
    'item_three',
    'item_four',
    'item_five'
]

print(amazon_cart)

amazon_cart[0] = 'item_first'

print(amazon_cart)

print(amazon_cart[0:6:2])

# Tricky thing about lists
amazon_cart[0] = 'item_one'
new_cart = amazon_cart
new_cart[0] = 'item_first'
print(new_cart) # Returns ['item_first', 'item_two', 'item_three', 'item_four', 'item_five']
print(amazon_cart)  # Returns ['item_first', 'item_two', 'item_three', 'item_four', 'item_five']

# new_cart = amazon_cart
# because we have assigned same memory location for both variables(lists),
# when you modify second list, first also changes

# To avoid that, we can do like - 
amazon_cart[0] = 'item_one'
new_cart = amazon_cart[:]
new_cart[0] = 'item_first'
print(new_cart) # Returns ['item_first', 'item_two', 'item_three', 'item_four', 'item_five']
print(amazon_cart)  # Returns ['item_one', 'item_two', 'item_three', 'item_four', 'item_five']


# Matrix - way to describe multi-dimensional lists

# Multi dimensional array
matrix = [
    [1,2,3],
    [5,6,7],
    [8,9,10]
]

# Access 7
print(matrix[1][2])

# List methods
basket = [1,2,3,4,5,6,7,8]

print(len(basket))

# Adding items to list
# Append - changes the list in place 
basket.append(100)
print(basket)

# Insert 
basket.insert(1,100)
print(basket)

# Extend -  it takes iterable as an argument
basket.extend([101,102,103])
print(basket)

# Removing methods
# POP - pops last element in list
basket.pop()
print(basket)

basket.pop(1)
print(basket)

# Remove
basket.remove(102)
print(basket)

popped_item = basket.pop(2)
print(popped_item)
print(basket)

# Clear
basket.clear()
print(basket)

# Index
basket =  ['a','b','c','d','e','f','g','d']

print(basket.index('c'))
print(basket.index('d',1,4))

# in keyword
print('d' in basket)

# Count
print(basket.count('d'))

# Sort
basket.sort()
print(basket)

# Reverse Sort
basket.sort(reverse=True)
print(basket)

# Sorted vs Sort

print(basket)
print(sorted(basket))   # Creates a new list

# Copy
new_list = basket[:]
print(new_list)

new_list = basket.copy()
print(new_list)

# Reverse - only reverse without sorting 
basket.reverse()
print(basket)

# Common list patterns
# Range
print(range(1,100))
print(list(range(1,100)))
print(list(range(6)))

# Join
sentence ="-"
new_sentence = sentence.join(['Hi','my','name','is','AB'])
print(new_sentence)

# Simplified
new_sentence = ' '.join(['Hi','my','name','is','AB'])
print(new_sentence)

# List unpacking
li = [1,2,3,4,5]

# If want to assign variable to each item in list
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

# If we wat to assign a->1, b->2, c->3  and remaining to other variable
a,b,c,*other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)

a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

# None ------------------------------------------------------------------------------------------------------------->
# Special datatype - represents absence of value
weapons = None

# Dictionaries ------------------------------------------------------------------------------------------------------>
# data-type in python also a data structure
# Unordered key value pair 
dictionary = {
    'a' : 1,
    'b' : 2
}

print(dictionary['b'])

dictionary = {
    'a' : [1,2,3],
    'b' : 'Hello',
    'c' : True
}

print(dictionary['a'][1])

mylist = [
    {
        'a' : [1,2,3],
        'b' : 'Hello',
        'c' : True
    },
    {
        'a' : [1,2,3],
        'b' : 'Hello',
        'c' : True
    },
]

print(mylist[0]['a'][2])

# Understanding Data Structures -------------------------------------------------------------------------------------->
# When to use list - sorted items,
# When to use dictionary - unordered items, holds more information

# Dictionary keys
# key - needs to be immutable, has to be unique
dictionary = {
    123 : [1,2,3],
    'b' : 'Hello',
    'c' : True
}

print(dictionary[123])

dictionary = {
    'a' : [1,2,3],
    True : 'Hello',
    'c' : True
}

print(dictionary[True])

# Dictionary methods
user = {
    'basket': [1,2,3],
    'greet' : 'Hello'
}

# Get method
print(user.get('age'))
print(user.get('age',50))   # You can add default value if key is not present

# Not common way to create dictionary
user2 = dict(name='John',age=55)
print(user2)

user3 = {
    'basket': [1,2,3],
    'greet' : 'Hello',
    'age'   : 50
}

print('basket' in user3)
print('size' in user3)
print('age' in user3.keys())
print('Hello' in user3.values())

print(user3.items())

user3.clear()
print(user3)

user4 = {
    'basket': [1,2,3],
    'greet' : 'Hello',
    'age'   : 50
}

# Copy
user5 = user4.copy()
print(user5)

# POP
print(user5.pop('age'))
print(user5)

# POP Item
print(user5.popitem())
print(user5)

# Update
print(user5.update({'age':70}))
print(user5)


# Tuples ---------------------------------------------------------------------------------------------------------------->
# Immutable lists
# Less flexible than lists
# Slightly performant than list
# example - Lat Long storing
my_tuple = (1,2,3,4,5,6)

print(my_tuple[1])
print(5 in my_tuple)

user = {
    (1,2) : [1,2,3],
    'greet' : 'Hello',
    'age' : 20
}

print(user[(1,2)])

new_tuple = my_tuple[1:3]
print(new_tuple)

x,y,z,*other = (1,2,3,4,5,6,7)

print(x)
print(y)
print(z)
print(other)

my_tuple = (1,2,3,4,5,5,6,7,8)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))


# Sets --------------------------------------------------------------------------------------------------------------->
# Unordered collections of unique objects
# Set object does not support indexing

my_set = {1,2,3,4,5,6,7}
print(my_set)

my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1,2,3,4,5,5,6,7,8,9]
my_unique = set(my_list)
print(my_unique)

print(1 in my_unique)
print(len(my_unique))

new_set = my_unique.copy()
my_unique.clear()
print(new_set)


# Set methods
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# Difference
print(my_set.difference(your_set))

# Discard
print(my_set.discard(5))
print(my_set)

# Difference update
print(my_set.difference_update(your_set))
print(my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# Intersection
print(my_set.intersection(your_set))
print(my_set & your_set)

# Is Dis Joint
print(my_set.isdisjoint(your_set))

my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
# Is subset
print(my_set.issubset(your_set))

# Is Superset
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))

# Union
print(my_set.union(your_set))
print(my_set | your_set)