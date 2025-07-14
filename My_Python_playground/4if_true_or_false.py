import os
os.system("cls")

#########################################################################
# This Chapter is about (True or False).How we are controlling a
# Flow using Comparator Operator and If statements and Logical Operators

#################################################################################
#
#
#   Control Flow ---> IF statements + Comparator Operators + Logical Operators 
#                     
#
########################  Boolean   #############################################
# Recognising falsy values
# ""      ---> Empty string is falsy value
# 0       ---> Number 0 is a falsy  value
# None    ---> Object which represents absence of a value again false

print(bool(""))    # Empty string so  it should be false
print(bool(0))     # bool value of 0 is False ##  important to know 
print(bool(None))  # Should be False
print(bool(1))     # should be True
print(bool(5))     # Should be True
print(bool("False"))  # This is funny, as this is a string, True

###################### Control Flow ####################################

#  Comparator Operators
print("Comparator Operator")
# All these comparator Operator give booloean output
print(5 > 2)     # True    (Greater than)
print(5 >= 2)    # True    (means Greater than or equal to)
print(5 < 2)     # False   (Less than)
print(5 <= 2)    # False   (Less than or equal to)
print(5 == 2)    # False   (Equality operator)
print(7 == 7)    # True    (Equality Operator)
print(7 == "7")  # False   (Equating to a string)
print(7 != 7)    # False   (Not equal to Operator)
print(5 != 7)    # True    (Not equal to operator)
print(1 != "1")  # True    (Not equal to operator)

# String Comparison and numeric representation of Strings
print(ord("A"))  # value of A is 65
print(ord("B"))  # value of B is 66
print(ord("a"))  # value of a is 97
print(ord("b"))  # value of b is 98
print(ord("Z"))  # value of Z is 90      (A-65 to Z-90)
print(ord("z"))  # value of z is 122     (a-97 to z-122)
print("Apple" > "Orange")  # False because after sorting Orange is greater

################### IF Statement ##########################
# lets analyse whats happening under the hood
Truth = True
lie = False
if (Truth|lie):
    print("True or false -> the logic is true")  # this is the output
else:
    print("True or false -> the logic is false")
if (not Truth):
    print("not Ture -> the logic is True")
else:
    print("not True -> the logic is false")   # this is the output
if (not lie):
        print("not False -> the logic is True")  # this is the output
else:
        print("not False -> the logic is false")
if(lie and lie):
     print("lie and lie -> the logic is True")
else:
        print("lie and lie -> the logic is false") # this is the output
if(lie or lie):
     print("lie or lie -> the logic is True")
else:
        print("lie or lie -> the logic is false") # this is the output

        
##################### Python Statements for controlling Flow #########################

#                      If elif else, For Loop , While Loop
#
#
# ***************************** IF Statement *****************************************
# 
# A simple explanation. 
# If always combines with boolean expression(true  or false) in the form of logical 
# operators(and,or,not) or comparison operators (<,>,=) to create complex boolean
# expressions.(true or false equations).So if statement is helpful in controlling the 
# flow. 
# 
# *************************************************************************************
# Intendation is king here. See the below examples.
#   
#  Type 1 :Single Condition  if()
#
#            if (boolean expression):
#                I am True so executing the action here,I wont execute if condition is False
#            I will execute anything
# 
#  Type 2 :Multiple if
#            if (boolean expression):
#                Do A
#            if (boolean expression):
#                Do B
#            if (boolean expression):
#                Do C
#       
#
#  Type 3 :Single Condition  if else
#
#             if (boolean expression):
#                Im True so Execute otherwise No. Checking the next if condition
#             else:
#                 (above bool expressions is false I will execute this section)
#
#  Type 4 :Multiple Conditon  if elif elif else
#           This is used to check multiple conditions on a single variable and 
#           do certain actions based on the conditions (boolean expression)
# Different conditions of the same variable like age.

# eg , if age is less than 18, print "you are a minor"
#      elif age is less than 65, print "you are an adult"
# remember if, elif,else are all intended in the same line.

#            if(boolean expression):
#                Im True so Execute otherwise No. Checking the next if condition
#            elif(another boolean expression): 
#                this condition is true, I will execute this section
#            elif(another boolean expression):
#                this condition is true, I will execute this section
#            else:
#                 (both  bool expressions are false I will execute this section)
#
# Can use comparison operators or Logical Operators or chain both of them to
# make a boolean expression

#   Type 5:Nested if statement (if inside if)
#       The first condition looks at the larger picture. Then put a nested if statement
#       inside the first if statement.

#            if (boolean expression):
#                  Im True so Execute otherwise No. Checking the next if condition
#                  if (boolean expression):
#                    Im True so Execute otherwise No.
#                  else:
#                    (above bool expressions is false I will execute this section)
#            else:
#                 (above bool expressions is false I will execute this section)

#
# ************************************************************************************

# Examples 1 Control Flow using if elif else using Comparison Operators (< = >)

# Notice the indentation, if elif and alse are all intended in the same line.

temperature = 25  # This is the current temp, change this value to see the output changing
if temperature > 30:
    print("Its very hot. Current value is ", temperature)
elif(25 <= temperature <= 30):
    print("its moderate temperature.Current value is ", temperature)
else:
    print("Its cold. Current value is ", temperature)

