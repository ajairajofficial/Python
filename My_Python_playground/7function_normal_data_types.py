import os
os.system ("cls")

########################  Functions for controlling Flow   #############################
# Functions are small or large logical blocks to perform a task.
# we can divide the code into several sets of functions.
#
#                         Functions for normal data types
#
# There are two types of functions
#    1) Performs a Task and returns no value
#    2) Performs a Task and retuns a value
#
# How defining and calling the function?
#
# Note : by default in python all fuctions returns a None value
# **************************************************************************************
#
# Type 1 ******** function with no parameters ***************
# syntax
#                 def function_name():
#                     executing this line retuns nothing
#
#
#                 function_name()
#
# ***************************************************************************
#
# Type 2 ******** function with parameters *****************
# syntax
#
#                def function_name(parameter_1, parameter_2):
#                    executing this line returns nothing
#
#
#                function_name(argument_1,argument_2)
#
#
# Note: argument is the actual value of a parameter.

# Parameters are variables defined in a function's declaration - 
# they are placeholders that receive values when the function is called.
# Arguments are the actual values passed to the function when it's invoked.
# or you can say value passed when calling a function. 
# function design (parameter) and function calling (argument)
# ***************************************************************************
# Type 3 *********** functions returning value *****************
# syntax
#
#                def function_name(paramenter_1,parameter_2):
#                    executing this line
#                    return value
#
#               returned_value = function_name(arguments_1,argument_2)
#
# Note: The value returned from the function is stored in the variable returned_value
# ******************************************************************************
# Special Arguments mentions        (((with Examples)))
# 1) Keyword Argument
# 2) Default Argument
# 3) XARGS  Arbitrary Argumets         *args  (introducing Tuples with this argument)
# 4) XXARGS Arbitrary Keyword Argument **Kwargs  (introducing Dictonary with this argument)
############################################################################

# eg for Type 1          See how function is defined and called
print("eg for Type 1")


def greet():     # defining a function
    print("Hey, how are you")


greet()    # calling the function in the program

############################################################################

# eg for Type 2          See how function with parameters is defined and called
print("eg for Type 2")


def greet_person(first_name, last_name):
    print("Hello {} {}, how you  doing".format(first_name, last_name))

    # calling the function and sending two string arguments
greet_person("Ajai", "Raj")

############################################################################

# eg for Type 3         See how function returns a value
print("eg for Type 2")


def greet_person2(name):
    return(f'hi {name}')   # returns the string


message = greet_person2("Zac") # returning the string is taken into an object,easy
print(message) # printing the object.pretty basic.

############################################################################

# Trying to show  non return function return None value as defaut


def greet_person3(name):
    print("Hi {}".format(name))


# Trying to show that this function returns None value
print(greet_person3("ajai"))  # output None

#############################################################################

#  Keyword Arguments


def divide_number(divident, divisor):
    return (divident/divisor)


print(divide_number(10, divisor=5))

#  here when the function is been called one of the parameter name divisor
#  is shown which is more readable as it is passing. So it is
#  called Keyword argument
#
############################################################################

# Default Argument

# This is showing how to make a paramenter optional


def sub_number(number1, number2=1):
    return number1-number2


# here what happens is since we are passing only 1 parameter
# it takes the other defaulted value and did 7-1 and returned 6
print(f"Just passing only one parameter {sub_number(7)}")

# ---------------------------------------------------------------------------
# same senario but this time passing both parameters


def sub_number_2(number1, number2=1):
    return number1-number2


# here it ignores the defaulted value and subtracted the values
# which are passed 7-2 and returned 5
print(f"Just passing only one parameter {sub_number_2(7,2)}")

# Note: Important note all defaulted parameters should be kept towards
# the last here in this case number2 is kept last

############################################################################

# XARGS (Arbitrary Arguments)   *arg     (packing the value to a tuple)

# If you do not know how many arguments 
# that will be passed into your function, add a * before the parameter 
# name in the function definition.

#This way the function will receive a tuple of arguments, 
# and can access the items accordingly:

def add_number(*number):
    print(number)  # so here all the values are packed in tuples


add_number(1, 2, 3, 4)
# here its not returning any value so only calling the function. 


# another way of representation


def add_number1(*number):
    print(number)   # just printing the packed tuple (5, 6, 7, 8)
    total = 0
    for x in number:         # unpacking tuples
        total = total+x      # adding the values
    print(f"The total is {total}")


