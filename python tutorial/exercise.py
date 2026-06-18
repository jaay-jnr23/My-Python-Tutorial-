#  DAY ONE
# print("hello world!\nhello world!\nhello world!")
# print("Hello" + " " +"Juwon")

# print("Day1 - String Manipulation")
# print('String Concentration is done with the "+" sign. ')
# print('e.g. print("Hello " + "World")')
# print("New lines can be created with a backslash and n.")

# input("what is your name?")
# print("Hello "+ input("What is your name?"))
# print( len( input("What is your name? ") ) )

# name = input("what is your name?")
# print( name )

# to calculate the length of the string we use....
# length = len( name )
# print(length)

# name = "jack"
# print(name)


# input("a:")
# input("b:")
# print("a = " + a)
# print("b = " + b)


# tip calculator 1 generating a band name 
'''# 1. create a greeting for your program.
print("Hello!!\nHello!!\nHello!!")
print("welcome to the band name generator!!")
# 2. Ask the user for the city that they grew up in
city = input("which city did you grow up in?\n")
# 3. Ask the user for the name of a pet
pet = input("what is the name of your pet?\n")
# 4. Combine the name of their city and pet and show them their band name
print("your band name could be " + city + " " + pet)
# 5. Make sure the input cursor shows on a new line, see the example at:
  https://band-name-generator-end.appbrewery.repl.run/'''

    
#   DAY TWO

#  Data Types

# STRING
# "Hello"
# when we add the []-square bracket, we want to put the index or the position of the character that we want
# by using the square bracket [] and putting a number in it i.e [4] we are able to dissect a string and pull out individual characters
# print("Hello"[0]) 
# for first character

# print("Hello"[1])
# for second character

# print("Hello"[2])
# for third character.....

# INTEGER

# print(123 + 345)

# using underscore (_) it is use to join words together so that when interprted it will be well presentable instead of uing the comma e.g 123_456 as 123456 

# FLOAT
# 3.4567

# BOOLEAN
# True
# False



# num_char = len(input("what is your name?\n"))
# print(num_char)

# first convert the num_char to a string for it to print the number of characters
# new_num_char = str(num_char)

# print("your name has " + new_num_char + " characters")

# to know the type of data
# print(type(num_char))

# print(80 + float("100.52"))
# print(str(300) + str(300))


# classwork
# write a program that adds the digits in a 2 digit number

'''two_digit_number = input("type a two digit number:")'''
# check the data type of the two digit number
'''print(type(two_digit_number))'''
# get each character of the two digit number
'''first_digit = two_digit_number[0]
second_digit = two_digit_number[1]'''
# print both the two digits
'''print(first_digit)
print(second_digit)'''
# get the first digit and second digit using subscripting then convert string to integer or int.
'''first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])'''
# Add the two digits
'''result = int(first_digit) + int(second_digit)
print(result)
 OR
two_digit_number = first_digit + second_digit
print(two_digit_number)'''


# mathematical operations in python
# print(3 + 2)
# print(4 - 2)
# print(6 * 9)
# print(8 / 4)
# print(type(8 / 4))
# print(2 ** 5) -- square power **

# PEMDAS
# P-parentheses ()
# E-exponents **
# M-multiplication *
# D-division /
# A-addition +
# S-subtraction -
# e.g
# 3 * 3 + 3 / 3 -3
# print(3 * 3 + 3 / 3 -3)
# the calculation goes from left to right 

# to change the calculation from a low pirioty to a very higher piority
# e.g
# (3 * (3 + 3) / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)
# the 3 + 3 calculate first because it becomes the higher priority

#  class work---BMI exercise one 
# write a program that calculate the body mass index(BMI) from a user's weight and height
# note: round the result to a whole number

'''height = input("enter your height in M: ")
weight = input("enter your weight in kg: ")'''
# using the exponent creator
'''BMI = int(weight) / float(height) ** 2'''
# change the BMI to integer
'''BMI_as_int = int(BMI)
print(BMI_as_int)'''

# round function used to round a number to a given precision in decimal digits
# print(round(8 / 3))

