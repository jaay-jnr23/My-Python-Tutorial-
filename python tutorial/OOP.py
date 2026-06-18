# OBJECT_ORIENTED PROGRAMMING--
'''A class is a pin point in creating an object''' 

# OOP means using python to create a representation of real world thing
# An object is a container of data and behaviour
# attributes define an object's state or internal data.
# attributes can be viewed as variables belonging to an object
# method can be viewed as a function belonging to an object
# a method can interact with and modify the object's attributes, thus altering its state
# class is a blueprint for defining a new object type in python 
# a class definition describes the attributes and methods that each object made from the class will have.
# a class can be used to create new objects
# instance is an object created from a class. the act of creating an instance is called instantiation
# object created from the same class are independent of each other.
'''class Person:
    pass

# objects
person_1 = Person()
person_2 = Person()
print(person_1)
print(person_2)'''

# creating a class function is a type
# methods is define on object

# examples
'''class Guitar:
    pass
acoustic = Guitar()
electric = Guitar()

# define attributes
acoustic.strings = 6
acoustic.year = 1996
acoustic.wood = "mahogany"

print(acoustic.wood)
print(acoustic.year)
print(acoustic.strings)'''

# to make it work for also electric. part --- we use in the def function..
'''class Guitar:
    def __init__(self):
        self.wood = "mahogany"
        self.year = 1996
        self.strings = 6
acoustic = Guitar()
electric = Guitar()

# define attributes
acoustic.strings = 6
acoustic.year = 1996
acoustic.wood = "mahogany"

print(acoustic.wood)
print(acoustic.year)
print(acoustic.strings)

print(electric.wood)
print(electric.year)
print(electric.strings)'''

# to pass in attributes and parameters--
'''class Guitar:
    def __init__(self,wood, year, strings):
        self.wood = wood
        self.year = year
        self.strings = strings
acoustic = Guitar("mahogany", 1996, 6)
electric = Guitar("popular", 2000, 5)

# define attributes

print(acoustic.wood)
print(acoustic.year)
print(acoustic.strings)

print(electric.wood)
print(electric.year)
print(electric.strings)'''

# task 1
# design a python chcekout system for a bookshop. give it the appropriate attributes
# 7mins

'''class Bookshop:
    def __init__(self,name, time, purchased):
        self.name = name
        self.time = time
        self.purchased = purchased
buyer_1 = Bookshop("Samuel Bamidele", "2:00pm", "Pencil")
buyer_2 = Bookshop("Emmanuel ezekiel", "4:56pm", "storybooks")
buyer_3 = Bookshop("Ola Port", "3:45pm", "A4-paper")

print(buyer_1.name)
print(buyer_1.time)
print(buyer_1.purchased)

print(buyer_2.name)
print(buyer_2.time)
print(buyer_2.purchased)

print(buyer_3.name)
print(buyer_3.time)
print(buyer_3.purchased)'''


# classwork---
# imagine the price of a book is fixed i.e the price is the same for all objects to be created
'''class Book:
    def __init__(self,name, section):
        self.name = name
        self.price = 100
        self.section = section

book_1 = Book("100 ways to Grow", "Age 4-6")
book_2 = Book("secondary school textbooks", "Age 9-13")
book_3 = Book("senior secondary school textbooks", "Age 14-19")
book_4 = Book("Notebooks", "All students")

print(book_1.name)
print(book_1.price)
print(book_1.section)

print(book_2.name)
print(book_2.price)
print(book_2.section)

print(book_3.name)
print(book_3.price)
print(book_3.section)

print(book_4.name)
print(book_4.price)
print(book_4.section)'''

# assume discount is given on specific books. e.g some 100 other 120
'''class Book:
    def __init__(self, name, section, price=120):
        self.name = name
        self.price = price
        self.section = section

book_1 = Book(name="100 ways to Grow", section="Age 4-6", price=100)
book_2 = Book(name="secondary school textbooks", section="Age 9-13", price=50)
book_3 = Book(name="senior secondary school textbooks", section="Age 14-19", price=80)
book_4 = Book(name="Notebooks", section="All students")

print(book_1.name)
print(book_1.price)
print(book_1.section)

print(book_2.name)
print(book_2.price)
print(book_2.section)

print(book_3.name)
print(book_3.price)
print(book_3.section)

print(book_4.name)
print(book_4.price)
print(book_4.section)'''
# represent both using the OOP

# 27/04/2022
# classwork
# using the desc() method under the def function print something like---
'''class Book:
    def __init__(self, name, section, year, price="120"):
        self.name = name
        self.price = price
        self.section = section
        self.year = year

    def desc(self):
        print(f"{self.name}, was created in the year {self.year}, avialable for {self.section}, price is {self.price}")

book_1 = Book(name="100 ways to Grow", section="Age 4-6", year="1999", price="100")
book_2 = Book(name="Love is blind", section="Age 9-13", year="1996", price="50")
book_3 = Book(name="The gods are not to be blame", section="Age 14-19", year="2004", price="80")
book_4 = Book(name="The lost treasure", section="All students", year="2000")

print(book_1.name)
print(book_1.price)
print(book_1.section)
book_1.desc()

print(book_2.name)
print(book_2.price)
print(book_2.section)
book_2.desc()

print(book_3.name)
print(book_3.price)
print(book_3.section)
book_3.desc()

print(book_4.name)
print(book_4.price)
print(book_4.section)
book_4.desc()'''


