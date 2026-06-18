# python codes are executed line by line
# your python interpreter converts the python code to machine readable codes
# print function
# the print function is used to return an output to the terminal
# print(90)
# print(190)
# print(290)
# print(390)

# comment
# it is used to explain our codes better. it should be written above the code and it should be brief
# it can be used to deactivate our code when testing it

# various data types in python
# integer---whole numbers (+ or -) e.g 2,5, -3, 6
# string---this is a sequence or collection of characters denoted by the presence of a quotation mark. ' ' or " ". they are also referred to as textual data e.g "jones", "78"
# float---these are decimal numbers or fractions. e.g 1.0, 2.9, 5.4
# boolean---it represent two states -- True or False
# list, tuples, dictionaries..

# write a python program that would print different data types.
# this is a string

'''print("i have a pen")'''
# this is an integer
'''print(35)'''
# this is a float
'''print(4.654)'''
# this is a string
'''print("throw")'''

# variables
# variables are containers used for storing data values in the computer memory.
# variables make use of the assignment (=) to assign (store) a value to a variable
# rules for creating variable name 
# 1- avoid the use of numbers and special characters when creating variable names
# 2- avoid spacing words instead, use underscore to join words (snake-case) or capitalise the first letter of everyword, after the first word (camecased styling)

'''number = 10
print(number + 20)'''

# using underscore _ to join words together
'''first_name = "john"
last_name  = "smith"
print(first_name)'''

 # concatenation -- joining strings together using the plus (+) operator
'''print(first_name +" "+last_name)'''

# class work
# write a python program that will return john likes red. hint: make use of variable
# using python variables, write a program that shows that a person's name is john, he is 12 years old and is a student

# john likes red
'''name = "john"
colour = "red"
result = (name + "likes " + colour)
print(result)
print(f"{name} likes {colour}")'''

# second class work
# name = "john"

# python functions

# print function---it is used to return an output to our terminal
# print()---

# input function---it allows a user write into a program. it receives data from a user
'''name = input('enter your name: ')
print(name)'''

# reverse function [::-1]

# length function -- 
# e.g 
'''print(len(data))'''

# zero indexing -- 0
# we can access these string characters by using our 'square bracket' []
# e.g 
'''print(data[0])
print(data[1])'''
# e.g
'''data = "python programming"'''
'''print(data[6])'''
#  note: strings are immutable. that is, they cannot be modified.


# SLICING

# string slicing - accessing more than one characters in a string
# types are;

# positive slicing 
'''data[0:3]'''
'''print(data[0:6])'''
# data[:] -- to print everything on data

# negative slicing
'''print(data[-11:-4])'''

# the 'IN' keyword checks for the existence of a character in a string
# e.g
'''result = "python" in data
print(result)'''

# the 'NOT IN' keyword is used to negate a statement
# e.g
'''result = "python" not in data
print(result)'''

# methods-- these are functions that are specific to python objects (strings, integers, list, tuples e.t.c)
# strings methods -- these are functions that are specific to string.
# methods can be access using the 'dot notation'
'''print(data.upper())
print(data.capitalize())
print(data.lower())'''

# using the 'is' method in string method -- these method brings out it result as boolean i.e true or false
# e.g
'''print(data.isupper())
print(data.islower())
print(data.isdigit())
print(data.istitle())'''

# using the find method -- to get the number of a string just like subscriting whereby using the number to get the character of a string by using the square bracker []
# e.g
'''print(data.find("p"))'''

# comparison operator -- it also return in boolean state i.e true or false
'''== -- equality
!= -- not equality / not equal to
> -- greater than 
< -- less than
>= -- greater than or equal to
<= -- less than or equal to'''
# e.g
# x = 20
# y = 20

'''print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x > y)
print(x < y)'''

# logical operators -- just like comparison operators, they are used in conditional testing
'''and -- it returns true if both condition stated is true, if one of the condition ceases to be true, it returns false
or -- it returns true if one or rather either of the condition stated is true, if only boththe conditions stated are not true, it returns false
not -- it negates a statement'''
# print(x > y and x < y)
# print(x > y or x < y)
# print(not x == y)
# print(x > y and not x != 20)