# here its unpacked and added to the total
add_number1(5, 6, 7, 8)

###########################################################################

# XXARGS   (Arbitrary Keyword Arguments) **kwargs   (packing key value pair as a dictionary)
# If the number of keyword arguments is unknown, 
# add a double ** before the parameter name: 
# hence the name arbitrary keyword arguments
# This way the function will receive a dictionary of arguments,

def dict_number(**number):  # packing as dictionary
    print(number)           # {'name':'ajai','age':30,'wife':'anu'}
    print(number['name'])   # output -> ajai
# number['name'] is accessing value with a key.


dict_number(name='ajai', age=30, wife='anu') #passing keyword argument

# instead of passing arbitary argument, we have to pass arbitary keyword
# argument. key value pair is passed
# so python packed number object with a dictonary now.

# using for loop and see what happens


def dict_number1(**number):
    for x in number:
        print(x)  # output - name age husband


dict_number1(name='anu', age=29, husband='ajai')


########################################################################
#Return Values
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#########################################################################
#The pass Statement
# function definitions cannot be empty, but if you for some reason have a 
# function definition with no content, put in the pass statement to avoid 
# getting an error.
def myfunction():
  pass

############################################################################
# position only arguments and keyword only arguments

#the difference between position-only and keyword-only arguments in 
#Python with clear examples.

#Position-only arguments must be specified by their position and 
#cannot be passed using keyword syntax. They appear before a / in the 
#function definition.

#Keyword-only arguments must be specified using their keyword name 
#and appear after a * in the function definition.

#Here's a practical example that demonstrates both:
def calculate_price(quantity, /, *, unit_price, discount=0):
    """
    quantity: position-only argument (before /)
    unit_price: keyword-only argument (after *)
    discount: optional keyword-only argument (after *)
    """
    subtotal = quantity * unit_price
    final_price = subtotal * (1 - discount)
    return final_price

# Valid calls:
result1 = calculate_price(5, unit_price=10)  # quantity by position, unit_price by keyword
result2 = calculate_price(3, unit_price=15, discount=0.1)  # with optional discount

# These would raise errors:
# calculate_price(quantity=5, unit_price=10)  # Error: quantity cannot use keyword
# calculate_price(5, 10)  # Error: unit_price must use keyword

#quantity is position-only (before /): must be passed by position
#unit_price and discount are keyword-only (after *): must be passed by keyword
#This design is useful when:

#You want to enforce a specific calling convention
#Parameter names might change in the future (position-only)
#Parameter order is less important than their meaning (keyword-only)
#You want to make the function call more explicit and self-documenting
def format_name(first, last, /, *, title="", suffix=""):
    """
    first, last: position-only arguments for first and last name
    title: keyword-only argument for prefix (Mr., Dr., etc)
    suffix: keyword-only argument for suffix (Jr., PhD, etc)
    """
    name_parts = []
    
    if title:
        name_parts.append(title)
    
    name_parts.extend([first, last])
    
    if suffix:
        name_parts.append(suffix)
        
    return " ".join(name_parts)

# Valid uses:
formatted1 = format_name("John", "Smith", title="Mr.")
formatted2 = format_name("Jane", "Doe", title="Dr.", suffix="PhD")

# These would raise errors:
# format_name(first="John", last="Smith", title="Mr.")  # Error: first/last must be positional
# format_name("John", "Smith", "Mr.")  # Error: title must use keyword

#This example is particularly useful because:

#First and last names are fundamental and ordered (position-only)
#Title and suffix are optional modifiers (keyword-only)
#Makes the code more readable when calling with optional parameters
#Clearly separates required name components from optional formatting elements
#The function enforces a clean and consistent way to format names while making 
# the optional parameters explicit through keyword usage.
############################################################################
# Explicit optional paramenters

# The keyword-only arguments are optional, but if you want to make them
# required, you can set a default value of None and then check for that value
# When we say "explicit" with optional parameters, it means the code clearly 
# shows what each value represents when calling the function. 
# It makes the code self-documenting and easier to understand.


def create_user(username, email, /, *, age=None, country=None, is_active=True):
    """
    username, email: position-only required arguments
    age, country, is_active: keyword-only optional arguments
    """
    user = {
        "username": username,
        "email": email,
        "age": age,
        "country": country,
        "is_active": is_active
    }
    return user

