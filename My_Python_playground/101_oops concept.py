import os
os.system("cls")

# ***********************************************************************

#                      Ex of classes objects and methods:

# ************************************************************************



# Example 1
class Vehicle:

  def __init__(self, make, model, year):   #self is how the object car passes into the constructor init
    self.make = make       # here the make atribute Toyota is assigned to car.make
    self.model = model  
    self.year = year

  def drive(self):  # how method drive is defined in the class
    print("Driving", self.model)

car = Vehicle("Toyota", "Camry", 2020) # Create object
print(car.make) # notice car.make is assigned in __init_ and saved as another object
car.drive() # Call method requires () sign very important

# explanation of what is self:
#self is how the object car passes into the constructor init
# see how the object car and its attributes are passed into the constructor init
# The self keyword in Python refers to the instance of the class itself. 
# Within a class definition, self is used to refer to the instance being created. 
# When we call a method on an object, Python implicitly passes the object itself as the 
# first argument to the method. This is conventionally called self.

# Vehicle is the class
# make, model, year are attributes defined in the class
# drive() is a method defined in the class
# car is an object instantiated from the Vehicle class
# car.drive() calls the drive method to print "Driving Camry"


####################################################################################
# some basics about self
##################################################################################

#  self.name is an instance variable in this example.

# When we define:

class Animal:

  def __init__(self, name):
    self.name = name

"""

The name parameter passed to init() is assigned to self.name.

The self keyword refers to the instance being constructed. 
So self.name becomes an instance variable associated with each Animal object.

This means:

Each Animal instance will have its own name attribute
We can access it using self.name in the class methods
It will have a different value for each Animal instance

"""
# For example:

cat = Animal("Whiskers") # here an object cat is created and it is an instance of animal class
 # the name attribute is passed through the animal class and reach the constructor _init_
# with the cat as object and is passed as self to _init_ method in the animal class and there
# name whiskers is saved/assigned to cat.name instance variable in the init constructor

dog = Animal("Rover") # similarly an object dog is created as in instance of animal class
# here the name attribute is passed to the animal class and reach the constructor  _init_
# with the dog as object and is passed as self to _init_ method in the animal class and there
# name rover is saved/assigned to dog.name instance variable through the init constructor

print(cat.name) # Whiskers 
print(dog.name) # Rover


"""
So self.name in the init method is creating an instance variable that can store 
a different value for each object created from the Animal class.

In summary:

self refers to the instance
self.name creates an instance variable
This variable can have a different value for each object instance

"""


#################################################################################


class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name}")

p1 = Person("John", 30)
p1.greet()



# When we call p1.greet(), Python will pass p1 as the self argument to greet(). 
# So inside greet(), self refers to the p1 object.
# This allows the method to access and modify attributes on that object, like self.name.
# Without self, the method has no way to know which Person instance it was called on.
# In the init constructor method, self refers to the newly created Person instance. 
# We can initialize the attributes for that instance using self.name = name.

# So in summary:

# self refers to the current instance of the class
# It gives methods access to the object's attributes and methods
# Inside the class definition, it represents the instance being created/operated on
# When a method is called on an object, self is passed automatically


"""what is an init constructor method?
The init method in Python is a special method that is automatically called when an object
is instantiated (created). It is known as a constructor method.
The init method allows you to initialize the attributes of an object when it is created.
It is called every time an object is instantiated: """

class Person:

  def __init__(self, name):  # init is a special method when object is created -->CONSTRUCTOR METHOD
    self.name = name # allows you to initialize attributes when object is created

p = Person('John') 


"""
The first argument is always self, which refers to the current instance.
Additional arguments can be defined to allow passing in initial data.
The init method is useful for setting initial values for attributes, connecting 
to databases/files, or any setup required for the object to work properly.
init is called automatically after the object is created, so you don't need 
to call it explicitly.
so init method is used to create object and initialize attributes at the time of object creation. 
It is called implicitly by Python whenever we create an object of that class.
Other methods can be defined to modify attributes after the object is created.

So in summary, init is a constructor method that gets called automatically to 
initialize a newly created object. It is useful for setting up initial attributes and
anything else the object needs on creation."""

