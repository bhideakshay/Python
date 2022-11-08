# Object Oriented Programming - OOP
# Everything in Python is an object

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Hi'))
print(type([]))
print(type(()))
print(type({}))

# Returns 
# <class 'NoneType'>
# <class 'bool'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>

# We are able to use different methods on that object

# Paradigm - A way to think about code and structuring the code 
# Remember example of drone and tank
# Wikipedia - History of Programming Languages

# Procedural code - from line 1 to 10 - > do this - do that
# Model something in code - eg - Car objects - engine, color(Attributes/ Properties), actions, forward (Methods)

# Creating a class in Python ------------------------------------------------------------------------------------------------->
# Camel Case - every new word starts with capital letter

class BigObject:    # Class
    pass

print(type(BigObject))

obj1 = BigObject()      # Instantiating a class to create object
obj2 = BigObject()      # Second object (Instance)
obj3 = BigObject()      # Third Object (Instance)

print(type(obj1))

# Class (Blueprint of properties and methods)--> Object (We use class to create instance of object/s) [Class instantiation]


# Creating classes in python --------------------------------------------------------------------------------------------------->

class PlayerCharacter:
    # Class object attribute
    membership = True
    
    def __init__(self, name, age=30):  # __init__ --> special method / dunder method --> constructor method
        if (self.membership):
            self.name = name            # Attributes / Properties
            self.age = age              # Attributes / Properties
        
    def run(self):                  # Method
        # print('Run')
        return self.age
    
    def shout(self,greet):
        return f'{greet}, my name is {self.name}'
    
    @classmethod
    def adding_numbers(cls,num1,num2):      # Standard is to use cls
        return cls('Teddy', num1 + num2)    # Creating a class using classmethod

    @staticmethod                           # Static method
    def adding_numbers2(num1,num2):
        return num1 + num2


player1 = PlayerCharacter('John',55)
print(player1.name)
print(player1.run())
print(player1.shout('Hello'))
print(player1.adding_numbers(1,2))

player2 = PlayerCharacter('Tom')
print(player2.name)
print(player2.run())
print(player2.shout('Hi'))

# Adding Property to object
player1.attack = 'Attack'

print(player1.attack)
# print(player2.attack)   # Will throw an error as player2 has no attribute attack


# __init__  Method

# @classmethod vs @staticmethod

# @classmethod - decorator
# We can use this method without instantiating it 

print(PlayerCharacter.adding_numbers(4,5))

player3 = PlayerCharacter.adding_numbers(7,8)
print(player3.age)


# Revision 

class NameOfClass():
    class_attribute = ' Value'
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def method(self):
        # Logic/ Code
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        # Logic / Code
        pass
    
    @staticmethod
    def stc_method(param1, param2):
        # Logic / Code
        pass