# class work
# write a python program that asks a user his name and favorite colour and prints something like teslim likes -=[][][]
'''name = input("enter your name")
color = input("what your favorite color?")
print(name + " likes " + color)''' 


# or
'''name = input("what is your name?")
color = input("what is your favorite color?")
result = print(name + " likes " + color)
print(result) '''

# concatenation--- this is the process of joining strings using the plus operator (+)
'''print(name + " "+"likes" +" "+color) 
print(f"{name} likes {color}")'''

# variable casting involves declaring types on variables. e.g
'''name = str("teslim")
age = int(60)
salary = float(90.0)
student = bool(false)'''

#  you can convert one data type to another -- type  conversion
# str-- int
# int-- str
# int-- float
# float-- int

# to know the type of data
# e.g 
'''data = 100
print(type(data))

score = ("100")
print(type(score))

tax = (1.03)
print(type(tax))

# to convert one data type to another data type
print(str(data))
print(type(str(data)))
print(int(score))
print(type(int(score)))
print(int(tax))
print(type(int(tax)))'''


# classwork
# write a python program that ask a user the year born and calculate the user's age

'''user = input("what year were you born?: ")
current_year = input("enter your current year?: ")
user_year = int(user)
current_new_year = int(current_year)
user_age = current_new_year - user_year
print(user_age)
user_new_age = str(user_age)
print("i am " + user_new_age + " years")'''

# # or

'''print(f"i am {user_new_age} years")'''


# exercise one
# write a python program which accepts the radius of a circle from the user and compute the area

'''radius_of_circle = input("enter the radius of your circle\n")
new_radius_of_circle = int(radius_of_circle)
pie = 22/7
area = pie * new_radius_of_circle ** 2
print(area)'''

# exercise two
# write a program which accepts a user's first name and print it in reverse order.

# reversed order
'''first_name = input("what is your first name?\n")
print(first_name[::-1])'''



# exercise three
# write a program that accepts on integer(n) and computes the value of n + n n + n n n

'''number = input("enter an integer ")
n = int(number)
result = n + n * n + n * n * n
print(result)'''

# arithemetic operators
#  + , - , * , ** , / , // , %
'''x = 20
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)'''

# changing case in a string with methods
# e.g
'''course = "python for beginners"
print(course.upper())
print(course.title())
print(course.capitalize())
print(course.find("p"))
print(course.find("s"))'''


# augmented or compound assignment operations
#  +=, -=, *=, /=, //=, %=
'''x = 10
x += 1
print(x)

x -= 1
print(x)

x *= 1
print(x)

x /= 1
print(x)

x **= 1
print(x)

x = 10
x = x +1
print(x)'''


# order of precedence
# parenthesis ()
# exponential **
# multiplication or division 
# addition or subtraction

#  CONDITIONAL STATEMENT

# using the "IF" statement,
# if statement -- this will execute a block of code as long as the conditional stated is true.
# else statement -- this will execute a block of code if the condition stated in the if block is not met.
# elif (else if) this is used in a chained if statement. i.e it is used when we are testing multiple conditions.

#  e.g
'''x = 0
if x == 10:
   print("yes")
elif x < 10:
    print("i dont't know")
else:
    print("no")'''

# classwork
# write a program that checks the length of a password. if the password length is less than 6 or greater than 12, it should reject it. but if iot is between 6 and 12 characters, it should accept.

'''password = input("enter your password\n")
x = len(password)
if x < 6: 
  print("reject")
elif x > 12:
    print("reject")
else:
    print("accept")'''

# or
'''x = len(input("enter your password\n"))
if x < 6 or x > 12:
    print("reject")
else:
    print("accept")'''

'''x = int(input("enter a value: "))
if( == 14)
     print("ok")
else:
    print("not okay")'''

'''x = int(input("enter a value: "))
if x > 2:
    print("positive")
elif x < 0:
    print("negative")
elif x == 0:
    print("zero")
else:
    print("i don't know")'''

