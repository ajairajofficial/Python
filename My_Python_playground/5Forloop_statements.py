##################### Python Statements for controlling Flow #########################

#                         For Loops for normal data types
#
# ************************************************************************************
#
# A simple explanation
#              for loops can be used to iterate over iterable loops
#
# Type 1: for loop
#
#             for variable in (iterable object):
#                          Action
#
# it will loop over the number of times iterable object iterates
#
# Type 2: for loop with break keyword         (for loop with if statement)
# this will break the loop on a boolean expression with an if statement (condition)
#
#             for variable in (iterable object):
#                       executing this line each time object iterates
#                       if (boolean Expression):
#                             execute this line if bool true
#                             break
#                       executing this line each time object iterates
#
# Data types which are iterable - string, built in functions like range, lists,dict,sets etc
#
# Type 3: for loop with continue keyword       (for loop with if statement)
# this will continue the loop but will execute a job on an if condition but will continue iterating
#
#              for variable in (iterable object):
#                       executing this line each time object iterates
#                       if (boolean Expression):
#                             execute this line if bool true
#                             continue
#                       executing this line each time object iterates
#
# Data types which are iterable - string, built in functions like range, lists,dict,sets etc
#
# Type 4: for loop with break keyword and else       (for loop with if statement)
# this will break the loop on if condition, else wont work if loop breaks
#
#              for variable in (iterable object):
#                       executing this line each time object iterates
#                       if (boolean Expression):
#                             execute this line if bool true
#                             break
#              else:
#                   execute this line if iterated through the whole iterable object
#
# Data types which are iterable - string, built in functions like range, lists,dict,sets etc
#
# Type 5: Nested loop                                  (for loop in for loop)
# useful for building arrays
#
#              for variable x in (iterable object):
#                  for varible y in (iterable object):
#                       execute this line y times x inc by one again execute this y times
#
# Data types which are iterable - string, built in functions like range, lists,dict,sets etc
#
# ***** very useful range function for for loop
#
##########################################################
# Lets talk about range function range(5)
##########################################################

"""
The range(5) function in Python creates an iterable sequence of numbers from 0 to 4 (5 numbers total).

The range() function takes a single integer argument that specifies the stop value. It will generate
numbers starting from 0, incrementing by 1, and stop before the number passed as the argument.

For example:

range(5) will generate the sequence [0, 1, 2, 3, 4]

The key things to understand about range(5):

It will start at 0 by default.
It will increment each number by 1 by default.
It will generate numbers up to BUT NOT INCLUDING the stop value passed as the argument.
So range(5) gives 5 numbers total, but stops before reaching 5.

This range object can then be used in loops, like:

for i in range(5):
print(i)

Which would print:

0
1
2
3
4

Or other functions like list() to explicitly convert it to a list:

print(list(range(5)))

Outputs: [0, 1, 2, 3, 4]

So in summary, range(5) gives a sequence from 0 to 4, and creates a range object that 
can be used for iteration, looping, or converting to a list as needed.
"""
###        What is special about range and strings in python ?

"""

So in summary, "looping over" or "iterating over" means traversing a collection and 
accessing each element sequentially using a looping construct in Python. This allows us 
to process elements in an orderly and efficient way.
Both range() and strings are iterable objects in Python, meaning they can be looped over.

Some key points:

Works on any sequence type: strings, lists, tuples etc.

Uses for-in syntax usually to loop over the elements.

The loop variable takes the value of next element on each iteration.

We can access/operate on each element inside the loop one by one.

Some key differences:

range() generates numbers sequentially on demand while a string is an immutable sequence of characters that exists in memory.
Range() generates numbers lazily without storing in memory, while
The range() function and strings have some special behaviors and meanings in Python:

range():

range() generates a sequence of numbers lazily - it doesn't create the full list in memory. It just gives you the next number in the sequence when needed. This makes it very efficient for generating large ranges.

range(n) gives numbers from 0 to n-1. It stops before the provided end value.

You can iterate directly over a range() object, like in a for loop.

range() doesn't store all the values in memory - it just computes the next value on demand. So it can represent very large ranges efficiently.

strings:

Strings are immutable in Python. This means the individual characters of a string cannot be changed once the string is created.

Strings have useful methods like .upper(), .lower(), .split(), etc. to manipulate the data.

Strings are iterable, so you can loop over the characters in a string using for c in s:

Strings are sequence types and support indexing/slicing like s[0], s[1:5] etc.

Strings are represented internally as sequences of bytes representing unicode characters.

You can use + to concatenate strings, but it creates a new string in memory. Better to use string formatting or join() in a loop to combine strings more efficiently.

So in summary:

range() doesn't store values, it computes lazily by demand
Strings are immutable sequences, you cannot change individual characters
Both strings and range() can be looped over directly
range() and strings have specialized behaviors and representations in Python





"""