#Example 2
class Circle:
  
  pi = 3.14     # Class attribute attached directly to the class

  def __init__(self, radius):   # radius is an attribute defined in class
    self.radius = radius

  def area(self):
    return Circle.pi * self.radius ** 2

c = Circle(5)
print(c.area()) 


# Circle is the class
# radius is an attribute defined in Circle
# pi is a class attribute attached directly to the class
# area() is an instance method that calculates area
# c is a Circle object
# c.area() calls area() on object c to calculate the area

"""
what is an instance?
The term "instance" in Python refers to a specific object that is created from a class.
When a class is defined, it provides a sort of blueprint or template for creating objects. 
The class itself is not an actual object. It's only when you create an object from the class 
that you get an actual instance.

For example:
"""
class Person:
  def __init__(self, name):
    self.name = name

john = Person("John") # john is an instance of the Person class
jane = Person("Jane") # jane is another instance 


"""
Here, john and jane are both instances (objects) created from the Person class.

The key things to note about instances:
An instance is a specific object that is created from a class.
The class is just an abstract blueprint. The instances are concrete objects 
created from the class.
When you call a class like Person("John") it creates an instance of that class.

Each instance has its own distinct set of attributes and methods.
The attributes are defined by the class, but each instance has its own copy of those attributes.

So john.name and jane.name can contain different values, even though they are both 
instances of the same Person class.

So in summary, an instance is a specific object created from a class definition. 
The instance contains its own distinct data and attributes. Multiple instances can be created
 from the same class with different attribute values """




# Example 3
text = "Hello" 

print(text.upper()) # Calls upper() method 
print(len(text)) # Calls len() method

# text is a str object
# upper() and len() are methods defined by the str class
# We call the methods on object text to operate on that string

#################################################################################
# Another set of examples to solidify the concepts:
# 1. Class with just attributes

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 30)
print(p1.name)
print(p1.age) 


# This is the simplest class with just attributes. 
# When p1 is created, it gets its own name and age attributes.

# 2. Class with attributes and methods

class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    
  def bark(self):  
    print("Woof! My name is", self.name)
    
d = Dog("Rex", "Labrador") # d is the variable holding the instance (object)
d.bark()

# This class has both attributes and methods. 
# We can call the bark() method on the Dog object d.
"""

The statement d = Dog("Rex", "Labrador") creates an instance of the Dog class called d.
When we call Dog("Rex", "Labrador"), this creates an instance of the Dog class, passing 
"Rex" and "Labrador" as the initial values for the name and breed attributes respectively.

So it is correct to say:

"d is the instance created from the Dog class with attributes name set to 'Rex' and 
breed set to 'Labrador'".

The key points are:

d is the variable holding the instance (object)
It is created from the Dog class
The __init__ constructor is called to initialize the attributes
name is set to 'Rex' and breed to 'Labrador' based on the arguments passed"""
# Ajai comment: I think an object is a variable carrying a particular subject or event 
#(name or time or any variable) the properties of those variables are carried in the class
#so it takes the template of the class (carrying the instance of the class) which has its
#on attributes and methods. The object is the instance variable holding the particular class instance
#with its own set of attributes and methods defined in the class.


# 3. Class with class attributes

class Circle:
  pi = 3.14  
  
  def __init__(self, radius):
    self.radius = radius 
  
  def area(self):
    return Circle.pi * self.radius ** 2
  
c = Circle(5)
print(c.pi) 
print(Circle.pi)


# Here pi is attached to the Circle class directly as a class attribute. 
# We can access it through the class or objects.

# 4. Inheritance

class Animal:

  def eat(self):
    print("Eating...")


class Dog(Animal):

  def bark(self):      
    print("Woof!")