# to round a number to the decimal places we want,
# e.g to two decimal places
# print(round(8 / 3, 2))
# or
# print(round(2.66666666, 2))

# in using the division we always get a float number, but if we don't want that we can use the flow-division // to get an integer
# e.g 
# print(8 // 3) 

# result = 4 / 2
# result /= 2
# print(result)

# score = 0

# to pin-point that a user score a particular point 
# score += 1
# print(score)

# score -= 1
# print(score)

# score *= 1
# print(score)

# using the f-string instead of converting the int or the float to a string to be able to print 
# score = 0
# height = 1.8
# iswinning = True
# print(f"your score is {score}, your height is {height}, your winning is {iswinning}")


# classwork
# create a program using math and f-strings that tells us how many days, weeks, months we have left if we live until 90 years old 
'''age = input("what is your current age?\n")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months and {years_remaining} years left")
#  or
message = f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months and {years_remaining} years left"
print(message)'''

# Tip calculator 2  to calculate a bill among any number of people in any percentage tip.
'''print("welcome to the tip calculator!!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")'''



#    DAY THREE

#  CONDITIONAL STATEMENT
#  IF / ELSE

# e.g
'''print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
if height >= 120:
  print("you can ride the rollercoaster!")
else:
  print("sorry, you have to grow taller before you can ride.")'''

# module -- it bring out the remainder of a given numbers when being divided 
# e.g 
'''print(7 % 2)'''
# 2 + 2 + 2 + 1
# 1 -- is the remainder of 7 % 2

# exercise
# write a program that works out whether if a given number is an odd or even number using the module function %
# i.e if there is a remainder when a number is divided by two it is an odd number or if there is no remainder it is even.
'''number = int(input("enter a number: "))
if number % 2 == 0:
  print("This is a even number. ")
else:
  print("This is an odd number. ")'''

# Nested 'IF' / 'ELSE' statement: this is when a programmer can check for another condition once the first condition is passed.
# i.e another IF and ELSE statement can be used. in other for this to work the first condtion must be true 
# i.e if the first 'IF' statement is true the second 'IF' statement must be false. for it to work.
# e.g
'''print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("what is your age: "))
  if age < 12:
    print("please pay $5.")
  elif age <= 18:
    print("please pay $7.")
  else:
    print("please pay $12.")
else:
  print("sorry, you have to grow taller before you can ride.")'''

# classwork--- BMI exercise two
# write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# i.e under 18.5 they are unerweight, over 18.5 but below 25 they have a normal weight
# over 25 but below 30 they are overweight, over 30 but below 35 they are obese
# above 35 they are clinically obese.

# solution
'''height = float(input("enter your height in M: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / height ** 2)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, You are underweight. ")
elif BMI < 25:
  print(f"Your BMI is {BMI}, You have a normal weight. ")
elif BMI < 30:
  print(f"Your BMI is {BMI}, You are overweight. ")
elif BMI < 35:
  print(f"Your BMI is {BMI}, You are obese. ")
else:
  print(f"Your BMI is {BMI}, You are clinically obese. ")'''


# classwork two--- leap year exercise
# write a program that works out whether if a given year is a leap year.
# i.e ON every year that is evenly divisible by 4, it is a leap year, EXCEPT every year that is evenly divisible by 100 is not a leap year
# UNLESS the year is also evenly divisible by 400 it is a leap year.
# solution
'''year = int(input("which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("leap year!")
    else:
      print("not a leap year!")
  else:
    print("leap year!")
else:
  print("not a leap year!")'''

# multiple IF statement-- 
# e.g
'''print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("what is your age: "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? yes or no. ")
  if wants_photo == "yes":
    # add $3 to their bill 
    bill += 3
  print(f"Your Total bill is {bill}")

else:
  print("sorry, you have to grow taller before you can ride.")'''



# exercise-- pizza order pratice
# write a program to ask the user what size they want and also some stuffs in ordering a pizza and at the end display their final bill
# solution
'''print("welcome to Mega pizza deliveries!!")
size = input("what size pizza do you want?\n\tS, M, L\n\t")
add_pepperoni = input("Do you want pepperoni?\n\tY or N\n\t")
extra_cheese = input("Do you want extra cheese?\n\tY or \n\t")
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your Total bill is ${bill}.")'''