# Explicit - Very clear what each value means
user1 = create_user("john_doe", "john@email.com", 
                    age=25, 
                    country="USA", 
                    is_active=True)

# Also explicit - We can see which optional parameters we're skipping
user2 = create_user("jane_doe", "jane@email.com", 
                    country="Canada")  # age will be None, is_active will be True

# This would NOT be explicit and would raise an error
# create_user("john_doe", "john@email.com", 25, "USA", True)  # Unclear what these values mean


###########  Passing arguments in function ###########################
# Access specific character in the string use array[]
name = "Ajai Rajp" # name is an object carrying string.Can be used as an array.
print("length of the name object ", len(name))  # len(arguments)
# Note: argument is the actual value of a parameter
# len is also an internal function carrying that object name as argument. 




#############################################################################
#               important things to remember
#         
#What is an Expression?
#Expression is a piece of code that produces a value eg c = a+b
#
#What are Function Parameters?
#Each function parameter has a type followed by an identifier, 
#and each parameter is separated from the next parameter by a comma.
#The parameters pass arguments to the function. When a program calls a function,
#all the parameters are variables. The value of each of the resulting arguments is 
#copied into its matching parameter in a process call pass by value. 
#The program uses parameters and returned values to create functions that take data 
#as input, make a calculation with it and return the value to the caller.

#The Difference Between Functions and Arguments
#The terms parameter and argument are sometimes used interchangeably. 
#However, parameter refers to the type and identifier, 
#and arguments are the values passed to the function. 
#In the following C++ example, int a and int b are parameters, 
#while 5 and 3 are the arguments passed to the function.

#eg in c++




#######################################################################################

###              Difference between a function and a method??

#######################################################################################

#  Functions are standalone, while methods are attached to a class.

#  Functions can be called directly, methods need an object instance.

#  Methods can access class/instance data, functions can't.

#  The first parameter of methods is always the instance (self),
#  functions don't have a fixed first parameter.

#For example:

# Function 
def add(x, y):
    return x + y

print(add(2, 3))



# Method
class Point:
    def __init__(self, x=0, y=0): # intialise x and y attributes in the init construct
        self.x = x 
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

p = Point() # now when the point object p is created it will have x and y attributes 
#             that can be accessed and modified using methods like move()
p.move(2, 3) 

#   In summary:

#      Functions are standalone, defined independently.
#      Methods are defined inside a class, attached to a class.
#      Functions are called directly with parameters.
#      Methods are called on an object instance using dot syntax.
#      Methods can access the object's attributes using self.
#      The self parameter is implicitly passed to methods.
#      So while they are similar, functions and methods have different scopes,
#      calling conventions, and access to data.


########################################################################

# some practice sections 


##################################################
number = "ajai"

for x in number:
    print (x)
#################################
def add_number(*number):  #packing value to a tuple
    print(number)  # (5,6,7,8)
    total = 0
    for x in number:
       print (x)    
       total += x
    return total


total = add_number(5,6,7,8)  
print (total)  # 26
#######################################
def dict_number(**number):
    total = 0
    for key in number:
        print (key)   # only print name, age and wife
        

dict_number(name= "ajai", age=40, wife="anu")

##############################################

def dict_number1(**kwargs):
    for key,value in kwargs.items(): # can create both key value when accessed items in dict kwargs
        print(key,value)

dict_number1(name="john",age=30,city="London")

##############################################

class Point:
    def __init__(self,x= 0,y=0):
        self.x = x
        self.y = y
    def move(self, dx,dy):
        self.x +=dx
        self.y +=dy

p = Point(1,2)

print(p.x,p.y) # 1 2 
p.move(3,4)
print(p.x,p.y) # 4 6 


################################################################################
#################################################################################
# recursion
print("Recursion example")
#Python also accepts function recursion, which means a defined function can call itself.

#Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
def find_files_by_extension(directory_path, extension, files_found=None):
    import os
    
    if files_found is None:
        files_found = []
    
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        
        if os.path.isfile(full_path) and item.endswith(extension):
            files_found.append(full_path)
        elif os.path.isdir(full_path):
            find_files_by_extension(full_path, extension, files_found)
            
    return files_found

# Get the files and print them
python_files = find_files_by_extension(r"C:\Users\ajair\Desktop\Python", ".py")