d = Dog()   # here d becomes the instance of the child class
d.eat() # Inherited from Animal # Here d can call the eat() method defined in the parent class Animal
d.bark() # Defined in Dog # Can also call the bark() method defined in the child class Dog



# Dog inherits from Animal, so it gets all the attributes and methods of Animal. 
# We can reuse eat() method.


# Abstract Base Classes

# These define a generic interface that concrete subclasses inherit from and implement. 
# They can't be instantiated directly but define common methods that subclasses override.

from abc import ABC, abstractmethod

class Animal(ABC):           # Abstract Base Class. this cant be instantiated meaning
                             # object wont pass throught the parent class.
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Bark!")



# Data Classes

# These are simple classes just meant to hold data attributes. 
# Often used as lightweight data containers.

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

'''The key points are:

dataclasses.dataclass is a decorator that marks a class as a data class.
Data classes are meant to hold pure data attributes, with no methods.

When you decorate a class with @dataclass, it automatically adds some special methods
like __init__() and __repr__() to the class.

The class attributes are defined by simply declaring the attribute names and types.
So in this example:

Product is declared as a data class using @dataclass

It has two attributes name (string) and price (float)

The @dataclass decorator will automatically add an __init__() method
that allows creating Product objects like:

'''

apple = Product("Apple", 0.60)
'''
It also adds a __repr__() method to nicely print objects
So in summary, data classes provide an easy way to define lightweight data objects 
without writing a lot of boilerplate code. The decorator adds useful methods for you.
'''

##########################################################################################
# Named Tuples

# These are tuple objects with named fields that you can access via name. 
# Lightweight data objects like classes but immutable.

from collections import namedtuple

Car = namedtuple('Car', ['make', 'model'])
my_car = Car('Toyota', 'Camry')
print(my_car.make) 

"""A named tuple in Python is a lightweight data structure similar to a regular tuple,
 except each element can be accessed by a name rather than just index.

For example:

from collections import namedtuple

Car = namedtuple('Car', ['make', 'model'])


This creates a named tuple type called 'Car' with two attributes: make and model.

We can then create instances of this named tuple:

my_car = Car('Toyota', 'Camry')


And access the fields by name:

print(my_car.make) # Toyota
print(my_car.model) # Camry



The key aspects are:

Named tuples provide access to elements by attribute name
They have a fixed set of fields defined when created
Lightweight immutable objects, similar to regular tuples
Useful for simple data objects with named fields
So in summary, named tuples allow you to create tuple-like objects 
that have field names rather than just indices. This can make the code more readable 
and self-documenting.

"""

# Linked Lists

# Class can represent nodes in a linked list data structure.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 



# So in summary, Python has many kinds of classes for different purposes 
# like inheritance, data storage, data structures, etc. 
# But the core ideas of class attributes and methods remain the same!




# Here are some other common types of classes and objects in Python:

# Mixin Classes

# These are classes that provide methods intended to be inherited by other classes, 
# not used on their own. Allow reusable bundles of methods.

class ReprMixin:
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r})'

class MyClass(ReprMixin): 
    def __init__(self, name):
        self.name = name

obj = MyClass('John')  
print(obj) # Prints "MyClass('John')"



# Enumerations

# These are classes that define a set of symbolic names bound to unique constant values. 
# Useful for defined named constants.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED) # 1



# Slots

# This restricts attributes on a class to only those defined in slots. 
# Saves memory with large classes.

