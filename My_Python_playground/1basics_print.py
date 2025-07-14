########################   Python Basics  #########################################
#########   Everything in Python is an object  #############################
######## Python is case sensitive language  ################################
####### indentation is a big deal in python to represent the structure of the code ############
########################################################################################
# Take these concepts for granted to build the intution and core concepts of python
########################################################################################
import os       # importing the os module for interacting with the operating system          
os.system('cls')      # command to clear the run terminal wondow
#os is the module name and system is the function name.
#The os.system('cls') call is using one specific function from the os module called system().
#The system() function allows running operating system level commands from within Python. 
#It takes a string command as input and executes that command 
#using the operating system shell like cmd.exe or bash
#os.system('cls') runs the cls command to clear screen using the underlying OS APIs.
#Behind the scenes, the os module interfaces with the underlying 
# operating system APIs to run these system level commands. 
#When os.system() is called, it opens a subprocess that executes the command, 
#waits for it to finish, and then returns the exit status of the process.
#os.system("notepad") opens notepad. 

#########################################################################################################
################################ Variables ############################################################
########################################################################################################
#Variables act as a storage containers that holds the data which is saved for the actions of a function
##########################################################################################################
a = 10  
b = 11
print(dir(a))  # to explore what you can do with an object
#The dir() function in Python returns a list of all attributes and methods available for the object passed as an argument. 
# When you call dir(a), you're asking Python to show you everything you can do with the integer object stored in variable a.
print("a =", a, "b =", b) # inside paranthesis  we can place multiple objects seperated by comas
#here we have string in double quotes and variable 
#lets deep dive into what happens in the code a = 10

#####################################################################################################
""" three things happened in a = 10
1) object Creation -> 10 is an integer object of class int
                      Every number in python is an instance of its respective class
                      The integer object 10 has both data (value 10 and methods )
2) Variable reference -> 'a' is a reference (or name) that points to the integer object 
                          The variable 'a' stores the memory address where the integerobject live  ### printt(id(a))
3) Assignment Operations -> '=' is the assignement operator 
                            it creates a binding between 'a' and integer object
                             creates int object first and binds a to it

                             
This can be verified by running the following code:  


print(id(a))                        # shows the memory address of the object         # proves variable reference
print(type(a))                      # shows: ,<class 'int'>                          # proves object creation
print(isinstance(a,int))            # shows: True

Since 'a' is refrenced as integer object, it has access to all integer methods.

print(a.bit_length())             # shows: 32 (binary representation of 10)
print(a.to_bytes(4, 'big'))        # shows: b'\x00\x00\x00\n' (10 in 4 bytes)
print(a.conjugate())              # shows: 10 (conjugate of a complex number)
 """
##########################################################################
# python is a dynamic typed language
x = 1          # x is an integer
x = "hello"    # x can be changed to string
x = 1.5        # x can become float
# meaning variable can change data types on the fly (runtime). No need to declare variables explicitly.

# Python is Dynamic Memory Management: (automaic Garbage Collection)
# Python uses a garbage collector to automatically manage memory.
# Can manually triggered using gc.collect()
# threshold based collection for different generations. 
#when an object count drops to zero, it is eligible for garbage collection.
# memory is allocated to objects when they are created and deallocated when they are no longer needed
# memory is automatically deallocated when the object is no longer referenced.
x = 10  # Creates object with reference count 1
y = x   # Reference count becomes 2
del x   # Reference count becomes 1
del y   # Reference count becomes 0, object can be collected.


#######################################################################
# String Manipulation
print("first line\nsecond line") # \n is used to print the next line (backlash n)
name = "Bob " #now name is an object of string class.
greet = "Hello "
print(greet + name)  # concatinate a string (can't concatinate string with integer)
print(name.upper())  # its not actually changing the content of name object  #BOB
#inorder to change it permenantly we need to assign it to a variable.
# upper() - METHOD                method means a function of an object
# name  - OBJECT
# name.upper() - METHOD CALL    method call is used to call the method of the object

#################################################################################
#########    python Input function    ###########################################
name =input("Enter your name: ")  # input function takes input from user and stores it in name variable
print("Hello", name)
# or simply write 
print("Hello", input("Enter your name: "))
#################################################################################