#    weight converter 
'''write a python program that converts from kg to lb(pounds) and from lb to kg. the program should be case insensitive. i.e it should treat KG and kg as one or lb and Lb the same''' 
# WHEN THE USER ENTERS HIS OR HER VALUE IN INTEGER OR FLOAT
'''weight = float(input("enter a digit\n"))
unit = input("enter a unit\n")
if unit == "KG" or "kg":
    print(int(weight * 2.205))
elif unit == "LB" or "lb":
    print(int(weight / 2.205))
else:
    print("invalid unit")'''

# WHEN THE USER INPUT IS IN INTEGER ONLY
'''unit = input("enter unit\n").lower()
value = int(input("enter value\n"))
if unit == "kg":
    result = value * 2.205
    print(result)
elif unit == "lb":
    result = value / 2.205
    print(result)
else:
    print("otherwise")'''

# JOTTING

# LISTS---A list is a collection of items in aparticular order, a square bracket [] is used to indicate a list and individual elements in the list are separated by commas.
#  e.g 
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
print(bicycle)'''

# ACCESSING ELEMENTS IN A LIST--to access an element in a list, write the name of the list followed by the index of the item enclosed in a square bracket.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
print(bicycle[0])'''

# CHANGING,ADDING AND REMOVING ELEMENTS 

# MODIFYING ELEMENTS IN A LIST i.e changing an element in a list--To change an element, use the name of the list followed by the index of the element
#  you want to change, and then provide the new value you want that item to have.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
bicycle[0] = 'tricycle'
print(bicycle)'''

# ADDING ELEMENTS TO THE END OF A LIST--The simplest way to add a new element to a list is to append the item to the list.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
bicycle.append('tricycle')
print(bicycle)'''

# INSERTING ELEMENT INTO A LIST-- you can also add a new item to your list by using the insert() method
# this is done by specifying the index of the new element and the value of the new item
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
bicycle.insert(1, 'tricycle')
print(bicycle)'''


# REMOVING ELEMENTS FROM A LIST--this can be done in different ways

# Removing an item using the del statement--if you know the position of the item you want to remove from a list
# you can use the 'del' statement.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
del bicycle[2]
print(bicycle)'''

# Removing an item using the pop() method-- the pop() method removes the last item in a list but it lets you work on it even when removed
#  with that item after removing it.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
popped_bicycle = bicycle.pop()
print(bicycle)
print(popped_bicycle)'''

# you can also pop items from any position 
'''print('The first man to drive a bicycle was ' + popped_bicycle.title() + ' ')'''


# Remove an item by value--if you know the value of the item you want to remove you can use the remove() method.
# The remove() method deletes only the first occurrence of the value you specify. If there's possibility the value
# appears more than once in a list, you'll need to use a loop to determine if all occurrences of the value have been
# removed.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
bicycle.remove('redline')
print(bicycle)'''

#  or to use a varaible to store what you remove when using a remove() method

'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
not_neccessary = 'redline'
bicycle.remove(not_neccessary)
print(bicycle)'''


# ORGANIZING A LIST

# Sorting a list permanently with the sort() method-- to sort out the item in a ist in an aphabeltical order. it is permanently changed.
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
bicycle.sort()
print(bicycle)'''

# Sorting a list temporarily with the sorted() function
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
print("Here is the original list:")
print(bicycle)

print("\nHere is the sorted list:")
print(sorted(bicycle))'''

# printing in a reverse order--in this case the reverse() method is in used 
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
bicycle.reverse()
print(bicycle)'''

