
# Expression is a piece of code that produces a value

####################### Type Convertions ###########################

####################################################################
import os
os.system('cls') # to clear the terminal screen
####################################################################
a = "1"  # if we add a srting with an integer we get a type error
a = int(a)
b = 2
c = a+b
print(c) # you can just print objects also seperated by commas
print (a,b,c)
print(" first line \n second line")

# Two things to note here,  1) we cant run input function in this
x = input("x=")
# Need to take bash terminal and run python3 filename.py because this
# is just a read only terminal
# 2) usually  the input takes value from user as string so we need to convert
# it into the specified data type in this case integer

y = int(x)+1  # if not converted it will give you  type error
print(f"x: {x},y: {y}")  # very useful syntax

# lets give a value to varible x as a string and convert it into different types
x = "1"
print("as integer ", int(x), type(int(x)))
print("as float ", float(x), type(bool(x)))
print("as boolean ", bool(x), type(bool(x)))
print("as string ", str(x), type(str(x)))

###########################   Expression #############################
# Expression is a piece of code that produces a value
print("The value of the expression ('*' * 8) =", ("*" * 8))
######################################################################

###########  Passing arguments in function ###########################
# Access specific character in the string use array[]
name = "Ajai Rajp"
print("length of the name object ", len(name))  # len(arguments)
# Arguments are inputs to the function
print(name[0])  # Print first Characters
print(name[-1])  # print the last character
print(name[0:])  # print the whole string
print(name[0:3])  # print the first three characters 012
print(name[:])  # print the full string
first_name = "Ajai"
last_name = "Raj"
full_name = "Ajai" + " " + "Raj"
print(f"hello {first_name},how are you")
# we can put any valid expression inside {}
print(full_name)
print(type(full_name))

########################################################################################
# Randomisation in python
########################################################################################
# Helpful to use a bit of random like in the games eg tetris showing different outcomes
# To create a degree of unpredictability in your code and make it more interesting.
# Python has a built-in module called random that can be used to make random numbers.
# When we normally write a program computers are deterministic like they perform repretable action in predictable way.
# Python use psrudo Random Number Generator (PRNG) to generate random numbers called Mersenne Twister.
# Mersenne Twister is a type of algorithm that generates random numbers.Check in wikipedia for more details
# So all the complxity of the algorithm underlies in the module. We just need to call the function.
import random  # import the random module
print(random.random())  # print a random floating number between 0 and 1 which isnt inclusive of 1
print (random.randint(1,10))  # print a random integer between 1 and 10
print(random.choice([1,2,3,4,5,6,7,8,9,10]))  # print a random number from the list
print(random.choice("Hello World"))  # print a random character from the string
print(random.choice(["Heads", "Tails"]))  # print a random string from the list
numbers = list(range(1,100 +1)) #create a list of numbers from 1 to 100
print(numbers)
winning_number = random.sample(numbers, 5) # print 5 random numbers from the list,you can provide a sample size.
print(winning_number) # print 5 random numbers from the list
#######################################
# Another stupid way of doing the same thing is using if else statement
random_number =random.randint(0,1)
if random_number == 0:
    print("Heads")
else:
    print("Tails")
########################################################### 
#              variables and memory management
###########################################################
# id() - shows the unique memory address of a variable/object
x= 42
print(id(x)) # 140727477121488

# type() # shows the type of the variable/object
print(type(x)) # <class 'int'>

# sys.getsizeof() # shows the size of the variable/object in bytes
import sys
print(sys.getsizeof(x)) # 28
data = [1,2,3,4,5]
print(sys.getsizeof(data)) # 120

#locals() and globals() # shows the local and global variables
x=100
def show_vars():
    y =200
    print(locals())
    print(globals())

show_vars()

#isinstance() # checks if the object is an instance of a class
value = "Hello"
print(isinstance(value, str)) # True
print(isinstance(value, int)) # False

#Key memory concepts:

#Python uses reference counting for memory management
#Variables are labels pointing to objects in memory
#Multiple variables can reference the same object
#Immutable objects create new memory locations when modified
#Mutable objects can be modified in place
#Example showing variable references:

# Example showing variable references
a = [1, 2, 3]
b = a
print(id(a)==id(b)) # True  
b.append(4)
print(id(a)==id(b)) # True

##########################################################################
# mutable & immutable objects  (These are connected to pass by value and pass by object reference) 
# lets see how python handles memory management with mutable and immutable objects

# think like this 
# Modify = Mutable    (M)
# not modify = immutable 

# or think like this

# MUTABLE = WHITEBOARD    (M W) 
# IMMUTABLE = PHOTO    (I P) 

############################################################################################
#################   Mutable Objects  ##############################
#Mutable means an object can be changed after creation. Think of it like a whiteboard -
#  you can write, erase, and modify its contents while keeping the same whiteboard.

#Common mutable types:  (Modify) 

# Arrays (in the array module)
# Byte Arrays
# Custom classes (by default)
# Dictionaries
# Lists
# Sets

