#################################################################################

#                           Data structure - LIST   []
import os
os.system("cls")
#storing single piece of data is variable
# sometimes we want to store grouped pieces of data
# data which has connections between each other
# sometimes we want to keep the order of the data, So we need something called data structure
# List is one type of datastructure that can have mixed data type and items seperated by a comma
#################################################################################
##                          Lists are Dynamic arrays.
# Reading is Fast 0(1) constant time 
# Insertion and deletion is slow 0(n) linear time (middle/beginning)
# Insertion and deletion is fast 0(1) constant time (end elemnt no need to shift)
################################################################################

# 1) We can have objects of any type
# 2) [] sequence of objects, ordered so can use index to access
# 3) mutable so you  can modify, combine, edit, add , index
# 4) packing and unpacking
# 5) looping over lists
# 6) adding,removing,finding using inbuilt function
# 7) soritng and some special functions like lambda map filter etc

############################################################################
# A simple explanation

#  alphabets = ['a','b','c','d]
#  list of strings assigned to a variable alphabets
#  list of numbers, boolean or even have List of lists
#  matrix = [[1,2],[3,2]]  list of list
#  ones = [1]* 100  now ones is an list object containing 100 ones

# list () is an * in buit function * which takes any itterable and
# converts to list

#################################################################################
# basic contruction and some useful in buit functions

greet = list("hello Ajai")  # string is an itterable
print(greet)  #['h', 'e', 'l', 'l', 'o', ' ', 'A', 'j', 'a', 'i']
print(len(greet))  # to get the length of the string ans: 10
print(list(range(5)))  # passing another itterable range # [0, 1, 2, 3, 4]
print(f"accessing the first character in greet object using index {greet[0]}") # h

# combining two list

first_name = ['a', 'j', 'a', 'i']
last_name = ['r', 'a', 'j']
combined = first_name + last_name 
print(combined) #['a', 'j', 'a', 'i', 'r', 'a', 'j']

# concatenating a string
first_name = ['a', 'j', 'a', 'i']
combine = "".join(first_name)  # combine the string to word
print(combine)  # ajai

# zip two lists
name = ['Ajai', 'Anu']
age = [30, 29]
for x, y in zip(name, age):  # calling zip and unpacking over iteration
    print(x, y)        # Ajai 30    Anu 29

# two lists to dictionary
name = ['Ajai', 'Anu']
age = [30, 29]
list_dict = dict(zip(name, age))
age = [30, 29]
print(list_dict)    # {'Ajai':30,'Anu':29}


# modify an item in list
last_name = ['r', 'a', 'j']
last_name[2] = 'i'  # raj omdified to rai
print(last_name) # ['r', 'a', 'i']

# using two index to slice a string

item = ['a', 'b', 'c', 'd']
# slicing the string without any effect in the item list
print(item[0:2])  # sliced an item using 2 index ['a', 'b'] # everything upto 2nd index but it will have 2 elements
print(item)      # but the item hasnt modified  ['a' 'b' 'c' 'd']
print(item[0:]) # sliced from 0th index to end ['a', 'b', 'c', 'd']
print(item[:2]) # sliced from beginning to 2nd index ['a', 'b']
print(item[::2])  # print every 2nd item ['a', 'c']
number = list(range(10)) # create a list from 0-9
print(number[::2])  # print even number [0,2,4,6,8]
print(number[::-1])  # print number in reverse [9,8,7,6,5,4,3,2,1,0]

# unpacking list to multiple varibles
numbers = [1, 2, 3]
first, second, third = numbers
# here the number list is unpacked into three varibles seperated by coma
# Important thing is the number of varibles on left side should be
# equal to the number of items in the list otherwise error