#################################################################################
############################### Theory behind OBJECT and CLASS ##################
#################################################################################
"""
Object: (data + behavior)

An object in Python is an instance of a class. Object is a basic building block of Python code 
that encapsulates data (attributes) and behaviors (methods).
Simply Objects = Data(attributes) + behavior(functions/methods)

For example, a string like "Hello" is an object of the str class. 
An integer like 5 is an object of the int class.   

Objects contain data (the string itself, the integer value) 
as well as methods that can operate on that data.  
Simply Objects = Data(attributes) + behavior(functions/methods)

Method:

A method is a function that belongs to a class. 
It is a behavior or action that an object can perform.

Methods are called by appending the method name to the object name using dot notation. 
For example: object.method()

Methods have access to the internal data (attributes) of the object they belong to.
eg: "Hello".upper() calls the upper() method on the "Hello" string object to convert it to uppercase.

Methods are defined in the class but called on the objects created from that class.

So in summary:
Objects (data + behavior)
Methods (functions belonging to objects)
Classes (blueprints for objects)
Attributes (object properties)

Objects encapsulate data and behavior
Methods are behaviors that operate on an object's internal data
We call methods on an object using dot notation to invoke the behaviors
This allows different objects of the same class to have the same methods 
that operate on each object's unique data.

Class:

A class is a blueprint or template for creating objects. 
It defines the attributes (data) and behaviors (methods) that an object 
created from that class will have.

Classes provide a way to logically group data and functions 
that operate on that data within one unit.

For example, the str class contains the data attributes and methods needed
for working with strings.

Classes define the properties and behaviors of an object, but they don't actually
contain any real data themselves.

Objects are created (instantiated) from classes, and each object contains its own set of
real data values then.

The class defines what attributes and methods the object will have, but the actual 
values are set and stored at the object level.

For example, we can create multiple string objects from the str class. Each string object will
have methods like upper(), lower() etc. but will contain its own unique text data.

So in summary:

Classes are templates that define attributes and methods common to all objects of that class.
Objects are instances created from classes that contain real data values and have access to the class's methods.
Classes allow logical grouping of data and behavior so they can be reused easily.
We instantiate ( means create) objects from classes that then contain their own data values.

Difference between real data and attributes:
Attributes are variables that belong to a class or object. 
They describe the characteristics or properties of that class/object. For example:

class Person:
  def __init__(self, name, age):
    self.name = name   # name attribute john is assigned to p1.name and sarah is assigned to p2.name
    self.age = age     # age attribute

Here name and age are attributes of the Person class.

Real data refers to the actual values assigned to those attributes when an object is created 
from the class. For example: john,30 sarah,25 are data 

p1 = Person("John", 30)  
p2 = Person("Sarah", 25)

p1 and p2 are Person objects containing real data:

p1 has real data values: name = "John", age = 30
p2 has real data values: name = "Sarah", age = 25
So in summary:

Attributes describe characteristics of a class and are defined at the class level
When objects are created from the class, real data values are assigned to those attributes
The objects contain the real data values, the class just defines what attributes an object 
will have 

The class attributes are like a template, and the objects fill in that template with real data.

In the Person class example: [ EXAMPLE 1 ]

p1 is an object of the Person class
name and age are attributes defined in the Person class
When we do:p1 = Person("John", 30)

This creates a Person object p1, and passes the values "John" and 30 to initialize 
the name and age attributes respectively.

Then when we do:p1.name = "Peter"

This changes the value of the name attribute on object p1 to "Peter".

look at this case of object which is name of string class and upper() method [ EXAMPLE 2 ]
name1 = "Zephyr Quirkington"                    # name1 is the object of the string class
print(name1.upper())
Here name1 is the object of the string class and upper() is the method of the string class. #ZEPHYR QUIRKINGTON

(class & object example 1) vs (object and method example 2)
Try to understand the syntax of how a person class is defined and the attribute name and age
is passed to the p1 objects. This changes the value of the name attribute on object p1 to "Peter".
and how the above example is working.

So in summary:

String objects like "name1" have methods defined in the str class like upper()     #ZEPHYR QUIRKINGTON
Person objects like p1 have attributes defined in the Person class like name and age  #John,30
We can access and modify the attribute values on a Person object like p1.name          #Peter   # Later we changed the name of the person

The key difference is that str methods like upper() are behaviors that act on the string data.
While Person attributes like name are just data values stored on the object.

so methods are behaviours that act on the data.

 """