# also using the discount() method
'''class Book:
    def __init__(self, name, section, year, price=120):
        self.name = name
        self.price = price
        self.section = section
        self.year = year

    def desc(self):
        print(f"{self.name}, was created in the year {self.year}, avialable for {self.section}, price is {str(self.price)}")

    def discount(self):
        rate = 0.1
        new_price = self.price * rate
        print(f"{self.name}, is now sold for {str(new_price)}")

book_1 = Book(name="100 ways to Grow", section="Age 4-6", year="1999", price=100)
book_2 = Book(name="Love is blind", section="Age 9-13", year="1996", price=50)
book_3 = Book(name="The gods are not to be blame", section="Age 14-19", year="2004", price=80)
book_4 = Book(name="The lost treasure", section="All students", year="2000")

print(book_1.name)
print(book_1.price)
print(book_1.section)
book_1.desc()
book_1.discount()

print(book_2.name)
print(book_2.price)
print(book_2.section)
book_2.desc()
book_2.discount()

print(book_3.name)
print(book_3.price)
print(book_3.section)
book_3.desc()
book_3.discount()

print(book_4.name)
print(book_4.price)
print(book_4.section)
book_4.desc()
book_4.discount()'''

# Classwork---
# Using OOP write a python program to simulate a bank transaction application.

'''class Bank:
    def __init__(self, name, deposit, withdrawn, balance, time, date_deposit, date_withdrawn, acc_number):
        self.name = name
        self.acc_number = acc_number
        self.deposit = deposit
        self.date_deposit = date_deposit
        self.withdrawn = withdrawn
        self.date_withdrawn = date_withdrawn
        self.balance = balance
        self.time = time 

    def desc(self):
        print(f"welcome!!\n {self.name}, your account number is {self.acc_number}\n you made a deposit of {self.deposit} naira as at {self.date_deposit}\n Made a withdrawn of {self.withdrawn} naira as at {self.date_withdrawn}\n you now have a balance of {self.balance} naira\n {self.time}.\n Thanks for your services with us, remember we love you.")


customer_1 = Bank(name="Mr Mustapher Muhammed", acc_number="3477289", deposit="Two Million", withdrawn="Five Hundred Thousands", balance="3.5 Million", date_deposit="09/11/2012", date_withdrawn="11/11/2012", time="2:00pm" )
customer_2 = Bank(name="Mr Ali Yusuf", acc_number="0466732", deposit="Fourteen Thousands", withdrawn="Nine Thousands", balance="Six Hundred and Thirty-one Thousands", date_deposit="13/04/2019", date_withdrawn="16/05/2019", time="3:45pm")
customer_3 = Bank(name="Mrs Kehinde Seun", acc_number="0445632", deposit="Four Thousands", withdrawn="Ten Thousands", balance="Thirty Million", date_deposit="08/09/2020", date_withdrawn="11/12/2020", time="12:30pm")
customer_4 = Bank(name="Mr Sanusi salmar", acc_number="455637645", deposit="Fifteen Thousands", withdrawn="Five Thousands", balance="Ten Million", date_deposit="09/02/2024", date_withdrawn="11/02/2024", time="11:15am")
customer_5 = Bank(name="Mr Muhammed Issa", acc_number="223453332", deposit="Ten Million naira", withdrawn="Five million Naira only", balance="Hundred Million Naira", date_deposit="10/02/2024", date_withdrawn="15/02/2024",time="10:00pm")

customer_1.desc()
customer_2.desc()
customer_3.desc()
customer_4.desc()
customer_5.desc()'''

# 4/05/2022
# INHERITANCE:
# Child class/sub class/base class---is a type of super class, that recieve attributes from another class while 
# The Parent class/Super class--is a type of class that distribute attributes to a sub class/the child class
# e.g
'''class Shop:
    def __init__(self):
        self.owner = "Bayo"
        self.location = "ilorin"
        self.staff = 10
    
    def desc(self):
        print(f"{self.owner} is the owner of the shop located at {self.location} and has {self.staff} staff")

class CoffeeShop(Shop):
    pass

shop_1 = CoffeeShop()
shop_1.desc()'''

# If the sub class/child class has an attribute there is no need for it to print the attributes under the the parent class--
# e.g
'''class Shop:
    def __init__(self):
        self.owner = "Bayo"
        self.location = "ilorin"
        self.staff = 10
    
    def desc(self):
        print(f"{self.owner} is the owner of the shop located at {self.location} and has {self.staff} staff")

class CoffeeShop(Shop):
    def __init__(self):
        self.owner = "Dayo"
        self.location = "Kano"
        self.staff = 20
    
    def desc(self):
        print(f"Mr {self.owner} owns a coffee shop in {self.location} and he has {self.staff} staff")

shop_1 = CoffeeShop()
shop_1.desc()'''




# POLYMORPHISM-- this let us define methods in the child class that have the same name as the methods in the parent class.
# e.g
'''class Bird:
    def intro(self):
        print("There are many types of birds. ")

    def flight(self):
        print("Most of the birds can fly but some cannot. ")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly. ")

class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly. ")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()'''

# Implementing Polymorphism with a function--
'''class India():
    def capital(self):
        print("New Delhi is the capital of India. ")
    
    def language(self):
        print("Hindi is the most widely spoken language of India. ")

    def type(self):
        print("India is a developing country. ")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA. ")

    def language(self):
        print("English is the primary language of USA. ")

    def type(self):
        print("USA is a developing country. ")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)'''