#  logical operators--- 'AND', 'OR' 'NOT'
# e.g
'''print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("what is your age: "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <=55:
    print("Everything is going to be ok,you can have a free ride.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? yes or no. ")
  if wants_photo == "yes":
    # add $3 to their bill 
    bill += 3
  print(f"Your Total bill is {bill}")

else:
  print("sorry, you have to grow taller before you can ride.")'''


# exercise---
# write a program that tests the compatibility between two people i.e LOVE CALCULATOR
'''print("Welcome!, to the Love calculator")
name1 = input("what is your name?\n")
name2 = input("what is your partner's name?\n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print(f"your love score is {love_score}\t\n you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"your love score is {love_score}\t\n you are alright together.")
else:
  print(f"your love score is {love_score}")'''


# project exercise Treasure island

# MY WORK
'''print("Welcome to the Treasure Island\n" + "Your mission is to find the missing Treasure")
print("This is the beginning of your journey")
pathway = input("There are two pathways of which one leads to the Island\n left or Right\n")
new_pathway = pathway.lower()
if new_pathway == "left":
  river = input("you need to cross the river,would you like to 'swim or wait' for a boat?\n")
  new_river = river.lower()
  if new_river == "wait":
    door = input("you've arrive your destination, which colour door are you going to open?\n red, blue or yellow\n")
    new_door = door.lower()
    if new_door == "yellow":
      print("you've found the missing treasure, You Win!!!")
    elif new_door == "red":
      print("you've just open the door of a witch, Game Over XXXX")
    else:
      print("you've been kidnapped by a giant king kong, Game Over XXXX")
  else:
    print("you've been eaten by a giant fish,,, Game Over XXXX")
else:
  print("you've just enter the pathway that reach to the deepest forest, Game Over XXXX")

print("Thanks for your services")'''

#  or
'''print("welcome to Treasure Island.")
print("your mission is to find the Treasure.")
choice1 = input('you\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
  choice2 = input('you\'ve come to a lake. There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
  if choice2 == "wait":
    choice3 = input("you arrive at the island unharmed.\nThere is a house with three doors, one red, one blue and one yellow.\nWhich colour do you choose?\n").lower()
    if choice3 == "red":
      print("it a room full of fire,\nGame Over!!!")
    elif choice3 == "yellow":
      print("you found the Treasure,\nYou Win !!!")
    elif choice3 == "blue":
      print("you enter a room of wolves,\nGame Over XXXX")
    else:
      print("you choose a door that doesn't exist,\nGame Over !!!!!!!")
  else:
    print("you got attacked by an angry trout.\nGame Over.")
else:
  print("you fell into a hole.\nGame Over.")'''




# Day 4
# Randomisation and Python Lists

# Randomisation--always use in numbers generator
# e.g
# to use the random module first import it
'''import random'''
# then we use the random integer to set a range of the numbers this is for generation a random whole numbers
'''random_integer = random.randint(1, 10)
print(random_integer)'''

# for generating a random floating numbers
'''random_float = random.random()'''
# it returns floating numbers from 0.0 to 1.0

'''print(random_float)'''

# How to create a random decimal number from 0 to 5
#  just multiply the random_float by 5 to be in the range of 0 and 5
'''print(random_float * 5)'''


# exercise
# write a virtual coin toss program that randomly tell the user "Heads" or "Tails" by using the random module
'''import random
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")'''


# Lists
# split()--it allows you to split a string into separate component base on some sort of divider

# exercise
# write a python program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill
'''import random
test_seed = int(input("Create a seed number:"))
random.seed(test_seed)'''
# split string method
'''names = input("Give me everybody's names separated by a comma\n")
name = names.split(", ")'''
# get the total number of items in the list
'''num_of_items = len(name)'''
# Generate random numbers between 0 and the last index
'''random_choice = random.randint(0, num_of_items - 1)
person_to_pay = name[random_choice]
print(f"{person_to_pay} is going to buy the meal today!.")'''  