# finding the length of a list
# e.g
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
len(bicycle)'''
# to get the length of a list as an output
'''bicycle = ['trek', 'connodale', 'redline', 'specialized']
print(len(bicycle))'''




#  PYTHON LOOPS

'''loops --- this is a way of running a block of code repeatedly. it involves running a block of code multiple or numerous times'''
# two popular loops in python is the 'FOR' loop and 'WHILE' loop

#            WHILE LOOP

# 'WHILE loop' -- this execute a block of code continuously as long as the condition stated is true. once the condition is no longer true, the loop stops
# if the condition stated is not true, the loop won't start 
# steps involved in running a WHILE loop
'''--- the initialisation -- combination of declaring a variable and assigning it value
x = 10
--- test a condition
x < 10
--- increment or decrement
x += 1  x -= 1'''

# e.g using a WHILE loop, write a python program to output from 1-10


'''x = 1
while x <= 10:
  print(x)
  x += 1'''




#  other programs
# -30 - 30

'''x = -30
while x <= 30:
 print(x)
 x += 1'''

# 30 - 0

'''x = 30
while x >= 0:
  print(x)
  x -= 1'''

# 30 - 0 even numbers

'''x = 30
while x >= 0:
  print(x)
  x -= 2'''

# 1 - 30 odd numbers

'''x = 1
while x <= 30:
   print(x)
   x += 2'''

# break statement --- this is used to completely jump out a loop
#  e.g
# x = 1
# while x <= 10:
#    if x == 6:
#        break
#    print(x)
#    x += 1

#  classwork

# -30 - 30

# x = -30
# while x <= 30:
#    if x == 16:
#         break
#   print(x)
#   x += 1

# 30 - 0

# x = 30
# while x >= 0:
#     if x == 20:
#         break
#   print(x)
#   x -= 1

# 30 - 0 even numbers

# x = 30
# while x >= 0:
#     if x == 15:
#        break
#   print(x)
#   x -= 2

# 1 - 30 odd numbers

# x = 1
# while x <= 30:
#     if x == 25:
#        break
#   print(x)
#   x += 2


# continue
# continue breaks one iteration 

# x = 1
# while x <= 10:
#    if x == 6:
#        break
#    x += 1
#       continue
#    print(x)
#    x += 1




#  guessing game 
'''if the user guesses right, it should return you win. otherwise, it should return try again. users should be given three trials at the end
of the third trial, if the user still guesses wrong, it should return you lose '''

# trials = 1
#  while trials <= 3:
#      guess = int(input("guess a number from 1-10?: "))
#      if guess == 8
#        print("you WIN!!!, you got the right number")
#        break
#        else:
#            print("TRY AGAIN!!!")
#     if trials == 3:
#         print("you have used up your guesses. you LOSE!!")
#     trials += 1 


#             FOR LOOP  

# 'FOR loop' -- this is used to iterate through a collection/sequence of character or loop through a list of character.
#  e.g
'''name = "i'm just a boy"
for names in name:
    print(names)'''

# name = "i'm just a boy"n 
# for names in name:
#     if names == "a":
#        break
#     print(names)

# name = "i'm just a boy"
# for names in name:
#     if names == "a":
#         continue
#     print(names)

#  Range -- with your range function you can loop through a sequence of numbers, it can take in a single value 
#  e.g
'''for value in range (1,21):
    print(value)

for value in range (11):
    print(value)'''

# Using Range() to make a list of Numbers
'''numbers = list(range(1,11))
print(numbers)'''

# Using the range function to skip numbers in a list like even numbers
'''even_numbers = list(range(2,11,2))
print(even_numbers)'''
# or 
'''odd_numbers = list(range(1,29,2))
print(odd_numbers)'''

# How to put the first 10 square numbers into a list
'''squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)'''


# write a program to keep asking for a number until you enter negative number, at the end print the sum of all entered numbers
'''start_number = 0
end_number = 1
list_of_number = []
while start_number < end_number:
    number = int(input("enter a number: "))
    start_number -=1
    if number < 0:
        break
    else:
        list_of_number.append(number)
print(sum(list_of_number))'''
        


# write a program to write a name until the user enter END. 
# print the name each time, when you are done print i am done 

'''active = True
while active:
    message = input("enter your name")
    if message == "END":
        active = False
     print("I AM DONE!")
   else:
       print(message)'''


#  correction

'''message = input("enter a name: ")
list_of_names = []
if message == "END":
    print("I AM DONE")