class MyClass(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier



# Metaclasses

# These are classes that define the behavior of other classes. 
# Allow custom class creation logic.

class Meta(type):
    def __new__(cls, clsname, bases, clsdict):
        # Custom class creation
        return super().__new__(cls, clsname, bases, clsdict) 

class MyClass(metaclass=Meta):
    stuff = 123



#########################################################################################
"""
Here are 4 of the most important concepts to understand about object-oriented programming (OOP)
in Python:

Encapsulation - Grouping related attributes and methods into an object. 
                This keeps implementation details hidden inside the class.
eg: A BankAccount class that privately stores the account balance 
    and provides a public method to deposit/withdraw money without directly accessing 
    the balance variable.

Abstraction - Exposing only essential features of an object while hiding inner details and 
               implementations. Leads to simpler interfaces.
eg: An abstract Animal class has an eat() method. The Cat, Dog, Bird subclasses override 
   it to implement their own eating behavior.

Abstraction in OOP focuses on the essential features and behavior of an object or concept,
hiding the unnecessary implementation details.
It allows simplifying complex systems by exposing only what's necessary and 
ignoring what's irrelevant at a given level of abstraction.
Defining abstract classes and interfaces in code is a way to achieve abstraction.
They define signatures for behaviors but don't implement them.

Subclasses or implementations then provide the actual logic for the abstract methods
and properties. This enforces a separation of concerns - the abstract class handles 
the general abstraction and subclasses handle specific implementations.
It also allows varying implementations through polymorphism, like having different 
animals implement eat() differently.

Inheritance - As you mentioned, this allows a child class to inherit attributes and methods 
              from a parent class. This promotes reuse and reduces code duplication.
eg: A Vehicle base class that has shared attributes like wheels. 
    Then Car and Motorcycle subclasses inherit the Vehicle class.


Polymorphism - Objects of different classes can be used interchangeably if they share common 
               methods with the same name. Allows code reuse.
eg:A Shape class has a draw() method. The Circle, Square, Triangle subclasses override
   draw() to implement their own drawing logic.
   



Some key points about these:

Encapsulation and abstraction help manage complexity through well-defined interfaces.

Inheritance enables reusable parent classes and specialized child classes.

Polymorphism enables interchangeable objects with the same method names.

Together they facilitate code reuse, modularization, and efficient object design.

Mastering these core principles is important for leveraging the full power of OOP in Python.

So in summary, the big 4 OOP concepts in Python are inheritance, encapsulation, polymorphism, 
and abstraction. Focusing on these will help you design effective, modular, and reusable 
object-oriented code."""

#############################################################################################
"""
Sure, here is an explanation of the 4 OOP concepts 
using the same BankAccount example:

Encapsulation    (use of private method and public method to access private data)
The BankAccount class encapsulates the balance data by making it a private __balance attribute. 
This prevents external code from directly modifying the balance and forces them to use the public 
methods like deposit() and withdraw(). This is for data protection.

Abstraction  (abstract class leave the implimentation details to the child classes)
We can make the BankAccount an abstract base class by defining abstract deposit() and withdraw() methods
without implementation. This focuses on essential features and hides unnecessary details that subclasses 
would implement.Only the implementation happens in the child class meaning the object can be passed only
on the child class.

Inheritance              (child class inherits from parent class)
We can create SavingsAccount and CheckingAccount as subclasses inheriting from the base BankAccount. 
The subclasses inherit the common attributes and behaviors but can define their own specialized methods 
if needed.

Polymorphism        (custom implimentations of deposit and withdraw methods with special features)
The deposit() and withdraw() methods can be overridden in the subclasses to provide custom implementations.
For example, SavingsAccount could limit withdrawals or CheckingAccount could have overdraft protection. 
The subclass methods have the same signature but their own logic.

To use polymorphism:

accounts = [SavingsAccount(), CheckingAccount()]for acc in accounts: acc.deposit(100) # customized per 
account

So in summary, the BankAccount example demonstrates:

Encapsulation via private data attributes
Abstraction through base class definition
Inheritance for subclass specialization
Polymorphism by overriding shared methods
This allows code reuse while still providing flexibility for subclasses to have their own logic. 
The same interface is used polymorphically."""


##################################################################################################################
##  Detailed encapsulation example and description  ####
##################################################################################

###   Here is an example of encapsulation in Python and a detailed explanation:

class Person:

    def __init__(self, name, age):  # init method takes name and age as arguments/parameters 
        self.__name = name          # assigns name to private attribute __name
        self.__age = age            # assigns age to private attribute __age

    def get_name(self):            # public method to get the name
        return self.__name         # returns the value of __name
    
    def get_age(self):            # public method to get the age
        return self.__age         # returns the value of __age

person = Person("John", 30)       # create a Person object
print(person.get_name())          
print(person.get_age())

"""

Here's how encapsulation works in this example:

The class Person has two attributes - __name and __age. Note the double underscores, 
which denote these attributes are private.

The init method takes name and age as arguments and 
assigns them to the private attributes __name and __age.

To access these private attributes from outside the class, 
we define public methods get_name() and get_age().

These act as getters to retrieve the value of the private attributes.

When we create a Person object, we pass the name and age which get 
stored in the private attributes.

To access them, we call the public methods get_name() and get_age().

This way, the internal representation of the class is hidden from external code.

The public methods provide a controlled access to the private attributes and prevent
them from being modified directly.

So in encapsulation, we bundle the data (attributes) and methods that operate on that 
data within a class. And some attributes are made private that cannot be accessed directly 
from outside the class. This helps control the visibility and access of class attributes.
"""
### another example of encapsulation
##This code seamlessly builds on the existing BankAccount class and examples by creating an 
# instance of the class and calling the relevant methods to demonstrate encapsulation.

class BankAccount:
    def __init__(self, intial_balance): #__init__() is the constructor initial_balance is parameter
        self.__balance = intial_balance
# so when we call BankAccount(100) outside the class (which you can see below) that
# 100 is passed to __init__() contructor and assigned to __balance, private attribute.
# so __init__() constructor encapsulates the initialization of __balance data/attribute and cant be accessed 
# from outside the class
        
# this __balance cant be accessed from outside the class can only be modified through 
# methods like deposit(), withdraw().
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False
#The get_balance() method is a "getter" method that allows the balance to be accessed from outside the class
# in a controlled way.
    def get_balance(self):
        return self.__balance


"""
This demonstrates encapsulation because:

The __balance attribute is prefixed with double underscores, 
which makes it a "private" attribute that can't be directly accessed from outside the class.

The balance can only be modified through the deposit() and withdraw() methods. 
This controls access to the balance.



So the balance data is encapsulated - it can only be modified through the class methods, not directly, 
and the class controls how it is accessed. This keeps the implementation details hidden and prevents uncontrolled
changes to the balance.

The benefit is that the class has full control over the __balance attribute and can manage its value, 
while still allowing the balance to be used outside the class through the getter. This encapsulation keeps 
the class internals private and protected.

"""
my_account = BankAccount(100) #An instance of the BankAccount class is created with an 
                              #initial balance of 100 and an object my_account is instantiated 
# @aj: An instance of a class is created with the constructor and initial balance passed to it
# class is BankAccount 
# instance of a class is the object my_account  (meaning my_account is an instance of the BankAccount class)
# this object carries all the varibles of that instant and properties of the class
"""
With this constructor:

When we call BankAccount(100), 100 is passed to __init__() as the initial_balance parameter
Inside __init__(), it assigns this initial_balance value to self.__balance

So:
BankAccount(100) calls __init__(100)
__init__(100) sets self.__balance = 100

All this means:

The constructor takes the initial balance value as a parameter
It assigns this value to __balance to initialize it
"""


print(my_account.get_balance()) # 100

my_account.deposit(50)
print(my_account.get_balance()) # 150

my_account.withdraw(75)
print(my_account.get_balance()) # 75

# Can't access balance directly from outside class
# print(my_account.__balance) # Error

"""To use the class:

Create an instance of BankAccount and pass the initial balance to the constructor.
In Python, the constructor method is the __init__() method that is called when 
an object is instantiated. 

Call get_balance() on the instance to retrieve the balance

Call deposit() and withdraw() to modify the balance

But cannot directly access the __balance attribute from outside the class

So get_balance() allows retrieving the encapsulated __balance attribute in a controlled way.

"""
class Car:

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year

my_car = Car('Toyota', 'Camry', 2020)
print(my_car.get_make()) # Toyota
print(my_car.get_model()) # Camry 
print(my_car.get_year()) # 2020

"""
In this example:

The __init__() constructor takes make, model, year and assigns them to 
private attributes with double underscores.

The get_make(), get_model() and get_year() methods are "getter" methods to access 
these private attributes.

Outside the class, we can call the getters on a Car instance, but not directly 
access __make etc.

So encapsulation is achieved by:

Making attributes private (double underscore prefix)
Providing getter methods to access these attributes in a controlled way
Not allowing direct access to private attributes from outside the class

This keeps the implementation hidden and controlled through the class interface.
The user doesn't need to know how the class stores the attributes internally.

Let me know if you have any other questions!
"""

##########
class Employee:

    def __init__(self, name, age, salary):
        self.__name = name 
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative!")
        self.__salary = new_salary

emp = Employee("John", 30, 5000)

print(emp.get_name()) # John
print(emp.get_age()) # 30 

emp.set_salary(6000) # Update salary
print(emp.get_salary()) # 6000

emp.__salary = -100 # Error, can't access directly


"""
Key points:

The name, age and salary attributes are private (double underscore)

Getter methods allow accessing these attributes

set_salary method allows updating salary field in a controlled way

We can't directly access or update the private attributes from outside the class

This encapsulates the data and methods into one single class, 
and hides the implementation details from code outside the class."""



##################################################################################################
################
################       Absraction and example
################
##################################################################################################

# Abstraction is a key concept in object oriented programming and has several important purposes:

# Reduces Complexity: Abstraction helps break down complex systems into simpler, more manageable 
# pieces. By hiding unnecessary details, abstraction reduces complexity and allows users to focus 
# on essential functionality.

# Isolates Impact of Changes: When implementation details are abstracted away, the code using those 
# abstractions is shielded from the impact of changes. For example, changing the implementation of a 
# method may not affect any code that simply invokes the abstract method interface.

# Promotes Reusability: Code focused on abstract interfaces can be applied more generally, promoting reuse.
# Interfaces define general capabilities that can be applied broadly across different implementations.

# Enables Modular Design: Breaking a large system into abstract modules with well-defined interfaces 
# enables more modular and flexible design. These modules can be developed somewhat independently and 
# reused in different contexts.

# Improves Readability: Appropriate abstractions can hide distracting details and make code more readable
# and understandable for humans.

# In summary, abstraction is about managing complexity by hiding unnecessary details, reducing coupling, 
# promoting reuse, and improving readability and maintainability of code. It is a fundamental technique 
# for managing complexity in large programs and systems.

## Abstraction refers to hiding complex implementation details and only exposing a simple interface to users.

## In Python, abstraction can be achieved by using abstract classes and interfaces.

## Abstract classes contain one or more abstract methods that have no implementation.

## Child classes inherit from the abstract class and provide implementations for those methods.

## Interfaces serve a similar purpose - they define method signatures that concrete classes must implement.

from abc import ABC, abstractmethod

class Animal(ABC):         # Animal is an abstract class, cannot instantiated directly in this class
                           # meaning object isnt passed here but in child classes
    @abstractmethod
    def make_sound(self):  # make_sound() is an abstract method
        pass

class Dog(Animal):     # Dog is a child class of Animal (abstract class) -> child implement from parent
    def make_sound(self):   # make_sound() is the abstract method implemented in child class
        return "Bark!"

class Cat(Animal):

    def make_sound(self):
        return "Meow"

# Create instances of the child classes
dog = Dog()
cat = Cat()

# Extract information using the child class methods
print(dog.make_sound()) # Woof!
print(cat.make_sound()) # Meow

# Animal is an abstract class that defines the abstract make_sound() method
# Dog and Cat inherit from Animal and provide implementations for make_sound()
# The code uses the abstract class Animal to abstract away the details of how each 
# animal makes a sound
        
#    what is an abstract class, abstract method , Abstract object?

# Abstract class: This is a class that contains one or more abstract methods. 
#                 It cannot be instantiated directly.

# Abstract method: A method signature without an implementation. 
#                 It must be implemented by child classes.

# Abstract object: An instance of an abstract class. 
#                  This is not possible in Python because abstract classes cannot be 
#                  instantiated directly.So in Python, we define abstract classes to provide 
#                  common interfaces and force child classes to provide implementations. 
#                  But we cannot create abstract objects directly from these classes.


# Abstract classes allow defining common interfaces for a group of subclasses (like Animal) while
        # leaving the implementation details to the child classes. This provides a flexible way to
        # abstract away complexity and promote code reuse through polymorphism.

# Abstract classes allow defining common interfaces for a group of subclasses.

# The abstract class Animal defines the common make_sound() interface that Dog and Cat subclasses 
# implement.Abstract classes leave the implementation details to child classes.

# Animal itself does not implement make_sound(), the Dog and Cat subclasses provide the specific implementations.
# This abstraction provides flexibility and promotes code reuse.

# The code using Animal objects doesn't need to know if it's a Dog or Cat, it just calls make_sound().
# This allows flexible reuse of subclasses.
        
# Polymorphism is enabled since different subclasses can provide different implementations.
# Dog and Cat have their own implementations of make_sound() demonstrating polymorphism in action.


#### Example 2 of abstraction..

from abc import ABC, abstractmethod  #The from abc import ABC, abstractmethod imports specific objects 
# from Python's built-in abc module, which stands for "abstract base class".
# ABC is a class that defines the capabilities of an abstract base class. Any abstract class we define
# should inherit from ABC.
# @abstractmethod is a decorator that marks a method as abstract. Abstract methods have a declaration 
# but don't provide an implementation.

class Shape(ABC):      #Shape is the abstract class that defines common interfaces for sub classes
                       # by defining area() and perimeter() as abstract methods but not implement them

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method signature without implementation. Works as a placeholder 
              # which means code will be added here later. act as a null operator.

class Square(Shape): # Square is a concrete subclass of Shape that implement the abstract methods
                     # that are defined in Shape abstract class --> area() and perimeter()
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

square = Square(5)
print(square.area())
print(square.perimeter())

circle = Circle(3)
print(circle.area())
print(circle.perimeter())



# In this example:

# Shape is an abstract class that defines abstract methods area() and perimeter()
# Square and Circle are concrete subclasses that implement the area() and perimeter() methods
# The Shape class provides a common interface for the subclasses
# We can create instances of the subclasses and call area() and perimeter() to get the values 
# based on different implementations

# So the Shape abstraction allows the Square and Circle classes to focus on their own specific 
# implementation details. The client code can simply use the Shape interface to work with different
# kinds of shapes polymorphically.

# This encapsulates the implementation details and provides an abstract interface for different shapes.

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod    
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class SavingsAccount(BankAccount):
    
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

savings = SavingsAccount(500)
savings.deposit(100)
print(savings.check_balance()) # 600

"""This abstracts the implementation details of different account types. 
We can rely just on the BankAccount interface for operations. 
Additional account types could be added without changing the client code.

The key benefit is decoupling the abstract interface from the concrete implementations. 
This allows changing or adding implementations without impacting the abstraction."""


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Turning key to start engine")

    def stop(self):
        print("Pressing brakes to stop")

    def drive(self):
        print("Driving the car")

class Motorcycle(Vehicle):

    def start(self):
        print("Turning ignition to start engine")

    def stop(self):
        print("Pulling brakes to stop")

    def drive(self):
        print("Driving the motorcycle")
        
# Create objects from child classes        
car = Car()
motorcycle = Motorcycle()

# Interact using the abstract Vehicle interface
car.start()
car.drive()
car.stop()

motorcycle.start() 
motorcycle.drive()
motorcycle.stop()


"""
In this example:

Vehicle is an abstract base class that defines interfaces like start, stop, drive
Car and Motorcycle provide specific implementations
The client code uses the abstract Vehicle type to interact with objects
This abstracts away the implementation details from the client
We can add other types of vehicles like trucks or electric vehicles without 
changing the client code much. The key benefit is the abstraction provided by Vehicle."""


#######################################################################################
#####                     inheritance 
 
#       child class gets from parent class 
#                                           (attributes and behaviour)
#######################################################################################

"""
 Inheritance allows new child classes to be defined that inherit attributes and behaviors 
 from their parent classes.

Here are some key points about inheritance in Python:

Child classes inherit methods and attributes from the parent class.

Child classes can override or extend methods from the parent class.

Inheritance allows code reuse - common logic can be defined in the parent class.

Child classes can be specialized versions of the parent class.

"""

#For example:

class Animal:

  def __init__(self, name):  # The Animal class has an init constructor (init method) that takes
    self.name = name          # name paramenter and assign it to self.name
                # self.name is an instance variable assossiated with each animal object
    """
                                          self refers to the instance
                                          self.name creates an instance variable
                        This variable can have a different value for each object instance
    """

  def eat(self):                     # Define eat method in Animal class
    print(f"{self.name} is eating.") # prints the name attribute and a message

class Dog(Animal):  # Dog class inherits from animal class by passing animal inside parentheses

  def bark(self):  # Define its own bark method in Dog child class
    print(f"{self.name} is barking.") 

dog = Dog("Rover")
dog.eat() # Inherited method
dog.bark() # Dog specific method

# We create a Dog instance, passing a name to the constructor.
# We can call the inherited eat() method from Animal.
# And the bark() method defined in Dog.


# In this example:

#  Dog inherits the init and eat methods from Animal
#  Dog class extends Animal by defining a new bark method
#  We can create a Dog instance and call both parent and child methods

"""
this inheritance example does look very similar to the abstraction examples 
I previously provided. The key difference is:

Abstraction focuses on defining common interfaces and abstracting away implementation 
details. The parent class defines abstract methods that child classes implement.

Inheritance focuses on code reuse and extending parent class functionality. 
Child classes inherit concrete methods from the parent and can override or extend them.

But they are very complementary concepts:

Abstraction defines interfaces for subclasses to implement
Inheritance allows subclasses to reuse and build upon parent class code
So in the inheritance example, Animal provides a concrete eat() method that Dog inherits.
In contrast, in an abstract class like:

"""

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


"""
Animal only provides an abstract interface. 
The concrete implementation must be provided by subclasses.

So while abstraction and inheritance are complementary, the key difference is:

Inheritance reuses parent class code
Abstraction requires child classes to provide implementations

"""

############################################
#####   another example of inheritance
################################################
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        print(f"Starting {self.model}")

class Car(Vehicle):

    def open_trunk(self):
        print("Opening car trunk")

class Motorcycle(Vehicle):

    def remove_helmet(self):
        print("Removing helmet")

car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "CBR")

car.start() # Inherited method
car.open_trunk() # Car specific method

motorcycle.start() # Inherited method 
motorcycle.remove_helmet() # Motorcycle specific method


"""
In this example:

Vehicle is the parent class with make, model attributes and start() method

Car and Motorcycle inherit from Vehicle

Car defines its own open_trunk() method

Motorcycle defines remove_helmet()

We can create instances of the child classes and call their inherited and custom methods

Some key benefits of inheritance demonstrated:

Code reuse - child classes inherit common attributes and methods
Specialization - child classes can have their own specific methods
Polymorphism - objects interact differently based on class

"""


##############################################################################################
############                    Polymorphism
##############################################################################################