# if we care only the first two items
numbers = [1, 2, 3, 4, 5, 6, 7]
first, second, *rest = numbers # unpack first two items and rest in rest
print(rest) # [3, 4, 5, 6, 7]
# except 1,2 everything else is packed to rest
print(first)    # unpacked and stored as an integer # 1
print(type(first)) # <class 'int'>
print(type(rest))  # <class 'list'>
# if you  want to copy only first and last
first, *middle, last = numbers
print(last) # 7

####################################################################

#                      Looping over lists

# 1) simple looping
# 2) using enumerate method (create index and wrap in Tuples)
# 3) unpacking using enumerate method (and index )
# 4) unpacking using enumerate method (same line itself)

####################################################################

letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:  # each time it itterates letter variable have a new item
    print(letter)   # a b c d e
print(type(letter))  # type string, at this point it carry the last 'e'
print(letter)     # 'e'



# zip two lists
# Works on tow or more lists and returns a list of tuples
name = ['Ajai', 'Anu']
age = [30, 29]
for x, y in zip(name, age):  # calling zip and unpacking over iteration
    print(x, y)        # Ajai 30    Anu 29

###############################################################################
# *************** Tuple and enumerate function ***********************
# using enumerate function to create and index and wrap in TUPLE
# it adds counter to an itterable.
# Returns (index ,value)
letters = ['a', 'b', 'c', 'd', 'e']
for letter in enumerate(letters):
    print(letter)  # now each item is a tuple (index,value) # (0,'a') (1,'b') et
print(type(letter))  # type  is tuple

print(list(letter))  # here only the last (4,'e') converted to [4,'e']

print(list(enumerate(letters)))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# unpacking

for letter in enumerate(letters):
    print(letter[0], letter[1])

# unpacking in the for loop line itself
for index, value in enumerate(letters):  # index,value = letter (unpacking)
    print(index, value)

# above each iteration the list object letters wrapped by enumerate function
# inside the function it tries to create an index and the value and
# wrap it into a tuple. so this tuple is unpacking to varible index and
# value in the same line. so index and value takes first and second value
# of tuple

############################################################################

# Adding and Removing items in list using
# 1) append                  @ add at last
# 2) insert                  @ any where
#    extend function          @ add multiple items
# + operator                @ add multiple items (concatenate)
# 3) pop function            @ remove last one or specify with index
# 4) remove function         @ dont know the index
# 5) del function            @ with single or range of index
# 6) clear method            @ clear all objects
# 7) count method            @ to find the number of occurance of an item
# 8) enumerate function      @ helps to get all index

############################################################################

# pushing is like appending or inserting
# append add to the last
# insert add to the specified index
letters = ['a', 'b', 'c', 'd', 'e']
letters.append('f')  # this will add 'f' as the last element. 
print(letters)

# Append only prices using a loop then adding
items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]
ordered_items_prices = []
total = 0
for item in items:
    # only integer value prices are copied to ordered_items_prices
    ordered_items_prices.append(item[1])
for x in ordered_items_prices:
    total = total+x
print('Total ={}'.format(total))
# ****


letters.insert(2, 'b inserted')  # index,item
print(letters) # ['a', 'b', 'b inserted', 'c', 'd', 'e', 'f']

# extend function
letters.extend(['x', 'y', 'z'])  # add multiple items   
print(letters) # ['a', 'b', 'b inserted', 'c', 'd', 'e', 'f', 'x', 'y', 'z']
# + operator
letters = ['a', 'b', 'c', 'd', 'e']
letters = letters + ['x', 'y', 'z']  # concatenate
print(letters) # ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']

# POP
letters.pop()     # if not mentioned last one will be poped
print(letters) # ['a', 'b', 'b inserted', 'c', 'd', 'e']
# pop is used when you know the idex to remove
# use remove when you know the value to remove
# The pop() method automatically returns the value it removes, 
# so you can use it directly in any expression or store it in a variable. 
# This is one of the great features of pop() - you get both the removal and 
# return value in one operation!


letters.pop(2)    # Mentioned with index                 BY LAST INDEX OR ANY INDEX
print(letters) # ['a', 'b', 'c', 'd', 'e']

