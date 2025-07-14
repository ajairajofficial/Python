#################### Python Statements for controlling Flow #########################
#
#                         While Loops for normal data types
#     will run only on bash so do command python3 everydaycode6.py
# ************************************************************************************
#
# A simple explanation
#              while loops repeat as long as the condition is True
#               An infinite loop can be created in while loop
#
# Type 1: while loop
#
#               while (boolean expression using comparison operator):
#                     iterates executes as long as the bool expresion is False
#
# Type 2: infinite loop
#
#                while (True):            (executes for ever)
#                   some thing to execute
#
# Type 3: infinite loop with a break keyword       (while and if )
#
#                while (True):
#                   user_input
#                   if user_input.lower == " some string "
#                      break
#                   execute this line in every iteration
#
#
#

# eg for Type 1              Ok while condition is true execute
print("eg for Type 1")

number = 4
while number > 0:             # number is greater than 0 as long as number = 1
    print(number)            # output will be -->   4 3 2 1
    number -= 1

# eg for Type 3               while loop with if statement and break keyword
print("eg for Type 3")

while (True):
    user_input = input("Searching for my wife /n Enter your name : ")
    secret_word = input("Enter our secret word:")
    if (user_input.lower() == "anu"):
        if (secret_word.lower() == "peace"):
            print("Found my wife yeeeeeeee")
        break


