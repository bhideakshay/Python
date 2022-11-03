# Conditional logic

# Controlling the flow

# if...elif... else ------------------------------------------------------------------------------------------->
is_old = False
is_licenced = True

if is_old:
    print('You are old enough to drive')
elif is_licenced:
    print('You can drive')
else:
    print('You are not old enough to drive')


if is_old and is_licenced:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')


# Indentation in python

# Truthy and Falsy

a = 'Hello'
b = 5

if a and b:     # a = True , b = True and both combined --> a and b --> Truthy 
    print('True')

print(bool(''))     # Falsy
print(bool(None))   # Falsy


# Ternary Operator / Conditional expressions
# 'do this' if 'condition' true else 'do this' 

# Example
# If user can msg you
is_friend = True
can_message = 'Yes, can message' if is_friend else 'No, can\'t message'
print(can_message)

# Short circuiting
is_friend = True
is_user = True
is_not = False

if is_friend and is_user:
    print('Best friends')

if is_not and is_user:        # short circuiting
    print('Best friends')

if is_friend or is_user:        # short circuiting-more efficient
    print('Best friends')

if is_friend or 0:        # short circuiting
    print('Best friends')


# Logical Operators ------------------------------------------------------------------------------------------->

# AND                       --> and
# OR                        --> or
# Greater than              --> >
# Less than                 --> <
# Equal to                  --> ==
# Not equal to              --> !=
# Greater than or equal to  --> >=
# Less than or equal to     --> <=
# Not (Inversion)           --> not   # Its a keyword as well as function --> not and not(True)

print('a' > 'b')    # Returns False due to bitwise operation 
print('a' > 'A')    # Returns True due to bitwise operation 

print(not(True))    # Not as a function


# Exercise
is_magician = True
is_expert = False

# check if magician and expert : 'You are an expert magician'
# check if magician but not expert : 'You are magician but not an expert'
# else you are not a magician : 'You need magic powers'

if is_expert and is_magician:
    print('You are an expert magician')
# elif is_magician or is_expert:                      # Short circuiting
#     print('You are magician but not an expert')
elif is_magician and not is_expert:                      # Short circuiting
    print('You are magician but not an expert')
elif not is_magician:
    print('You need magic powers')


# 'is' vs '=='
# == checks for Equality and value
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])

# 'is' checks for checks for memory location in which he values are stored
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])

# Loops ------------------------------------------------------------------------------------------->
# Allows us to run piece of code multiple times

# for...loop
# iterate over iterables

for item in ('Hello'):
    print(item)

for item in range(0,4):
    print(item)

# Nested loops
for x in range(0,3):
    for y in ('a','b','c'):
        print(y)


# Iterables -> one by one check each item
# Objects or collection that can be iterated over
# list, dictionary, tuple, sets, strings

user = {
    'name' : 'John',
    'age'  : 55,
    'can_swim' : False
}

for item in user.items():
    print(item)

# Returns
# ('name', 'John')
# ('age', 55)
# ('can_swim', False)

for item in user.values():
    print(item)

# Returns
# John
# 55
# False

for item in user.keys():
    print(item)

# Returns
# name
# age
# can_swim


for item in user.items():
    key, value = item
    print(key,value)

# Returns
# name John
# age 55
# can_swim False


# simplified
for key, value in user.items():
    print(key,value)

# Returns
# name John
# age 55
# can_swim False

# Exercise
# Simple counter to count items in my list

my_list = [1,2,3,4,5,6,7,8,9,10]

total = 0
for item in my_list:
    # total = total + item
    total += item
print(total)
print(len(my_list))

# Range()
print(range(100))
print(list(range(100)))

print(list(range(0, 100)))

for number in range(0,10):
    print(number)

# if no variable is required we use '_'
for _ in range(0,10):
    print(_)

for _ in range (0,11,2):
    print(_)

# Descending
for _ in range (11,0,-1):
    print(_)

for _ in range (2):
    print(list(range(10)))


# Enumerate()
# If you need index counter for the item you are iterating over

for _ in enumerate('Hello'):
    print(_)

# Returns
# (0, 'H')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

for index, char in enumerate('Hello'):
    print(index, char)

# Exercise
# Enumerate list of 100 numbers and print the index of number 50

for index, num in enumerate(list(range(100))):
    if num == 50:
        print(f'The index of 50 is: {index}')
 


# While loops -------------------------------------------------------------------------->

i = 0 
while i <= 50:
    print(i)
    i+=1

# else block in while loop
i = 0
while i < 50:
    print(i)
    i+=1
else:
    print('Done...!!!')

# Break
i = 0
while i < 50:
    print(i)
    i+=1
    break
else:                           # Else block will not be executed
    print('Done...!!!')


# for loop vs while loop
my_list = [1,2,3,4,5,6,7,8,9]

for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1  


while True:
    response = input('Type Something : ')
    if (response == 'bye'):
        break


# Break, Continue, Pass

my_list = [1,2,3,4,5,6,7,8,9]

for item in my_list:
    # continue
    print(item)

i = 0
while i < len(my_list):
    # pass              --> pass 
    # continue          --> continue to next iteration
    # break             --> jumps out of loop
    print(my_list[i])
    i += 1


# First GUI - Simulation
# Display blank space for 0 and * for 1

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# Solution one
for x in picture:
    to_print = 0
    for y in x:
        if to_print == 0:
            if y == 0:
                to_print = ' '
            elif y == 1:
                to_print = '*'
        else:
            if y == 0:
                to_print += ' '
            elif y == 1:
                to_print += '*'
    print(to_print)

print('\n\n')

# Simplified solution
for image in picture:
    for pixel in image:
        if pixel == 0:
            print(' ',end='')
        elif pixel == 1:
            print('*',end='')
    print('')

# Example for mirror image of above 
for image in picture[::-1]:
    for pixel in image:
        if pixel == 0:
            print(' ',end='')
        elif pixel == 1:
            print('*',end='')
    print('')


# Exercise
# Find and print duplicates in a list
some_list = ['a','b','c','b','d','m','n','n']

duplicate_list = []
for item in some_list:
    new_list = some_list.copy()
    new_list.remove(item)
    if item in new_list:
        if not (item in duplicate_list):
            duplicate_list.append(item)

print(duplicate_list)

# simplified

duplicate_list = []
for item in some_list:
    if some_list.count(item)>1:
        if item not in duplicate_list:
            duplicate_list.append(item)

print(duplicate_list)