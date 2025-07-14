import os
os.system("cls")
name = ["ajai", "nakshu" ]
age = [30,25]
department = ["IT","HR"]
age[1] =10

list_dict = dict(zip(name, age))

print(list_dict)

name = "ajai Raj"
Name = list(name)
print(Name) 
print (len(Name))
print(Name[0:3])
combine = "".join(Name)
print (combine)

number = [1,2,3,4,5,6,7,8]
print(sum(number))
first, *rest, last = number
print(first, last)  