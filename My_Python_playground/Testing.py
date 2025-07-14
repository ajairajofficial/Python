import os
os.system('cls')

""" 
a = 1
b = 2
x = 3
m=None
# print(f"a = {a} , b= {b} ")

# print (type(x))
name =input("hello whats your name ")
age =input("whats your age")
age =int(age)
if (age < 20):
    print(f"hi {name} you are too young")
elif (20 < age < 30):
    print(f"hi {name} you are mid aged")
else:
    print("you are too old ajai")

temp= 20
collect = "we are going" if (temp > 25) else "we arent going"
print (collect)

num = "qweqewe"
for n,m in enumerate(num):
    print(n,m)

count = 0
success = True
for n in range(1,4):
    print ("Attempt" , n* '*')
    if(success):
        print ("success")
        break
else:
    print("failed")
print(f"value of n is {n} and value of success is {success}")

 
index_count = 0
word = "mnopq"
for letter in word:
    print(word[index_count])
    index_count += 1

print(word[2])

word = "wxyz"
for letter in enumerate(word):  # this has created tuples with index
    print(letter)  # can use item instead of variable letter just a word

# Unpacking the above tuples with the enumerate function
word = "abcd"
for index, letter in enumerate(word):
    print(index)
    print(letter) 
 

name = "ajai"
for letter in enumerate (name):
    print (letter)
"""
successful = True     
for number in range(1, 4):
    print("Attempt", number*'.')
    if successful:
        print("successful")
        break
else:
    print("Tried 3 times and failed")
print ("hey")


def fun ():
    a= "hey"
    b= input ("enter your name")
    print (f"{a}I am having fun {b}")
    print("{},I am having fun {}".format (a,b))
    


fun()

def name(name1):
    return(f"hello {name1}")

returned_value = name("Ajai")
print (returned_value)


def divide (divident ,divisor):
    return (f"ans is ={divident/divisor}")

print (divide(divident=10,divisor = 5))


for x in range(1,10):
    print (x)