else:
    list_of_names.append(message)'''



# 5/04/2022
#   

# FUNCTIONS
'''functions-- functions are used to structure our code, maintain our codes and make our code reusable. it keeps our codebase cleaner and prevents repitition of codes
(DRY(Dont repeat yourself)principle).
 we have two broad classification of functions-- user-defined functions or custom functions and python built-in function

 custom-function
-- it starts with the def keyword followed by the function name and a set of round brackets or parenthesis
 the parenthesis can be empty or could contain variables called parameters.
the body of the function contains the code to be executed.
-- a function would not be executed unless a call is made to that function'''

# Example:
#  write a python function that prints hello world..
# first , declare the function
'''def greetings():
    print ("hello world")'''
# secondly, call the function to evoke it 
'''greetings()'''



# parameters and arguments
'''parameters are variable that are declared in the function definition. 
they act as placeholders for the actual value to be passed into the function.
-- arguments are the actual value to be passed into a function when a call is made to the function e.g when you write a python function to return 
the sum of two numbers, you pass in the parameters in the function definition like a,b or c,d or x,y . these parameters denotes the two numbers that would be passed 
into a function. while the actual value but that you pass into the function at the point of cell e.g 2,2 or 3,4 or 6,7 or 12,12 are called the arguments.'''


# write a python function that return the sum of two numbers
# x and y are called the parameters.
'''def sum_numbers(x,y):
    print(x + y)'''
# arguments are passed into the function when call is made e.g 10,10,20,19
'''sum_numbers(10,10)
sum_numbers(20,19)'''

# arguments are divided into positional arguments and keyword arguments
# positional argument is when the arguments are passed based onthe position of the parameter.
'''def sum_numbers(x,y):
    print(x + y)'''
# positional argument 
'''sum_numbers(10,20)
sum_numbers(20,19)'''


# keyword argument is when you assign the argument to a parameter at the point of call. kwargs helps to explain our code better.
'''def sum_numbers(x, y):
    print(x + y)'''
# keyword argument
'''sum_numbers(x=10,y=20)
sum_numbers(y=20,x=19)


def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name(fname="john", lname="doe")'''
# you can interchange the arguments when using kwargs
'''full_name(lname="doe",fname="john")'''

# classwork
# write a python function to check whether a number entered by a user is in a given range also entered by the user 
'''def check_number():
    number = int(input("enter a number: "))
    x = range(int(input("enter a given range: ")))
    if number in x:
        print(True)
    else:
        print(False)
check_number()'''

# write a python function that accepts a string and calculate the number of upper case letters and lower case letters. Hints:check isupper() & islower() functions

'''def calculate_strings():
    message = input("enter a message: ")
    uppercase = 0
    lowercase = 0
    for i in message:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
    print("The Total number of uppercase is ", uppercase)
    print("The Total number of lowercase is", lowercase)
calculate_strings()'''


# create a function show Employee() in such a way that it should accept employee's salary.
# The function should return the employee level
    #    -if salary < 50000, level-low
    #    -if salary > 50000, level-high

'''def salary_employee():
    salary = int(input("enter your monthly salary: "))
    if salary > 50000:
        print("level-high")
    else:
        print("level-low")
salary_employee()'''


# write a program that accept integer from the user and display the cube of the number from 1 up to a given
# integer passed to a function e.g
# Given:input_number = 6

'''def input_number():
    number = int(input("Enter a number: "))
    print(number ** 3)
input_number()'''


# 11/04/2022

# lambda function
# this is a simple anonymous function. it can take any number of arguments but have a single expression
# e.g

'''a = lambda x, y: x + y
print(a(3, 5))

b = lambda x,y: x - y
print(b(10,3))

c = lambda x, y: x / y
print(c(10,2))'''
# e.t.c


# higher-order function
# A Higher order function is a function that takes other functions as an arguments or as a return value
# e.g

'''def sum_function(x, y):
    return x + y

def diff_function(x, y):
    return x - y'''

# Higher order function
'''def higher_function(func, x, y):
    return func(x, y)

result = higher_function(sum_function,10,3)
print(result)