# exercise -- Treasure map
# write a python program which will mark a spot with an X
'''row1 = ["+", "+", "+"]
row2 = ["*", "*", "*"]
row3 = ["#", "#", "#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")'''

'''#programming on rock paper scissor game--
import random

rock = '''
     ______
 ---'   ___)
       (____)
       (____)
       (___)
 ---.__(__)
 '''

paper = '''
     ______
 ---'  ____)____
          ______)
          _______)
          ______)
 ---._________)
 '''

scissors = '''
    ______
 ---'  ___)____
         ______)
      __________)
      (___)
 ---.__(__)
 '''

game_images = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
   print("you typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
   print("You win!")
elif computer_choice == 0 and user_choice == 2:
   print("You lose!") 
elif user_choice > computer_choice:
   print("You win!")
elif computer_choice > user_choice:
   print("you lose!")
elif computer_choice == user_choice:
   print("it's a Draw")'''


  


# Day 5----
# concept of loops--

# FOR LOOP--
# e.g
'''fruits = ["Apple", "strawberry", "Grape"]
for fruit in fruits:
   print(fruit)
   print(fruit + "pie")'''

# exercise
# Average Height Exercise
#  write a program that calculate the average student height from a list of heights.
'''student_height = input("Input a list of student heights ").split()
for n in range (0, len(student_height)):
  student_height[n] = int(student_height[n])
total_heights = 0
for height in student_height:
  total_heights += height
print(total_heights)


number_of_student = 0
for student in student_height:
  number_of_student += 1
print(number_of_student)

average_height = round(total_heights / number_of_student)
print(average_height)'''

# write a program that calculates the highest score from a list of scores
'''student_scores = input("Input a list of students scores")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)'''

# Using 'for' loop with the 'range' function
'''for number in range(1, 10):
    print(number)'''

# also for step by a particular number within the range
'''for number in range(1, 11, 3):
    print(number)'''

# Then for addition i.e adding them together using the 'for' loop and the 'range' function
'''total = 0
for number in range(1, 101):
    total += number
print(total)'''

#ADDING EVENS EXERCISE
#Calculate the sum of all the even numbers from 1 to 100 including 1 and 100
'''total = 0
for number in range(2, 101, 2):
    total += number
print(total)'''
# OR
'''total_2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_2 += number
print(total_2)'''

# FIZZ BUZZ EXERCISE
 # write a program that automatically prints the solution to the fizz buzz game 

'''for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
      print(number)'''

# Pypassword generator exercise
# Write a program that genarate password for you that no one can hack into it

'''import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '/', '+', '()']

print("Welcome to pypassword generator")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input(f"How many symbol would you like in your password?\n"))
nr_numbers = int(input(f"How many number would you like in your password?\n"))'''

#EASY LEVEL/WAYS
'''password = ""

for char in range(1, nr_letter + 1):
    password += random.choice(letters)

for char in range(1, nr_symbol + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)'''

#Hard Level/Ways
'''password_list = []

for char in range(1, nr_letter + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbol + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")'''



# DAY 6
# FUNCTIONS--- WHILE LOOPS AND CODE BLOCKS

# PYTHON FUNCTIONS---- 
# Built in functions---- These are functions that are built-in E.G len() Print() and so on
# Defining Functions --
'''def my_function():
    print("Hello world")
    print("God is great")
    print("Wonderful God")'''

#Calling the Function
'''my_function()'''

#Using the Reeborg's world0---
'''# Search for Reeborg's world on the internet--
Under Reeborg's basic keyboard example of functions----''' 
'''move(), turn_left(), take(), put(), toss(), build_wall(), pause(), done(), think(100)'''

#WHILE LOOP---this loop is use when something is true and you want it to do that thing repeatedly 
#----------and if the something never becomes false then the while loop becomes an 'Infinite loop'
# example on Infinite Loop----
'''while 5 > 3:''' 

#For Loop---For loop are great when you want to literate over something and you need to do a thing which each thing you are literating.e.g
'''fruits= ["Apple", "Pear", "Orange"]
for fruit in fruits:
    print(fruit)'''
#OR
'''for n in range(1, 6):
    print(n)'''


#Day 7--