letters = ['a', 'b', 'c', 'd', 'e']
letters.remove('c')  # it will only remove the first 'c'     BY VALUE
print(letters)  # ['a', 'b', 'd', 'e']

del letters[0]      # delete with index
print(letters)

del letters[0:2]    # delete with a range of index
print(letters)

letters.clear()  # clear all items
# insert and  append are the only methods that can add items to a list
# append insert and remove use the value in the list 

# Finding items/ objects in a list

letters = ['a', 'b', 'c', 'c', 'd', 'e']

print(F"only show the first index of C which is {letters.index('c')} ")  # onlly show the first item

if 'f' in letters:  # if the item is not in list it will error out so check first
    print(f" checking f {letters.index('f')}") # it will not print because f is not in list

if 'c' in letters:
    print(F"only show the first index of C which is {letters.index('c')} ")  # 


# using count function
print(f"using count method {letters.count('c')}")


# iterting with enumerate method to check repeated items
for index, value in enumerate(letters):
    if 'c' in value:
        print(f"index of c in letters list is {index}")
# So here the list are converted to tupil and unpacked in the same line

############################################################################

# Sorting & Special functions
# 1)  .sort          # use in list but not in dictionary
# 2)  sorted()       # use in both list and dictionary
# 3)  sorting  a list of complex numbers  /  .sort  / (eg a list of Tuples)
# 4)  sorting  a list of complex numbers / sorted() / (eg a list of Tuples)
# 5)  lambda function  / .sort /       (sexy way of calling short function)
# 6)  lambda function  / sorted() /    (sexy way fo calling short function)
# 7)  Map function    # apply function to every element isn the list (Functional programming Style)
# 8)  filter function                  (Functional programming Style)
# 9)  list comprehension
# 10) zip function

###########################################################################

# *********************************************************************
# 1) 
# .sort   # use in list but not in dictionary (modifies the original list directly)
#   .sort() returns None modifies the original list directly
# syntax list.sort(key=None, reverse=False)
numbers = [5, 8, 31, 23, 1, 75, 22, 7]

numbers.sort()                           # sorting numbers 
print(numbers)

numbers.sort(reverse=True)              # sorting in reverse order
print(numbers)

# **********************************************************************
# 2)
# sorted (), a sorted function works with any iterable but .sort only works with list
# sorted() returns a new list
# syntax sorted(iterable, key=None, reverse=False)


numbers = [5, 8, 31, 23, 1, 75, 22, 7]
# this do not modify the numbers list
print(sorted(numbers))
print(sorted(numbers, reverse=True))   # sorting in reverse order

# Important note: An object with a dot operator modify
# the object itself.
# but An object wrapped in function returns a modified value
# and it doesnt change an object itself # very interesting
# look at the difference between .sort and sorted()

# **********************************************************************
# 3) .sort 
# sorting a list of complex objects  /.sort /  (list of tuples) [()]

items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]


def sort_items(item):
    return(item[1])


items.sort(key=sort_items)  # passing only reference not function
print(items)

# important it has to be a keyword argument
# When we write items.sort(key=sort_items), we're passing the function 
# itself (its reference/address in memory) rather than calling the function.
#  Notice there are no parentheses () after sort_items.
# Passing function reference
# items.sort(key=sort_items)    # Correct ✓

# Calling function and passing its result
# items.sort(key=sort_items())  # Wrong ✗

#When you use sort_items (without parentheses), you're handing over the entire function to sort()
# The sort() method will then call this function internally for each item when it needs to 
# compare elements

def get_length(text):
    return len(text)

words = ['python', 'java', 'c++']

# Passing function reference
words.sort(key=get_length)
print(words)  # ['c++', 'java', 'python']

# Behind the scenes, sort() uses the function like this:
# get_length('python') -> 6
# get_length('java') -> 4
# get_length('c++') -> 3

