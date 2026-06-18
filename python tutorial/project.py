from tkinter import *
window = Tk()
window.geometry("500x300")

def getvals():
    print("Accepted")

title = Label(window, text="REGISTRATION FORM", font="ar 15 bold").grid(row=0, column=3)

name = Label(window, text="Full Name")
phone = Label(window, text="Phone Number")
gender = Label(window, text="Gender")
age = Label(window, text="Age")
occupation = Label(window, text="Occupation")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
occupation.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
agevalue = StringVar
occupationvalue = StringVar
checkvalue = IntVar

nameentry = Entry(window, textvariable=namevalue, width=40)
phoneentry = Entry(window, textvariable=phonevalue)
genderentry = Entry(window, textvariable=gendervalue)
ageentry = Entry(window, textvariable=agevalue)
occupationentry = Entry(window, textvariable=occupationvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
occupationentry.grid(row=5, column=3)

checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)


Button(text="Submit", command=getvals).grid(row=7, column=3)

window.mainloop()