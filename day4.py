# Functions
def say_hello(name):
    print('Hello ' + name)

#calling a function
say_hello('John')

# Arguments vs Parameters
def say_hello_with_emoji(name, emoji):  # Parameters - used when we define the function (Positional parameters)
    print(f'Hello {name} {emoji}')

say_hello_with_emoji('John', '😁')      # Arguments - used while calling / invoking a function (Positional arguments)

# Keyword arguments
say_hello_with_emoji(emoji='😁', name='John Doe')     # Bad practice

# Default parameters
def func_with_default_pramas(name='John',age='55'):
    print(f'Hello {name}, your age is {age}')


func_with_default_pramas('Rohn',60)     # Providing arguments
func_with_default_pramas()              # Default parameters used

# Return
# 1. It returns something 
# 2. Doesn't returns anything but modifies something
# 3. It automatically exists the function
def cal_sum(num1, num2):
    return num1 + num2      # Returns the value

print(f'The cal_sum of numbers is : {cal_sum(1,2)}')

# For good function
# 1. Should do one thing really well
# 2. Should return something

total = cal_sum(10,15)
print(f'The cal_sum is : {total}')
print(f'The cal_sum is : {cal_sum(100,total)}')

# Nested functions
def outer_func(num1,num2):
    def inner_func(n1,n2):
        return n1 + n2
    return inner_func(num1,num2)

total = outer_func(10,2)
print(f'Multiplication is : {total}')

# Methods vs Functions
# Methods needs to be owned
    # eg - 'Hello'.capitalize()

# Docstrings
def test_func(a):
    '''
    Info : This function prints given parameters
    '''
    print(a)

test_func('a')

help(test_func) # Returns 'Info : This function prints given parameters'

print(test_func.__doc__)    # By using magic method or dunder method

# Clean Code
def is_even(num):
    if (num % 2) == 0:
        return True
    elif (num % 2) !=0: 
        return False

print(is_even(5))

# Cleaned code
def is_even(num):
    if (num % 2) == 0:
        return True
    return False

print(is_even(7))

# More cleaned code 
def is_even(num):
    return (num % 2 == 0)

print(is_even(4))


# Arguments and Keyword Arguments
# *args, **kwargs

# *args
def super_func(*args):
    print(args)
    print(*args)
    return sum(args)

print(super_func(1,2,3,4,5,6))

# **kwargs
def another_super_func(*args, **kwargs):
    print(args)
    print(*args)
    print(kwargs)
    print(*kwargs)
    total = 0 
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(another_super_func(1,2,3,4,5,num1=5,num2=10))

# Rule : params, *args, default parameters, **kwargs


# Exercise 
# Print highest even from list

def highest_even(li):
    li.sort(reverse=True)
    print(li)
    for item in li:
        if item % 2 == 0:
            return item

print(f'Highest even number is: {highest_even([10,2,3,4,8,11])}') 

# Another logic
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(f'Highest even number is: {highest_even([10,2,3,4,8,11])}') 

# Walrus operator 
# :=
# This operator assigns values to variables as part of a larger expression

a_str = 'Helooooooooooo'
if (len(a_str)>10):
    print(f'Too long {len(a_str)} elements')

# with the use of walrus operator
if ((n := len(a_str))>10):
    print(f'Too long {n} elements')


a = 'Helooooooooooo'
while ((n:=len(a))>1):
    print(n)
    a = a[:-1]

print(a)

# Read release notes for python version --> whats new in python 3.10?


# Scope - what variables do I have access to (Functional Scope)
# 1. Global Scope - anybody has access to it
# 2. Local Scope

if True:
    x = 10

def some_func():
    total = 100

print(x)

# Exercise - Scope rules
a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

# Rules - Checking if variable is present (Inner to Outer(Global)) 
# 1. Start with local scope
# 2. Parent Local Scope
# 3. Global scope
# 4. Built in Python functions

# Parameters - Considered as local variables

# Global keyword -> Not good way of doing this - Bad practice
total = 0 

def count():
    global total
    total += 1
    return total

count()
count()
print(count())

# Better way - Dependency injection
total = 0 

def count(total):
    total += 1
    return total


print(count(count(count(total))))


# nonlocal keyword
# Want to use a variable which is not in my scope of function but outside of my function but not global
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('Inner', x)
    
    inner()
    print("outer", x)

outer()


# Why do we need scope???

# Python Developer Tools - 
# Terminal / CMD 
# Code editors - Sublime Text, VS code (They are lightweight)
# Integrated development Environments(IDE) - PyCharm, SPYDER (Full fledged environment)
# Notebooks - Jupyter Notebooks

# Code formatting
# autopep8