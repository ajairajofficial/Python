##########################################################################################

#                              Arrays                 (mutable)


# Efficient way to handle a large sequence of numbers.
# This datastructure is much faster than lists
# use list instead array, use array  only if we deal with lot of data
# and there is any performance issue.

######################################################################################

# first import                                #from module import class
from array import array

# syntax  array(typecode,[1,2,3])        here the typecode is integer
# get the typecode values details from google

number = array("i", [1, 2, 3])                # "i" is the typecode
print(number)

number.append(7)                              # added at last
print(number)

number.insert(0, 5)                           # inserted 5 at index 0
print(number)

number.pop()                                  # popped the last element
print(number)

number.remove(2)                              # removed int 2
print(number)

######################################################################################