#################################### Python data types #################################################
"""
Text type : str
Numeric types : int, float, complex
Sequence types : list, tuple, range
Mapping type : dict
Set types : set, frozenset
Boolean type : bool
Binary types : bytes, bytearray, memoryview
None Type : NoneType

"""
########################################################################################################
"""
Text Type
 str: Represents text as a sequence of Unicode characters
Numeric Types
 int: Represents integers (whole numbers)
 float: Represents floating-point numbers (decimal numbers)
 complex: Represents complex numbers (numbers with real and imaginary parts)
Sequence Types
 list: Ordered, mutable collection of items            (changeable)
 tuple: Ordered, immutable collection of items         (unchangeable)
 range: Represents an immutable sequence of numbers    (unchangeable)
Mapping Type
 dict: Key-value pairs, unordered (though as of Python 3.7+, insertion order is preserved)
Set Types
 set: Unordered collection of unique items, mutable            (changeable) (unique) (Unordered)
 frozenset: Unordered collection of unique items, immutable  (unchangeable) (unique) (Unordered)
Boolean Type
 bool: Represents True or False values
Binary Types
 bytes: Immutable sequence of bytes 
 bytearray: Mutable sequence of bytes
 memoryview: Memory view of binary data
None Type
 NoneType: The type of the None object, which represents the absence of a value

"""
###########################################################################################################


####################          Strings     (Primitive Data Types : 1/4)  #########################
# Strings are immutable in python (cant be modified after creation)
name = "Glitterdust" # Always write a string in double quotes
# eg name[0] ="B"  # this is not possible because strings are immutable
# when you modify an immutable object you actually create a new object like this
new_name =name[0].upper() + name[1:] #First character upper case and print the rest of the string eg: #Glitterdust
# this method of creating a new string is called string interpolation and the method of pulling out character is called 
# subscripting.
first_name ='albert'
last_name = 'einstein'
full_name = first_name + " " + last_name #string concatenation (combining strings)
print(full_name)

print("Hello"[-1]) # prints the last character of the string eg: o
print("123") # Now this is treated as string.
print("new_name is", new_name)
print(name.lower())  # used lower method with object name
print(name) # simply put    print (object)
course_name = "python programming"
print(course_name.title())  # just to get the title caps
print(course_name.find("pri"))  # return -1 because there is nothing like that
print(course_name.find("pro"))  # shall return the index of the string
print(course_name.replace("p", "j"))  # replaced p with j in the string
print("pro" in course_name)  # return a boolean value in this case True
print("swift" not in course_name)  # return a boolean value in this case True

""" Now what is the difference between method and function in python 
name = "Ajai"
print(len(name))  # this is a function
print(name.upper())  # this is a method

So len()is a built-in function that works on multiple types (int, float, str, etc.)
and return their length. Its a part if the Python built in namespace not attached to any specific object.
On the other hand, upper() is a method that is defined in the str class.

Now you know the diffence between len() and .upper() and why it is called as len(name) and name.upper()

 """

####################          Numbers  (data types)     #########################
x = 1  # int      class   (whole number- Number without any decimal place)
y = 1.1  # float    class
z = 1+2j  # complex  class
t = -1  # int
print(int("123")) #This is called type converstions or type casting meaning that we are converting a string to an integer

print("type of x = ", type(x), "  type of y =",
      type(y), "  type of z =", type(z))
print("type of t =", type(t))

###################  standard Arithmetic Operators       #############