result_1 = higher_function(diff_function,30,20)
print(result_1)'''


#  Nested function
# e.g

'''def outer_func():
    def inner_func():
        print('i am inside a function')
    return inner_func
new = outer_func()
new()''' 

# scope-- The locations in a program in which a name can be used. And by name, we mean variable or function.
#  there are like two types

# GLOBAL SCOPE: Which a module or file, a variable that is assigned outside of any function is part of global scope.

# LOCAL SCOPE: A variable that is assigned inside a function is local to that function. when that function is done 
# running, that variable caeses to exist. A lower level scope such as a function body can access a name from higher
#  level scope like the global scope in the file, but a higher level scope like the globe in the file cannot access
# a name from a lower level scope like a function.

# e.g
# LOCAL SCOPE
'''def result():
    var = 50
    print(var)
result()'''

# GLOBAL SCOPE
'''var = 10000
print(var)'''
#  how to relate your global scope with your local scope,
'''value = 100

def result():
    var = 50
    print(var + value)
result()'''

# The global scope can be use in a way as a constant whereby the value doesn't change, e.g


# 12/04/2022

#  Constant Variable
# many at times, global variables are used as constant. these are values that do not change throughout a program.
# e.g
'''PRICE = 800
def profit():
    print(PRICE * 100)

def sales():
    print(PRICE + 100)

def lost():
    print(PRICE / 100)'''


# Shadow Variable
# this is a situation where by the global and local variable have the same name.

# LISTS

# List--is a data structure that stores an ordered sequence of objects. it is called an array too. It is created
# using a square bracket[]. Each object in the list is called an element or an item. The items can be homogenous or heterogenous.
# The length of a list is equal to the number of elements that it hold. Lists are mutable i.e it can be changed.
# e.g
# HOMOGENOUS
'''list_1 = [1, 2, 3, 4, 5, 6]'''
# HETEROGENOUS
'''list_2 = [1, 2, 3, True, "five", 6.0]'''

# list constructor function
'''list_3 = list((1, 2, 3, 4, 5, 6))
list_4 = list((1, 2, 3, True, "five", 6.0))'''


# len()--returns the number of characters in a list
# e.g
'''print(len(list_1))'''

# To check if a List contains an item using the 'in' and 'not in' keywords.
# positive and negative indexing--it starts counting from zero. The index represent the order of the element in the list.
# The negative value is used to pull element from the end of the list.
# e.g

'''print("five" in list_2)
print(10 in list_2)'''

# List Comprehension--it allows you to generate the same list in one line of code
# e.g--to put the first 10 square numbers into a list
'''squares = [value ** 2 for value in range(1,11)]
print(squares)'''

# How to put the first 10 square numbers into a list
'''squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)'''

# Using a mutiple list
# e.g
'''available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza")'''


# LIST METHODS--these are function that are specific to python list. 

# append() Method--it add an item to the end of a list.
# e.g
'''list_1.append(22)
print(list_1)'''

# extend() METHOD--it add more than one item to a list, two or more items to a list.
'''list_1.extend(["twenty", 15, "thirty"])
print(list_1)'''

# remove() METHOD-- use to remove an item from a list.
# e.g
'''list_2.remove(1)
print(list_2)'''

# pop() METHOD --it removes the last item in a list
# e.g
'''list_2.pop()
print(list_2)'''

# insert() METHOD-- it is use to add a new element to a list in doing that you specify the index you want it to be.
# e.g
'''list_1.insert(2, 20)
print(list_1)'''

# clear() METHOD--this is use to clear the elements in a list or use to empty the list.
# e.g
'''list_3.clear()
print(list_3)'''

# copy() METHOD--used to clone a list
# e.g
'''new = list_1.copy()
print(list_1)
print(new)'''
# or
'''new = list_1[:]
print(new)'''

# sort() METHOD-- used to arrange the items in a list.it works for only a string, doesn't work for an integer.
# e.g
'''list_1.sort()
print(list_1)'''
# or
'''list_5 = ['a', 'd', 'c', 'b', 'f', 'e']
list_5.sort()
print(list_5)'''

