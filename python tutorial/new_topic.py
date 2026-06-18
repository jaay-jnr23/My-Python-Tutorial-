'''from tkinter import *
window = Tk()'''
# labels
# fg--foreground color is just like the background color
# bg---background color.

# using the pack() method--
'''label_1 = Label(window, text="hello world", fg="blue", bg="white" ).pack()
label_2 = Button(window, text="welcome", fg="white", bg="orange").pack()
label_4 = Entry(window, text="hello world").pack()

text = Text(window, height=20, width=20).pack()'''

# using the plac() method--
'''label_1 = Label(window, text="hello world", fg="blue", bg="white" ).place(x=10, y=10)
text = Text(window, height=20, width=20).place(x=10, y=10)'''


'''window.mainloop()'''


# classwork-- create a registration form
import tkinter
from ast import Delete
from distutils.log import info
from sqlite3 import connect
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
import pymysql

window = tkinter.Tk()
window.configure(bg="blue")
window.geometry("1500x1500")

def delete(id):
    x = messagebox.askquestion("wait", 'do you want to delete user?')
    if x == 'yes':
        delete_con = pymysql.connect(host="localhost", user="root", password="", db="juwon")
        mycursor = delete_con.cursor()
        msg = "delete from jay where id = {}"
        delete_query = msg.format(id)
        mycursor.execute(delete_query)
        delete_con.commit()
    messagebox.showinfo("success", "user deleted")

# using messagebox--
def register():
    press = messagebox.askquestion("wait", "do you want to create an account")
    if press == "yes":
        label_0 = entry_1.get()
        label_1 = entry_2.get()
        label_2 = entry_3.get()
        label_3 = entry_4.get()
        label_4 = entry_5.get()

        if  label_0 == "":
             messagebox.showerror("error", "Enter First Name")
        elif label_1 == "":
            messagebox.showerror("error", "Enter Middle Name")
        elif label_2 == "":
            messagebox.showerror("error", "Enter Last Name")
        elif label_3 =="":
            messagebox.showerror("click your Gender")
        elif label_4 =="":
            messagebox.showerror("error", "Enter your Age")
        else:
            messagebox.showinfo("done")

# connect to mysql
        connect_register = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="juwon"
        )

        # connect a cursor
        my_cursor = connect_register.cursor()

        # create a query
        text = "INSERT INTO jay VALUES ('', '{}', '{}', '{}', '{}', '{}')"
        done = text.format(label_0, label_1, label_2, label_3, label_4)


        # execute a query
        my_cursor.execute(done)


        connect_register.commit()
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        messagebox.showinfo("Registration successful")

def User_list():
    User_list = tkinter.Tk()
    User_list.geometry("1200x1200")
    User_list.title("jay")
    User_list.configure(bg="grey")

# connect to database 
    connect = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="juwon"
    )
# create a cursor--
    my_new_cursor = connect.cursor()
    query = "SELECT * FROM jay"
    my_new_cursor.execute(query)
    Users = my_new_cursor.fetchall()

# create the heading
    id = Label(User_list, text="ID", width=0, font=("bold", 10)).grid(row=0, column=0)
    label_0 = Label(User_list, text="First Name", width=20, font=("bold", 10)).grid(row=0, column=1)
    label_1 = Label(User_list, text="Middle Name", width=20, font=("bold", 10)).grid(row=0, column=2)
    label_2 = Label(User_list, text="Last Name", width=20, font=("bold", 10)).grid(row=0, column=3)
    label_3 = Label(User_list, text="Gender", width=15, font=("bold", 10)).grid(row=0, column=4)
    label_4 = Label(User_list, text="Age", width=10, font=("bold", 10)).grid(row=0, column=5)
    Edit = Label(User_list, text="Edit", width=10, font=("bold", 10)).grid(row=0, column=6)
    Delete = Label(User_list, text="Delete", width=10, font=("bold", 10)).grid(row=0, column=7)


    row_count = 1
    column_count = 0

    for i in Users:
        id = Label(User_list, text=i[0], width=0, font=("bold", 10)).grid(row=row_count, column=column_count)
        label_0 = Label(User_list, text=i[1], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 1)
        label_1 = Label(User_list, text=i[2], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 2)
        label_2 = Label(User_list, text=i[3], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 3)
        label_3 = Label(User_list, text=i[4], width=15, font=("bold", 10)).grid(row=row_count, column=column_count + 4)
        label_4 = Label(User_list, text=i[5], width=10, font=("bold", 10)).grid(row=row_count, column=column_count + 5)
        Edit = Button(User_list, text="Edit", width=10, font=("bold", 10), command=lambda id=i[0]: edit(id)).grid(row=row_count, column=column_count + 6)
        Delete = Button(User_list, text="Delete", width=10, font=("bold", 10), command=lambda id=i[0]: delete(id)).grid(row=row_count, column=column_count + 7)


        row_count += 1
        connect.commit()