# **************************************************************************
# 4)
# sorting a list of complex objects  / sorted() /  (list of tuples) [()]

items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]


def sorted_items(item):
    return(item[1])

print(sorted(items, key=sorted_items))  # passing only reference not function

# The parameter works through a really neat mechanism! When you pass sorted_items as
# the key function to sorted(), Python automatically calls sorted_items for each item in the list.

#Here's what happens step by step:
# Behind the scenes, Python does this:
# For each tuple in items, it calls sorted_items(item)
# sorted_items(('apples', 15)) returns 15
# sorted_items(('oranges', 12)) returns 12
# sorted_items(('pear', 20)) returns 20
# sorted_items(('brocli', 2)) returns 2

# The magic happens because:

# sorted() takes each element from the list one at a time
# It passes that element to your key function (sorted_items)
# Your function receives each tuple as the 'item' parameter
# The returned values (the numbers) are used to determine the order
# This is a great example of Python's "first-class functions" feature, where functions 
# can be passed as arguments to other functions. The sorted() function knows to use your 
# key function on each element, making it a powerful and flexible way to customize sorting behavior.

# *********************************************************************************************
# 5)   LAMBDA FUNCTION


# Lambda function is a small anomymous function that can be defined in a single line
# basic syntax is variable_name = lambda arguments: expression
# variable_name act as a function after declaration

square = lambda x: x * x
print(square(5))

add = lambda x, y: x + y
print(add(5, 10))
#Lambda function can also be used as a parameters for other functions
# eg using Lambda function for the above sorting / .sort /

print("lambda function /.sort /")

items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]
items.sort(key=lambda x: x[1]) # how key function works explained below 
print(items)

mylist = [1, 3, 2, 4, 5]
mylist.sort(key=lambda x: x * 2)
print("LAMBDA SORT LIST", mylist)  #Eg [1,2,3,4,5] its sorts based on squared value but it does not modify the list

# how the key function works in sort?
# When you pass a key function to sort, it acts as a transformation rule 
# that gets applied to each element before the comparison happens. The key function
# essentially creates a "proxy value" that determines the sorting order, while the 
# original elements maintain their data.
# proxy value is the value that is used to sort the elements.A temporary value that 
# is used to sort the elements. it works only this way with the key function.
# ***************************************************************************
# 6)
# using Lambda function for the above sorting / sorted() /
print("lambda function /  sorted() / ")

items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]

print(sorted(items, key=lambda item: item[1]))
print(sorted(items, key=lambda x: x[1], reverse=True))

# in the above step x is the passing parameter x[1] is the value returned
# to the function sorted and it will sort based on price

# **************************************************************************
# 7)    MAP FUNCTION
# why using Map function?  -->    (apply a function on all elements in an iterable)
# syntax  --> map(function, iterables)
# ??? map() function is used to apply a function on all the elements
# in the item of specified iterable and return map object.
print("Map function ")
items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]
# first argument lambda and return value # second iterable
prices = map(lambda x: x[1], items)
print(prices)  # output Map function and memory address

# This map function will iterate over the iterables 'items'
# and it will call the lambda function on each item 'x'
# and return x[1] which are the prices in this case
# map function returns map  object which is iterable.So
# if you want to convert to list
print(list(prices)) #eg [15, 12, 20, 2]

# another better way to write the above code is 
#prices =list(map(lambda x:x[1],items))

#Map function to do sqauare numbers of a list
numbers = [1, 2, 3, 4, 5]  # lists
square = list(map(lambda x: x*x, numbers))
print(square) # eg [1, 4, 9, 16, 25]


# map function with out lambda function and multiple iteration passing 2 arguments


def num_mul(x, y):
    return x*y


numbers = [1, 2, 3, 4, 5]  # lists
numbers2 = (2, 4, 6, 8, 10)  # tuples
multiply = map(num_mul, numbers, numbers2)
print(f"map function with 2 iterable--{list(multiply)}")
# cool above we pass function reference and 2 iterables