################################################################################################
#################   Immutable Objects  ##############################
#Immutable means an object cannot be changed after creation. It's like a printed photograph -
#once developed, you can't modify it. If you want changes, you need to create a new photo.

#Common immutable types:
 
# Bytes
# custom classes (when explicitly designed to be immutable)
# Numbers (int, float)
# Strings
# Tuples
# Frozen sets
##################################################################################################


# The distinction between mutable and immutable objects has significant impacts 
# on Python's memory management:
print("Mutable Objects:")
####################################################################################
#Immutable Objects:
#Create new objects for every modification
#More memory allocations and deallocations
#Better for memory safety as original data can't be accidentally modified
#Great for caching since their state never changes
#Python can optimize memory by reusing common values (like small integers)
#Here's an example showing memory behavior with immutable strings:
# Immutable string operations

text = "hello"
id_before = id(text)
text += " world"  # Creates new string object
id_after = id(text)
print(id_before != id_after)  # True - different objects in memory
print (dir("hello")) # dir() is a built-in function that returns a list of attributes and methods of an object.
#####################################################################################

# Mutable Objects:

#Modify data in-place without creating new objects
#More memory efficient for modifications
#Single memory allocation until object size needs to grow
#References point to same memory location
#Changes affect all references to the object

#Example with mutable list:
# Mutable list operations
list1 = [1, 2, 3]
list2 = list1  # Both reference same memory
id_before = id(list1)
list1.append(4)
id_after = id(list1)
print(id_before == id_after)  # True - same object in memory
print(list2)  # [1, 2, 3, 4] - reflects changes
print(id(list1)) #shows the memory address of the list1
###########################################################################

# See how list and dict can easily append and modify the object without creating a new object
# you dont have to assign it to a new variable
list_example = [1, 2, 3]
list_example.append(4)  # Original list is modified

dict_example = {'a': 1}
dict_example['b'] = 2   # Original dict is modified

# where as an Immutable  objects are assigned it to a new variable
string_example = "hello"
new_string = string_example + " world"  # Creates new string

number = 42
number = number + 1  # Creates new number object

#######################################################################################
# ****************************************************************************
######################## Pass by value and pass by reference ###########################
#######################################################################################
# (it means how the object are passing thorough the functtion)
# See how python handle a mutable object and immutalbe object when passed to function.
# ****************************************************************************

# The secret is when you pass immutable objects to a fuction Pyhton creates 
# a new object for any modification. This is pass by value. I mean the immutable object 
# passed to a function as argument when a function is called. 

# when you pass a mutable object to a function, the object is passed by object reference.

#In Python, the behavior is actually best described as "pass by object reference". 
# Here's how it works:

# Example with immutable objects (integers, strings, tuples)
def modify_number(x):
    x = x + 1    # Creates new object, doesn't modify original
    return x

num = 5
modify_number(num)
print(num)  # Still 5

# Example with mutable objects (lists, dictionaries, sets)
def modify_list(lst):
    lst.append(4)    # Modifies the original list
    return lst

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]
# in the above example, the list is modified in place. This is because lists are mutable.
# When you pass a mutable object to a function, the object is passed by object reference.
# This means that the function receives a reference to the original object.
# If you modify the object through this reference, you're modifying the original object.
# here when the function is called the object my_list is passed as an argumant 
# here if you check the id(lst) and id(my_list) you will see that they are the same.

# what's happening:

# In Pass by Value:
# The actual value is copied
# Changes to the copy don't affect the original
# Languages like C use this by default

# In Pass by Reference:
# A reference to the memory location is passed
# Changes affect the original value
# Common in languages like C++

# Python's Pass by Object Reference:
# Variables are references to objects
# When passing mutable objects, you can modify the original
# When passing immutable objects, you can't modify the original
# Here's another clear example:

# With immutable string
def change_string(s):
    s = s + " World"    # Creates new string object
    return s

text = "Hello"
change_string(text)
print(text)  # Still "Hello"

# With mutable list
def change_list(lst):
    lst[0] = 99    # Modifies original list
    return lst

numbers = [1, 2, 3]
change_list(numbers)
print(numbers)  # [99, 2, 3]
##########################################################################
# the above pass by reference is very closely related to pointers in C
# Yes, absolutely! The concept is very closely related to pointers. 
# In fact, Python's object references work similarly to pointers in languages like C/C++, 
# but with added safety and abstraction.
# In Python
x = [1, 2, 3]  # x holds reference to list object
y = x          # y now points to same list object
y.append(4)    # modifies the object both x and y point to
print(x)       # [1, 2, 3, 4]
print(y)       # [1, 2, 3, 4]

# Equalant concept in C++
# int* x = new int[3]{1, 2, 3};  // x points to array
# int* y = x;                     // y points to same array
# y[3] = 4;                       // modifies where both point to

#Key similarities:

# Both references and pointers store memory addresses
# Multiple references/pointers can point to same data
# Modifying through one reference affects all references
# The main difference is that Python handles memory management automatically 
# and prevents direct memory manipulation, making it safer than raw pointers.
# This pointer-like behavior is what enables Python's efficient handling of data structures
# and function parameters!