print("7 + 3 =", 7 + 3)         # Add
print("7 - 3 =", 7 - 3)         # Substract
print("7 * 3 =", 7 * 3)         # Multiply
print("7 / 3 =", 7 / 3)         # Divide  (returning a float)
print("7 // 3 =", 7 // 3)       # just the quotion
print("7 % 3 =", 7 % 3)         # remainder
print("7 ** 3 =", 7 ** 3)       # Exponent

# *******************   Augmented Argument operator *********************

c = 1
c += 2                   # c = c+ 2
print("c = ", c)

#########################################################################
# *******************   fstring  ********************* print(f"{}")
# is used when we concatenate string and integer we get a type error
# F string can be used to mix differnt data types
score = 10
height = 1.8
is_winning = True
print(f"your score is {score}, your height is {height}, you are winning is {is_winning}")

# just remember f string -> f and then string it and put the variable name in curly braces

###############################################################################################################
################################################################################################################
#######                     some important concepts to build a strong foundation in python  ###################
###############################################################################################################
"""
###############################################################################################################

Python Standard Library vs. Built-in Namespace: A Comprehensive Explanation
Introduction
Python's ecosystem is structured in layers that provide different levels of accessibility and functionality. 
Two fundamental components of this ecosystem are the Python Standard Library and the Built-in Namespace. 
Understanding the distinction between these two is crucial for effective Python programming.

Python Standard Library
Definition and Purpose
The Python Standard Library is a comprehensive collection of modules and packages that comes bundled with Python. 
It serves as a "batteries included" toolkit, providing pre-written code for a vast array of common programming tasks.

Key Characteristics
Modular Structure: Organized into separate modules, each focused on specific functionality
Requires Explicit Importing: You must use import statements to access functionality
Extensive Coverage: Handles everything from file operations to network protocols
Cross-Platform: Works consistently across different operating systems
Real-World Analogy
Think of the Standard Library as a well-organized toolbox. Each drawer (module) contains specialized tools (functions and classes) for specific jobs.
You need to open a specific drawer to access the tools inside.

providing a wide range of functionalities like file I/O, mathematical operations, data handling, 
internet protocols, and more.

Examples: Modules like os, sys, math, random, datetime, json, etc., are part of the standard library.

Usage: To use functionalities from the standard library, you typically need to import the relevant module. 
For example:

import math
print(math.sqrt(16))  # Output: 4.0
Scope: The standard library encompasses many modules, making it a vast resource for various tasks.

# File operations
import os
print(os.getcwd())  # Get current working directory

# Date and time handling
import datetime
print(datetime.datetime.now())  # Current date and time

# Random number generation
import random
print(random.randint(1, 10))  # Random integer between 1 and 10

# JSON processing
import json
data = json.dumps({"name": "Python"})  # Convert dict to JSON string

###################################################################################################################################
Built-in Namespace
The Built-in Namespace contains functions, types, and exceptions that are always available in Python without requiring any imports. 
These are the core tools that Python makes immediately accessible in any script or module.

Key Characteristics
Always Available: No import statements needed
Core Functionality: Provides the most fundamental operations
Implemented in the builtins Module: Though you rarely need to reference this directly
Limited in Scope: Contains only the most essential tools
Real-World Analogy
The Built-in Namespace is like the tools you always carry in your pockets - immediately accessible without having to open any toolbox.

Common Examples

# Basic I/O
print("Hello, World!")  # Output to console

# Data structure operations
my_list = [1, 2, 3]
print(len(my_list))  # Get length of list

# Type conversion
number_str = "42"
number_int = int(number_str)  # Convert string to integer

# Error handling
try:
    1/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
###################################################################################################################################

The Relationship: Deeper Understanding
The relationship between these two components is hierarchical and interconnected:

Containment Relationship: The Built-in Namespace is technically part of the Standard Library, specifically through the builtins module.

Accessibility Gradient:

Built-ins: Immediately accessible
Standard Library: Accessible after import
Third-party packages: Accessible after installation and import

Implementation Detail: You can actually access built-ins through explicit import, though this is rarely necessary:

import builtins
print(builtins.len([1, 2, 3]))  # Same as len([1, 2, 3])

Historical Evolution: The distinction between what's built-in versus what requires import has evolved over Python's history, with some functionality moving between these categories.

Practical Implications
Understanding this distinction has practical implications for Python developers:

Code Readability: Using built-ins directly makes code cleaner, while Standard Library imports clearly show dependencies
Performance Considerations: Built-ins are slightly faster to access than imported functions
Namespace Pollution: Built-ins are always in your namespace, so be careful not to override them
Documentation Navigation: Knowing this distinction helps you find the right documentation faster

Conclusion
The Python Standard Library and Built-in Namespace represent different layers of Python's "batteries included" philosophy:

Built-in Namespace: The essential, always-available core of Python
Standard Library: The extended toolkit that requires explicit imports

Together, they provide a rich ecosystem that makes Python powerful and versatile while maintaining a clean, uncluttered default environment.
This balance between immediate accessibility and organized modularity is one of Python's greatest strengths as a programming language.

"""
##################################################################################################################
###########################         Public variables in string module    #########################################

#The string module in Python provides several useful public variables. Here's how to use them:

import string

# Using string module's public variables
print(string.ascii_letters)    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print(string.hexdigits)       # 0123456789abcdefABCDEF
print(string.octdigits)       # 01234567
print(string.punctuation)     # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)      # space, tab, newline, return, formfeed, vertical tab

# Practical example - check if a string contains only letters
test_string = "HelloWorld"
if all(char in string.ascii_letters for char in test_string):
    print("String contains only letters")

# Create a string with letters and digits
valid_chars = string.ascii_letters + string.digits
print(valid_chars)  # all letters and numbers combined


# These public variables are particularly useful for:

#1)Input validation
#2)Password generation
#3)Text processing
#4)Character set verification
#5)Creating custom string filters

# The string module's constants provide a clean and reliable way to work with specific 
# character sets in Python.

""" 
#########################################################################################
A small introduction to Lists, tuples dictionaries and sets
#########################################################################################
Lists:   items  are ordered, changeable, and allow duplicate values. 
represented in square brackets [].

Lists are ordered collections of items. They can contain items of different types,
and they are mutable, meaning you can change their contents.

#########################################################################################
Tuples: items are ordered, unchangeable, and allow duplicate values.
represented in parentheses ().
Tuples are ordered collections of items. They can contain items of different types,
Tuples are similar to lists but are immutable, meaning their contents cannot be changed
once created.

##########################################################################################
Dictionaries: items are unordered, changeable, and do not allow duplicate values.
represented in curly braces {}.
Dictionaries are unordered collections of key-value pairs. They are mutable,
and each key is associated with a value.

##########################################################################################
Sets: items are unordered, unchangeable, and do not allow duplicate values.
represented in curly braces {}.
Sets are unordered collections of unique items. They are mutable,
and they do not allow duplicate values.

##########################################################################################

Now some of the common operations on these data structures:
##########################################################################################"""
#                                      Lists:
# Creating a list

my_list = [1, 2, 3, 4, 5]
# Accessing elements
print(my_list[0])  # Output: 1 (first element) (getting the first element)
print(my_list[-1]) # Output: 5 (last element) (getting  the last element)

# Looping through a List: 
# Technique 1: Technically its called iterating over a list  
for item in my_list: # Looping through the list and itterating over each item in the list
    print(item)     # benifit is we dont need to know the number of items in the list to iterate over it

# Technique 2:
for i in range(len(my_list)): # Looping through the list and itterating over each item in the list
  print(my_list[i]) # Looping through the list and itterating over each item in the list

# Technique 3:
print ("enumerated")
for i, item in enumerate(my_list): # Looping through the list and itterating over each item in the list
  print(i, item) # this yeiled a tuple of the index and the value of the item
  # enumerate is a built-in function in Python that returns an enumerate object.
  # enumarate(my_list) returns an enumerate object that contains tuples of the index and the value of the item.
  # the for loop then unpacks the tuple into the index and the value of the item.
  #We can see the tuples explicitly by converting the enumarate object to a list.
  # print(list(enumerate(my_list))) # this yeiled a list of tuples

# Technique 4:
print ("enumerate with start parameter")
for i, item in enumerate(my_list, start=1): # Looping through the list and itterating over each item in the list
  print(i, item) # this yeiled a tuple of the index and the value of the item
# Technique 5:
print ("zip")
for i, item in zip(range(len(my_list)), my_list): # Looping through the list and itterating over each item in the list
  print(i, item) # this yeiled a tuple of the index and the value of the item

# Technique 6:

#using enumerate with zip
print ("enumerate with zip")
for i, item in zip(enumerate(my_list), my_list): # Looping through the list and itterating over each item in the list
  print(i, item) # this yeiled a tuple of the index and the value of the item
  # enumerate is a built-in function in Python that returns an enumerate object.

# technique 7:
# using normal range function
print ("range for Loop ")
Square =[]
for i in range (1,11):  # 1 to 10
  Square.append(i**2)
  print(Square)

#technique 8:
# using list comprehension, write expression in a single line. 
print ("list comprehension")
Square = [i**2 for i in range (1,11)]
# slicing a list 
print ("slicing a list")
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3]) # Output: [2, 3] (elements from index 1 to 2)# see it like 3 is pushing it.
print(my_list[:3]) # Output: [1, 2, 3] (elements from index 0 1 and 2)
print(my_list[2:]) # Output: [3, 4, 5] (elements from index 2 to the end) # see here index 2 is included
print(my_list[::2]) # Output: [1, 3, 5] (elements from index 0 to the end, skipping every second element)
print(my_list[::-1]) # Output: [5, 4, 3, 2, 1] (elements from the end to the beginning, reversing the list)