# reverse() METHOD-- used to rearrange the items in a list from the last item.
# e.g
'''list_5.reverse()
print(list_5)'''

#  How to concatenate two Lists together--by looping throught it
'''list_6 = [1,2,3,7,8]
list_7 = [2,6,0,5]
for o in list_6:
    list_7.append(o)
    print(list_7)'''

# 13/04/2022
# exercise
# To run the sum of this list
'''list_1 = [1,2,3,4,5]
print(sum(list_1))'''

# or

'''sum_of_list = [1,2,3,4,5]
ans = 0
for i in sum_of_list:
    ans += i
print(ans)'''

# To run a the average of a list
'''list8 =[2,3,4,5,7,8,2]
print(Avg)'''

# Run the min and max of a list
'''print(min(list8))
print(max(list8))'''

# class---

# Tuples--this is an ordered python data structure denoted by the prescence of round bracket. they are immutable
# and allows for duplicate values.
# e.g

'''tuple_1 = (1,2,3,4,5)
tuple_2 = ("one",2,3.0,True)

tuple_3 = tuple((1,2,3,4,5))'''

# to get the length of a tuple
'''print(len(tuple((1,2,3,4,5))))'''
# or
'''print(len(tuple_2))'''

# loop through a tuple
# sum


# multidimensional tuple-- tuple inside another tuple
# e.g
'''tuple_4 = ((1,2,3),(4,5,6))'''
# To access the character in a tuple--
'''first count the  brackets of the tuples  
before counting the characters in them starting from zero(0).'''
# to access 6 in tuple_4
'''t = tuple_4[1][2]
print(t)'''
# to access 3 in tuple_4
'''g = tuple_4[0][2]
print(g)'''

# unpacking in tuples-- here, we declare more than one variable to store our items
'''x, y, z = (1, 2, 3)
print(x)
print(y)
print(z)'''

# Tuple have two METHODS--
# COUNT  and
# INDEX method

# COUNT METHOD--to count the number of times a character appear in a tuple.
'''tuple_5 = (4,6,8,9,4)
print(tuple_5.count(4))'''

# INDEX METHOD--to look for the particular number of character in a tuple like the number of a character 
# when counting it from zero.
'''print(tuple_5.index(8))'''


# 19/04/2022

# Dictionaries are python data types that are denoted by curly brackets. they are mutable. they do not allow 
# duplicate values. they store data in key_value pairs. they cannot be accessed by indexing. they are very similar to 
# json data.

'''my_profile = {
    "name" : "john doe" ,
    "age" : "24",
    "city" : "ilorin",
    "course" : "python",
    "hobby" : ["writing", "travelling", "swimming"]
}'''

'''print(my_profile)
print(my_profile["name"])'''

# Dictionary methods:

# get method:
# e.g
'''print(my_profile.get("name"))'''

# keys method--to show all the keys in a dictionary
# e.g
'''print(my_profile.keys())'''
# or
'''for name in my_profile.keys():
    print(name.title())'''

# looping through a dictionary key in order
'''for name in sorted(my_profile.keys()):
    print(name.title())'''

# values method
# e.g
'''print(my_profile.values())'''
# or

# looping through the values in a dictionary without it repeating twice we can use the set() method, can only work for a string.
'''for run in set(my_profile.values()):
    print(run.title())'''

# clear method
# e.g
'''print(my_profile.clear())'''

# more examples
'''print(my_profile.items())
print(my_profile.copy())
print(my_profile.pop(("course")))
print(my_profile.popitem())
print(my_profile.update(("duration":"12 weeks"))'''

# Adding New key value pairs in a dictionary
'''my_profile["Religion"] = 'christian'
print(my_profile)'''

# How to loop through a Dictionary
# e.g
'''for i in my_profile:
    print(my_profile[i])'''

# to remove key value pairs
'''del my_profile["course"]
print(my_profile)'''

