########################################################################################

#                                 Tuples           (a read only, immutable list)


# A tuple is very useful at places if we dont want to modify a sequence of objects
######################################################################################
# A simple explanation

number = (12, 13)              # a tuple
number = 2, 3                  # another way of representing tuple
print(number)    # (2,3)

# to represent tuple no need to even need paranthesis

# so how do we distinguish between
value = 3                  # int
values = 4,                # Tuple  a comma is important
print(type(value))
print(type(values))
#####################################################################################
#
# 1)   multiply operator               to repeate
# 2)   tuple()                         wrap function to convert to tuple
# 3)   unpacking                       x,y =(1,2)
# 4)   swaping                         no need for a 3rd varible

###################################################################################

# 1) multiply operator
point = (1, 2)
point = point*3
print(point)

# 2) tuple()

numbers = [1, 2, 3, 4]
numbers = tuple(numbers)
print(numbers)

# 3) unpacking a list and tuple


numbers = [12, 3, 5, 4]                    # a list
x, y, *z = numbers
print(z)                                  # z is a list
print(x)                         # x is taking a value 12

numbers = (56, 3, 43, 7)                  # a tuple
x, y, *z = numbers
print(z)                               # z again packs to list from tuple
print(x)


# 4) Swaping                          (differnt way of unpacking a tuple)
x = 10
y = 12
y, x = x, y                    # unpacking as tupils because of coma and swaping

print(f'x = {x}')
print(f'y = {y}')


####################################################################################