# map function with lambda function and multiple iteration
numb1 = [1, 2, 3, 4, 5]  # lists
numb2 = (2, 4, 6, 8, 10)  # tuples
mul = map(lambda x, y: x*y, numb1, numb2)
print(f"map function with lambda  2 iterable--{list(mul)}")


# **************************************************************************
# 8)
# filter function              (to filter data)
# syntax --> filter(function,iterable)
print("filter function ")
items = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]
item_less_than_15 = filter(lambda x: x[1] < 15, items)
print(item_less_than_15)  # output filter object woth memory address
print(list(item_less_than_15)) #eg [(oranges, 12), (brocli, 2)]
# items object has a list of tuples. On each iteration it will take one
# item which in this case here is tuple. So the lambda function
# argument x here is catching the address of that item from iteration and
# pass it on to the function and here we have a comparison boolean operator
# if this boolean expression is True. The item will come out of the filter
# function as a result. and the output is a filter object which is iterable.

# find even number using filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) #eg [2, 4, 6, 8, 10]

# find prime number using filter function
nums = range(1,100)
def is_prime(num):
    for x in range (2,num):
        if num % x == 0:
            return False
    return True # only reaaches this line if the for loop completes with out any break

prime = list(filter(is_prime,nums))
print("prime numbers are", prime)

# Example run for num = 7:

# Try 2: 7 % 2 = 1 (not divisible) (start at 2 divisor)
# Try 3: 7 % 3 = 1 (not divisible) (% is the modulo operator)
# Try 4: 7 % 4 = 3 (not divisible) 
# Try 5: 7 % 5 = 2 (not divisible)
# Try 6: 7 % 6 = 1 (not divisible)
# No factors found, return True - 7 is prime!

# now how the return of True or false returned is gonna work in the filter function

# The filter function works in a really interesting way here:

# filter() applies the is_prime function to each number in nums
# For each number:
# When is_prime returns True: that number is kept
# When is_prime returns False: that number is filtered out
# Example with nums = [1,2,3,4,5]:

# is_prime(1) → False → filtered out
# is_prime(2) → True → kept
# is_prime(3) → True → kept
# is_prime(4) → False → filtered out
# is_prime(5) → True → kept
################# this is very inefficient way to find prime number
## this is the optimsed way of finding prime number
def is_prime(num):
    if num < 2:
        return False
    # Only need to check up to square root of num
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

nums = range(1, 100)
prime = list(filter(is_prime, nums))
print("Prime numbers are(Efficient way):", prime)

# **************************************************************************
# 9)
# reduce function
# multiplying all the elements in a list
# syntax --> reduce(function,iterable)
# reduce function is not built in function in python.
# so we need to import it from functools module
from functools import reduce
numbers =[1,2,3,4,5]
product = reduce(lambda x,y: x*y, numbers)
print(product) # eg 120

# finding the max number in a list
numbers = [1, 2, 3, 4, 5]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # eg 5

#finding the total sum of the fruits in a list
fruits = [('apples', 15), ('oranges', 12), ('pear', 20), ('brocli', 2)]
total_fruits = reduce(lambda x, y: x + y[1], fruits, 0)
print(total_fruits)  # eg 49
# structure of reduce function is reduce(function,iterable,initial value)
# in our case lambda x,y: x+y[1] is the function
# fruits is the iterable and 0 is the initial value of the accumulator x
# x is always the accumulator (starts from 0 better to initialise with 0 and 
# and y is each item from the fruit list (the tuples))
# This is a standard pattern in functional programming where reduce() always passes 
# the accumulated value as the first parameter and the current item as the second parameter
# to your function!
#
#The program calculates the sum of all quantities in the fruits list using reduce().
#Here's the breakdown:

#The fruits list contains tuples where:

#First element is the fruit name (string)
#Second element is the quantity (number)
#The reduce() function iterates through the list with:

#Initial value = 0 (third argument)
#Lambda function: lambda x, y: x + y[1]
#x: accumulator that holds running sum
#y: current tuple from fruits list
#y[1]: accesses second element of tuple (quantity)
#Here's how it executes:

#Start: x = 0
#First iteration: 0 + 15 = 15 (apples)
#Second iteration: 15 + 12 = 27 (oranges)
#Third iteration: 27 + 20 = 47 (pear)
#Final iteration: 47 + 2 = 49 (brocli)

# Another very useful feature is to find the prime number using reduce function:
# we can use the reduce function to find the prime number
# prime number is a number that is divisible by 1 and itself
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    return all(n % i for i in range(2, int(n**0.5) + 1))

def find_primes_up_to(limit):
  """
  Finds all prime numbers up to a given limit using lambda and reduce.

  Args:
    limit: The upper limit for the prime search.

  Returns:
    A list of prime numbers up to the limit.
  """
  if limit < 2:
      return []
  return list(filter(is_prime, range(2, limit + 1)))


# Example usage:
primes = find_primes_up_to(20)
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Using reduce to check if a specific number is prime (less efficient than all()):
number_to_check = 17
is_number_prime = reduce(lambda acc, i: acc and number_to_check % i, range(2, int(number_to_check**0.5) + 1), True)

print(f"Is {number_to_check} prime? {is_number_prime}") # Output: Is 17 prime? True



# ***************************************************************************
# 9)
# list comprehension
# python own function to replace map and filter function
# syntax  variable =[expression for item in items]
# see its wraped in list bracket
items = [('ajai', 30), ('anu', 29), ('nakshathra', 5)]
names = [item[0] for item in items]  # map function using list comprehension
print(names)
# looks more clean and easy
# doing a filter function replacement using list comprehensionn
items = [('ajai', 30), ('anu', 29), ('nakshathra', 5)]
fil = [item for item in items if item[1] < 30]  # filter fun using list com
print(fil)

# filter all the items with alphabet a in their name
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
filtered_fruits = [x for x in fruits if 'a' in x]
print(filtered_fruits)  # ['apple', 'banana', 'cherry']

#syntax is newlist = [expression for item in items if condition == True]
# list comprehension with if else for filter function

# only accepts item that are not "apple":
newlist = [x for x in fruits if x != "apple"] # here if x!="apple" will return True

# list comprehension with range function:
numbers = [x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list comprehension with if else for filter function
numbers = [x for x in range(10) if x < 5]  # [0, 1, 2, 3, 4]

# setting all values of the new list to upper case
newlist = [x.upper() for x in fruits]  # ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY']

# set all values in the new list to "hello"
newlist = ['hello' for x in fruits]  # ['hello', 'hello', 'hello', 'hello', 'hello']

# return orange instead of banana
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
newlist = [x  if x!="banana" else "orange" for x in fruits]
print(newlist)  # ['apple', 'orange', 'cherry', 'orange', 'kiwi', 'mango']

# ****************************************************************************
# 10)
# zip function

# concatenating a string
first_name = ['a', 'j', 'a', 'i']
combine = "".join(first_name)  # combine the string to word
print(combine)  # ajai

# Zip two lists to another list
name = ['Ajai', 'Anu']
age = [30, 29]
zippy = zip(name, age, "something else")  # returns a zip object
# interesting to watch what happened to that string "some..."
print(f'zipping two list to one lists {list(zippy)}')

# zip two lists and unpacking
name = ['Ajai', 'Anu']
age = [30, 29]
for x, y in zip(name, age):  # calling zip and unpacking over iteration
    print(x, y)        # Ajai 30    Anu 29

# two lists to dictionary
name = ['Ajai', 'Anu']
age = [30, 29]
list_dict = dict(zip(name, age))
age = [30, 29]
print(list_dict)    # {'Ajai':30,'Anu':29}