# eg for Type 1         See how different arguments are passing in range function

print("eg for Type 1")

for x in range(5):       # here range function is iterable from 0 to 4
    print(x)             # each time it iterates it will put the value in x variable
                         # so looped 5 times

for x in range(1, 6):    # here range function iterates between 1 to 5
    print(x)             # this range is useful when counting because its not staring from zero


for x in range(1, 11, 2):   # here range function is iterable from 1 to 10 steps of 2
    print(x)                # output will be 1 3 5 7 9


# eg for Type 2          See how the break keyword works with if statement
print("eg for Type 2")

for x in range(8):       # iterates 0-5 @ x=5 exits without printing
    if (x == 5):
        print("I am exiting the loop")
        break
    print(x)

# eg for Type 3          See how the continue keyword works with if statement
print("eg for Type 3")

for x in range(8):       # iterating 0-7 (so looped 8 times)
    if (x == 5):
        print("found 5")
        continue  # continue means continue back to for loop (very imp) it wont execute the rest
    print(x) # this line almost acts like else condition very interesting thats why it wont print x=5 when condition is true
             
number_of_times = 0
for x in "hey how you doing ":    # eg for iterating over a string
    if (x == 'o'):
        number_of_times += 1
        continue
print("number of times character 'o' in the string is ", number_of_times)


# eg for Type 4          See how the break keyword works with if statement & else
print("eg for Type 4")

successful = False      # Try changing this True and false to see how the loop works
for number in range(1, 4):
    print("Attempt", number*'.')
    if successful:
        print("successful")
        break
else:
    print("Tried 3 times and failed")

# eg for Type 5           # (Nested loop) See how the loops iterate over x and y
print("eg for Type 5, Nested loops")

for x in range(5):
    for y in range(4):
        print(f"{x},{y}")

########################################################################
###################     Special functions    ############################

# 1) Arrays
# 2) Enumerate (auto index pack to tuples and unpacking)
# 3) Zip  (need to add more while progressing )

index_count = 0
for letter in "peter":
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

# same concept with using arrays
index_count = 0
word = "mnopq" # actually string saved in an object can be retrived using index 
for letter in word:             # here letter is just a variable like x
    print(word[index_count])
    index_count += 1

# again same concept but different way of doing

word = "rstuv"
for letter in word:
    print(letter)


# special function called enumerate (useful maninly in lists data structure)
word = "wxyz"
for letter in enumerate(word):  # this has created tuples with index
    print(letter)  # can use item instead of variable letter just a word
"""
(0, 'w')        
(1, 'x')
(2, 'y')
(3, 'z')
"""
# Unpacking the above tuples with the enumerate function
word = "abcd"
for index, letter in enumerate(word):
    print(index)
    print(letter)


###########################################################################
#     what is an enumerate function?

# The enumerate() function adds counter/index to an iterable and returns
#    it in a form of enumerate object. This enumerate object can then be
#    used directly in loops or converted into a list of tuples using list
#    () method.
"""   
Let me break it down:

enumerate() takes an iterable object like a list, tuple, string etc. as input.

It returns a special enumerate object.

This enumerate object keeps a counter for the index and produces tuples 
containing the index and value of each item during iteration.

For example:"""

names = ["John", "Mary", "Bob"]

enum_names = enumerate(names)
print (enum_names) # this does not work but prints the defualt string representation
# instead we can unpack the tuples directly in loop
# we can explicitly convert to list to get the index/value pairs like below. 
print(list(enum_names))  # [(0, 'John'), (1, 'Mary'), (2, 'Bob')]

# So enumerate() has added a counter to the iterable and returned an enumerate object.
# We converted it to a list to see the tuples it generates.

"""
We can directly iterate over the enumerate object in a loop to get the 
index/value pairs: 
this is the way to unpackage the tuples directly without converting to a list:
"""
# Unpacking the enumarate object which is a tuples directly in loop
# but cant access the enumarable object. 
for index, name in enumerate(names):
    print(index, name) 


"""
This prints:

0 John
1 Mary
2 Bob

So in summary,

enumerate() adds a counter and returns an enumerate object
This object can be used directly in loops to get index/value pairs
Or converted to a list of tuples using list()
The enumerate object allows you to easily loop while tracking the index positions.
"""
################  for loop for data structure is different ########################
################  practise that as well ############################################
####################################################################################