# ************************************************************************************
# Example of Nested If and elif statement
# QU
# inorder to ride a roller coaster you need to be 120cm tall
# and differnt price range for differnt age groups
# under 12 is $5
# 12-18 is $7
# 18+ is $12
# Ans:
# The first condition looks at the larger picture, here in this case height.
# Then put a nested if  elif statement for age. This is the idea.

print("Welcome to the Roller Coaster")
bill = 0
height = int(input("what is your height in cm?"))
if height >=120:
    print("you can ride the roller coster")
    age = int(input("what is your age?"))
    if age <12:
        bill = 5
        print("please pay $5")
    elif 12<=age<= 18:
        bill = 7
        print("please pay $7")
    else:
        bill =12
        print("the adult price is $12")
else:
    print("sorry you have to grow taller before you can ride")


 ##########################################################################################
 # Use the power of Nested if, if elif, and multiple if 
 #Question:
 # First condition check the Height >120 can ride. <120 cant ride.
 # Age <12 $5, <=18 $7, >18 $12
 # Are you insterested in a picture taken : Yes + $3 to the current bill , No just print the bill
 # Ans:
 # The first condition looks at the larger picture, here in this case height.
 # then age is nested in the height condition. Differnt conditions of age only needs 
 # one variable with multiple conditions so use if elif.
 # then another if conditio to check if the user wants a picture or not.The picture if 
 # is indented to the same level of the age condition. that would be considered as multiple if.
 #           
print("welcome to the roller coaster & photo booth")
bill =0
height = int(input("What is yourheight in cm?\n"))
if height >=120:
    print("you can ride the roller coaster")
    age =int(input("What is your age?\n"))
    if age <12:
        bill =5
        print("Child tickets are $5")
    elif age <=18:
        bill =7
        print("Youth tickets are $7")
    else:
        bill =12
        print("Adult tickets are $12")
    want_photo = input("Do you want a photo taken? Y or N.\n")
    if (want_photo == "Y")| (want_photo == "y"):
        bill +=3
        print(f"your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride")


""" here age is nested inside height, Age variable has differnt conditions
at particular age so we do if  elif , Photo is asked for all people who is qualified
to ride so intended at the same level of age and being multiple if. Meaning one of the 
if in the age is executed and the photo if is executed so itended in the same level
becase it is multiple if photo condition should  also  be checked. """

# example 
# Pizza delivery program
# Based on the size of the pizza work out the final bill
# Small Pizza: $15 , Medium Pizza: $20 , Large Pizza: $25
# Pepperoni for Small Pizza: +$2 , Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Ans:
# here size has if,elif. peporoni has if elif but nested inside size
# cheese has if and elif but multiple ifs with size. Why intended with size if becuase 
# its the same price for all size.

print(" Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0
error = 0
if (size == "S") | (size == "s"):
    bill += 15
    if (add_pepperoni == "Y") | (add_pepperoni == "y"):
        bill += 2
    elif (add_pepperoni == "N") | (add_pepperoni == "n"):
        bill += 0
    else:
        print("Invalid Input")
        error += 1
elif (size == "M") | (size == "m"):
    bill += 20
    if (add_pepperoni == "Y") | (add_pepperoni == "y"):
        bill += 3
    elif (add_pepperoni == "N") | (add_pepperoni == "n"):
        bill += 0
    else:
        print("Invalid Input")
        error += 1
elif (size == "L") | (size == "l"):
    bill += 25
    if (add_pepperoni == "Y") | (add_pepperoni == "y"):
        bill += 3
    elif (add_pepperoni == "N") | (add_pepperoni == "n"):
        bill += 0
    else:
        print("Invalid Input")
        error += 1
else:
    print("Invalid Input")
    error += 1
if (extra_cheese == "Y") | (extra_cheese == "y"):
        bill += 1
elif (extra_cheese == "N") | (extra_cheese == "n"):
    bill += 0
else:
    print("Invalid Input")
    error += 1

if error == 0:
    print(f"Your final bill is ${bill}")
else:
    print("Try again")
 



# ***************************************************************************************
# ******************      Terinary Operator Example    **********************************

# Basic
age = 30
if (age > 18):
    message = "Eligible"
else:
    messaage = "Not Eligible"
print(message)

# Replacing the above program with Terinary Operator
age = 30
message = "Eligible" if age > 18 else "Not Eligible"
print(message)

# ****************************************************************************************
# Using logical operators to model more complex conditions

# AND             (Since these Operators also yield Boolean outputs )
# OR              (Very useful in using with if statement)
# NOT

water = False    # not water means (False False) which is True
bone = True
cereals = True

if ((cereals or bone) and not water):
    print("my dog had his lunch")
else:
    print("not eaten")

# Short Circuit Evaluation

# if there is a False comes first in AND operation it will not check the rest of expression
# if there is a True coems first in OR operation it will not check the rest of expression

# Chaining Comparison Operator and logical operator
age = 22
if age >= 18 and age < 65:       # same as (18 <= age < 65)
    print("Good for working")


# very useful in operator                     (for loop and in operator )

numbers = [1, 2, 3, 4]     # created a list
if 3 in numbers:           # no need for a for loop to check
    print("3 is there in the list")
else:
    print("3 is not there in the list")


# ***************************************************************************************