# looping through all key value pairs in a dictionary-- if you want to see everything stored in a dictionary
# use the 'for' loop and also the items() method but can only work for string not integer or list.
'''for key, value in my_profile.items():
    print("\nkey: " + key)
    print("\nvalue: " + value)'''


# Nested-Dictionaries---pg 109
# A lIST OF DICTIONARY:
# e.g
'''alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)'''
# to use range() to create a fleet of 30 aliens;
'''aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)'''
# to change the first three alien details at of the five
'''for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'''

'''for alien in aliens[0:5]:
    print(alien)
print('....')
print("Total number of aliens: " + str(len(aliens)))'''

# A LIST IN A DICTIONARY:
# e.g
'''favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c++', 'coding'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'java']
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())'''

# A DICTIONARY IN A DICTIONARY:
'''students = {
    1: {
        "name": "john doe",
        "email": "johning@gmail.com",
        "password": "2344"
    },
    2: {
        "name": "love john",
        "email": "lovecare@gmail.com",
        "password": "5567"
    },    
    3: {
        "name": "mercy doe",
        "email": "mercy@gmail.com",
        "password": "1111"
    },      
    4: {
        "name": "steven doe",
        "email": "stdoe@gmail.com",
        "password": "3224"
    },      
}

print(students[2]["name"])
print(students[3]["email"])
print(students[4]["password"])'''


# 20/04/2022

# Python Modules
# Modules is a file with python codes. We use modules to organise our codes into multiple files
# it organises and structure our codes, makes it reusable too
# a module should contain all the related functions and classes 
# import name of file(obj) or from name of file import name of function, if mutiple functions use comma

# example
# generate budget
'''# to work with nigeria's budget, you need nigeria's ppp
# first import the budget from another module
import home

# then you access the methods in home by,
nig_ppp = home.nig_inc()
print(nig_ppp)

# also for ghana's ppp
gha_ppp = home.gha_inc()
print(gha_ppp)

# for South Africa
SA_ppp = home.SA_inc()
print(SA_ppp)'''
#  OR
# second way to import
'''from home import nig_inc, gha_inc, SA_inc
nig_ppp = nig_inc()
print(nig_ppp)

gha_ppp = gha_inc()
print(gha_ppp)

SA_ppp = SA_inc()
print(SA_ppp)'''

# Python Module Index
'''import math
print(math.ceil(2.99999))
print(math.floor(3.0988))
# print(math.asin(90))
print(math.pow(2,3))
print(math.sqrt(49))
print(math.factorial(4))
print(math.pi(4.8))'''


# 25/04/2022
# How to use Random Module

'''import random
print(random.random())'''

# to get random numbers in mutiple times
'''import random
for i in range(10):
    print(random.random())'''

# to use the randint to get integers randomly
'''import random 
random_integers = random.randint(1, 10)
print(random_integers)'''

#  using random.choice-- which is use to select an item randomly
'''import random
cars = [1, 2, 3, 4, 5, 6]
print(random.choice(cars))'''


# PACKAGE
'''Package is just like a collection of module'''
# we have python package and custom package
# how to use our custom package 
# first create a folder that will serve as our package named "package"
'''from package import __init__
print(__init__) '''


# Using datetime Module
'''import datetime'''
# first assign a variable then using the datetime method then typing the year, month and day
'''date_of_birth = datetime.date(2022, 11, 7)'''
# then we can access the year by,
'''print(date_of_birth.year)'''
# also the month by
'''print(date_of_birth.month)'''
# and also the date
'''print(date_of_birth.day)'''

# using datetime.time method -- to know the time
'''import datetime'''
# assign a variable to it then arrange in hour, minute and second
'''time_of_birth = datetime.time(2, 22, 45)'''
# to get the hour
'''print(time_of_birth.hour)'''
# to get minute
'''print(time_of_birth.minute)'''
# and also second
'''print(time_of_birth.second)'''

# How we can work with datetime.timedelta()--- it can be use to add to a date
'''import datetime
date_of_birth = datetime.date(2022, 11, 7)
new = datetime.timedelta(2003)
print(date_of_birth + new)'''

# 26/04/2022