def edit(id):
    edit = tkinter.Tk()
    edit.geometry("1500x1000")
    edit.title("Edit")


# connect to database
    connect_edit = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="juwon"
    )   
# create a cursor
    new_cursor = connect_edit.cursor()

# write a query
    new_query = "SELECT * FROM jay WHERE id={}"
    new_text=new_query.format(id)
    new_cursor.execute(new_text)
    users = new_cursor.fetchall()
    print(users)


    def save():
        connect_save = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="juwon"
        )

        save_cursor = connect_save.cursor()
        save_query =  "update jay set label_0=%s, label_1=%s, label_2=%s, label_3=%s, label_4=%s where id=%s"
        id = lab_0.get()
        label_0 = lab_1.get()
        label_1 = lab_2.get()
        label_2 = lab_3.get()
        label_3 = lab_4.get()
        label_4 = lab_5.get()
        

        input=(label_0, label_1, label_2, label_3, label_4, id)
        save_cursor.execute(save_query,input)
        connect_save.commit()
        edit.destroy()

    lab = Label(edit, text="UPDATE USER", font=(BOLD, 20), foreground='red')
    lab.place(x=100, y=20)

 # labels on edit
    id = Label(edit, text="ID", width=10, font=(BOLD, 10))
    id.place(x=80, y=80)
    lab_0 = Entry(edit)
    lab_0.place(x=250, y=80)
    lab_0.insert(0, users[0][0])

    label_0 = Label(edit, text="First Name", width=20, font=(BOLD, 10))
    label_0.place(x=80, y=130)
    lab_1 = Entry(edit)
    lab_1.place(x=250, y=130)
    lab_1.insert(0, users[0][1])

    label_1 = Label(edit, text="Middle Name", width=20, font=(BOLD, 10))
    label_1.place(x=80, y=180)
    lab_2 = Entry(edit)
    lab_2.place(x=250, y=180)
    lab_2.insert(0, users[0][2])


    label_2 = Label(edit, text="Last Name", width=20, font=(BOLD, 10))
    label_2.place(x=80, y=230)
    lab_3 = Entry(edit)
    lab_3.place(x=250, y=230)
    lab_3.insert(0, users[0][3])

    label_3 = Label(edit, text="Last Name", width=20, font=(BOLD, 10))
    label_3.place(x=80, y=280)
    lab_4 = Entry(edit)
    lab_4.place(x=250, y=280)
    lab_4.insert(0, users[0][4])

    label_4 = Label(edit, text="Gender", width=20, font=(BOLD, 10))
    label_4.place(x=80, y=330)
    lab_5 = Entry(edit)
    lab_5.place(x=250, y=330)
    lab_5.insert("end", users[0][5])


    save_button = Button(edit, text="Save", padx=10, pady=5, command=save, background="blue", foreground="white")
    save_button.place(x=200, y=550)

# labels on window
label = Label(window, text="Registration Form", font=(BOLD, 14)).place(x=60, y=10)

label_0 = Label(window, text="First Name")
label_0.place(x=80, y=53)
entry_1 = Entry(window)
entry_1.place(x=180, y=55)

label_1 = Label(window, text="Middle Name")
label_1.place(x=80, y=130)
entry_2 = Entry(window)
entry_2.place(x=180, y=135)


label_2 = Label(window, text="Last Name")
label_2.place(x=80, y=200)
entry_3 = Entry(window)
entry_3.place(x=180, y=205)

label_3 = Label(window, text="Gender")
label_3.place(x=80, y=280)
entry_4 = Entry(window)
entry_4.place(x=180, y=280)


label_4 = Label(window, text="Age")
label_4.place(x=80, y=360)
entry_5 = Entry(window)
entry_5.place(x=180, y=365)

button_3 = Button(window, text="Submit", foreground="red", background="white", font=(BOLD, 10), command=register)
button_3.place(x=100, y=400)
button_4 = Button(window, text="List of Users", command=User_list).place(x=200, y=420)
# creating a frame
'''f = Frame(window, width=500, height=500, relief=GROOVE, borderwidth=5)
f.pack(side=RIGHT)
f1= Label(f, text="Hello World", fg="Red",).place(x=50, y=50)'''

window.mainloop()


# 10/05/2022
# how to use a function in tkinter---
'''from tkinter import *
window = Tk()

def register():
    label = Label(window, text="hello").pack()
register()


window.mainloop()'''