# Modifying elements
my_list[0] = 10  # Changes the first element to 10 using  the index
print(my_list)  # Output: [10, 2, 3, 4, 5]
# Adding elements
my_list.append(6) # Adds 6 to the end of the list (here its not the index but the value)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
# Removing elements
my_list.remove(4) # Removes the first occurrence of 4 from the list (here its not the index but the value)
print(my_list)  # Output: [10, 2, 3, 5, 6]
#
# copying a List
my_list_copy = my_list.copy() # Copies the list
print("My new copied list is" ,my_list_copy)

###########################################################################################
#                                      Tuples:
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
# Accessing elements
print(my_tuple[0])  # Output: 1 (first element)
print(my_tuple[-1]) # Output: 5 (last element)
# Looping through a Tuple:
# Technique 1:
for item in my_tuple: # Looping through the tuple and itterating over each item in the tuple
   print(item)     # benifit is we dont need to know the number of items in the tuple to iterate over it


### some theory on how the garbage collector works in the case of cycclic references
class Node:                    # Defines a new class called Node
    def __init__(self):       # Constructor method _init - called when creating new Node objects
        self.next = None      # Creates an instance variable called 'next' and sets it to None
    # self.next is a reference to the next node in the linked list like a pointer/arrow
#Creating and linking nodes
a = Node()   # create first node # Node is like creating a box. # self is a reference to the current object 
b = Node()  # create second node
# now intial object Creation is finsihed at this point each Node has a reference  count of 1 
# from variable 'a' and 'b' to the Node object
# now we are going to create a cycle
a.next = b  # 'b' is assigned to the 'next' attribute of 'a' #now the reference count of 'b' is 2
b.next = a  # 'a' is assigned to the 'next' attribute of 'b' #now the reference count of 'a' is 2
# Now we have circular structure where 
# 'a' is pointing to 'b' through its next attribute
# 'b' is pointing to 'a' through its next attribute
# memory management challenge
del a  # Reference count of first node becomes 1
del b  # Reference count of second node becomes 1
'''
Even after deleting variables 'a' and 'b':

Each Node still has a reference from the other's 'next' attribute
Reference counting alone can't detect this as garbage
Python's garbage collector specifically looks for these cycles and cleans them up
This is why Python uses both reference counting and cycle detection in its garbage collection
system to handle such circular reference scenarios effectively.

The reference counting works like this:

Each object maintains a count of how many references point to it
When we create Node objects, each gets a count of 1
When we link them, each gets an additional reference (+1)
When we delete variables, each loses one reference (-1)
Both nodes still have mutual references through their .next attributes
This creates a cycle that standard reference counting can't clean up
Python's garbage collector specifically looks for and cleans up these cycles
This is why Python needs both reference counting and cycle detection in its garbage collection system.
'''
##############################################################################################
#Example explaining different types of attributes
class Student:
    school = "Python Academy"  # Class variable (attribute)
    
    def __init__(self):
        self.name = "John"    # Instance variable (attribute)
    
    def study(self):          # Method (attribute)
        return f"{self.name} is studying"
        
    @property                 # Property (attribute)
    def student_info(self):
        return f"{self.name} at {self.school}"

###############################################################################################