# Print each file found with a nice format
print("\nPython files found in your directory:")
print("-" * 40)
for index, file in enumerate(python_files, 1):
    print(f"{index}. {file}")
print("-" * 40)
print(f"Total files found: {len(python_files)}")

## detailed explanation of the code
# Lets break down the recursive part of this program step by step with a clear example!

# Imagine you have this folder structure:

# Python_Projects/
#     ├── main.py
#     ├── utils/
#     │   ├── helper.py
#     │   └── config/
#     │       └── settings.py
#     └── tests/
#         └── test.py

# here is how the recurssion works:
# 1.First Call:
# find_files_by_extension("Python_Projects", ".py")
# Finds: main.py
# Sees utils folder -> Makes recursive call
# Sees tests folder -> Makes recursive call

# 2.Recurssive call for config:
# find_files_by_extension("Python_Projects/utils", ".py")
# Finds: helper.py
# Sees config folder -> Makes recursive call

# 3.Recurssive call for config:
# find_files_by_extension("Python_Projects/utils/config", ".py")
# Finds: settings.py
# No more folders -> Returns back to utils

# 4.Recurssive call for tests:
# find_files_by_extension("Python_Projects/tests", ".py")
# Finds: test.py
# No more folders -> Returns back to utils

# The magic happens because:

# Each call explores one directory level
# When it finds a folder, it "dives deeper" by calling itself
# The files_found list is shared between all recursive calls
# Each call adds its findings to the same list
# When finished, it "bubbles up" back to the previous call

# Final result would be a list containing:
# [
#     'Python_Projects/main.py',
#     'Python_Projects/utils/helper.py',
#     'Python_Projects/utils/config/settings.py',
#     'Python_Projects/tests/test.py'
# ]

# Think of it like exploring a house:

# You enter a room (directory)
# You note down any Python files
# When you see a door (subfolder), you go through it
# You keep doing this until you've explored every room
# Then you walk back out the way you came

# This recursive approach is elegant because it can handle any depth
# of nested folders automatically!

# 1. Function Definition"""
def find_files_by_extension(directory_path, extension, files_found=None):
    # directory_path example: r"C:\Users\Documents"
    # extension example: ".txt"
    # files_found: starts as None, becomes a list

    # 2. Import os module - gives us tools to work with files and directories
    import os

    # 3. Initialize empty list if None
    if files_found is None:
        files_found = []
   
    # 4. os.listdir() lists all files and folders in the directory
    # Example: os.listdir(r"C:\Users\Documents") might return:
    # ["report.txt", "images", "data.csv", "projects"]
    for item in os.listdir(directory_path):
       
        # 5. os.path.join() combines paths correctly for your operating system
        # Example: os.path.join(r"C:\Users\Documents", "report.txt")
        # Result: r"C:\Users\Documents\report.txt"
        full_path = os.path.join(directory_path, item)
       
        # 6. os.path.isfile() checks if path points to a file
        # os.path.isfile(r"C:\Users\Documents\report.txt") returns True
        # item.endswith() checks if filename ends with given extension
        if os.path.isfile(full_path) and item.endswith(extension):
            files_found.append(full_path)
           
        # 7. os.path.isdir() checks if path points to a directory
        # os.path.isdir(r"C:\Users\Documents\images") returns True
        elif os.path.isdir(full_path):
            find_files_by_extension(full_path, extension, files_found)
   
    return files_found

# Example structure:
# Documents/
#   └── report.txt
#   └── images/
#       └── photo.txt
#   └── data.csv
#
#esult = find_files_by_extension(r"C:\Users\Documents", ".txt")
# First iteration:
# - Finds "report.txt" -> adds to list
# - Sees "images" folder -> explores inside
# - Sees "data.csv" -> ignores (wrong extension)

# Inside "images" folder:
# - Finds "photo.txt" -> adds to list

# Final result would be:
# [r"C:\Users\Documents\report.txt", r"C:\Users\Documents\images\photo.txt"]

# OS Functions Used:

# os.listdir(): Lists contents of a directory
# os.path.join(): Combines paths safely
# os.path.isfile(): Checks if something is a file
# os.path.isdir(): Checks if something is a directory

# These OS functions make it possible to work with files and folders in a way that
# works across different operating systems (Windows, Mac, Linux)!
########################################################################################
