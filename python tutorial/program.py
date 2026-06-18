# program to create a user full details #profile
from pp import First_Name


first_name = input("your first name?\n")
middle_name = input("your middle name?\n")
last_name = input("your last name?\n")

gender = input("your gender?\n")

user = input("what year were you born?: ")
current_year = input("enter your current year?: ")
user_year = int(user)
current_new_year = int(current_year)
user_age = current_new_year - user_year
user_new_age = str(user_age)

complexion = input("your complexion?\n")
state_of_origin = input("your state of origin\n")
nationality = input("your nationality\n")
religion = input("what's your religion?\n")
father_name = input("father's name\n")
mother_name = input("mother's name\n")
genotype = input("your genotype?\n")
new_genotype = (genotype.upper())
bloodgroup = input("your bloodgroup?\n")
weight = input("enter your weight in kg\n")
height = input("enter your height in M\n")
marital_status = input("what's your marital status?\n")

occupation = input("what's your occupation?\nStudent?, Yes/No\n")
new_occupation = (occupation.lower())

user_age_in_thirty_years = input("do you like to know your new age in the next thirty years?\n")

user_full_name = print("your name is:" + first_name + " "  + middle_name + " " + last_name)
Age = print("you are " + user_new_age + " years")
user_complexion = print(f"{first_name} is {complexion} in complexion")
user_state = print(f"{first_name} is from {state_of_origin} state, {nationality}")
user_religion = print(f"{first_name} is a {religion}")
user_background = print(f"{first_name} is born in the family of Mr and Mrs {father_name}")
user_bloodgroup_and_genotype = print(f"{first_name} has {bloodgroup} as bloodgroup and {genotype} as Genotype")

if new_genotype == "SS":
   print(f"{first_name} is a sickle cell patient")

elif new_genotype == "AA":
   print(f"{first_name} is an healthy person")

elif new_genotype == "AS":
   print(f"{first_name} is realiable to sickness if not careful")

# else:
#    print("genotype not known")


if new_occupation == "yes":
    n_occupation = print(f"{first_name} is a student")
else:
    new_new_occupation = input("what's your present occupation?\n")
    occupation_new = print(f"{first_name}, you work as a/an {new_new_occupation}.")



BMI = int(weight) / float(height) ** 2
BMI_as_int = int(BMI)
new_BMI = str(BMI_as_int)
user_BMI = print(f"{last_name}, your Body Mass Index is {new_BMI}")
user_popularity = print(f"{last_name} is {marital_status}")

if marital_status == "married":   
    marital_new = input("who is your spouse?\n")
    new_status = print(f"{marital_new} is {last_name} spouse" )
else:
    print(f"{first_name} is not married")


user_age_age = user_age + 30
user_new_age_in_thirty = str(user_age_age)
user_ages = f"{first_name}, your age in the next thirty years is {user_new_age_in_thirty}"

if user_age_in_thirty_years == "yes":
    print(user_ages)
elif user_age_in_thirty_years == "no":
    print("okay")
else:
    print("can't recornise")

