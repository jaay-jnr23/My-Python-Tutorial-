# profile 
from collections import UserList
from importlib.metadata import entry_points
from ast import Delete
from distutils.log import info
from sqlite3 import connect
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from tokenize import Name
from unicodedata import name
from xml.dom import UserDataHandler
import pymysql
from setuptools import Command

window = Tk()
window.configure(bg="#304050")
window.geometry("1500x1500")


def delete(id):
    y = messagebox.askquestion("Wait", 'Delete User?')
    if y == 'yes':
        connect_delete = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="project"
        )
        new = connect_delete.cursor()
        query_new = "delete from views where id={}"
        text =query_new.format(id)
        new.execute(text)
        connect_delete.commit()
    messagebox.showinfo("user successfully deleted")

def Register():
    y = messagebox.askquestion("Create a Profile?")
    if y == "yes":
        First_Name = entry_1.get()
        Middle_Name = entry_2.get()
        Last_Name = entry_3.get()
        Gender = entry_4.get()
        Year_Born = entry_5.get()
        Current_Year = entry_6.get()
        Complexion = entry_7.get()
        State_of_Origin = entry_8.get()
        Nationality = entry_9.get()
        Religion = entry_10.get()
        Father_Name = entry_11.get()
        Mother_Name = entry_12.get()
        Genotype = entry_13.get()
        Blood_Group = entry_14.get()
        Weight = entry_15.get()
        Height = entry_16.get()
        Occupation = entry_17.get()
        Marital_Status = entry_18.get()

        if First_Name == "":
            messagebox.showerror("Error", "First Name")
        elif Middle_Name == "":
            messagebox.showerror("Error", "Middle Name")
        elif Last_Name == "":
            messagebox.showerror("Error", "Last Name")
        elif Gender == "":
            messagebox.showerror("Error", "Your Gender?")
        elif Year_Born == "":
            messagebox.showerror("Error", "Year Born")
        elif Current_Year == "":
            messagebox.showerror("Error", "Current Year?")
        elif Complexion == "":
            messagebox.showerror("Error", "Your Complexion")
        elif State_of_Origin == "":
            messagebox.showerror("Error", "What's your state of origin?")
        elif Nationality == "":
            messagebox.showerror("Error", "your Nationality")
        elif Religion == "":
            messagebox.showerror("Error", "your Religion?")
        elif Father_Name == "":
            messagebox.showerror("Error", "Your Father's Name?")
        elif Mother_Name == "":
            messagebox.showerror("Error", "Your Mother's Name")
        elif Genotype == "":
            messagebox.showerror("Error", "Your Genotype?")
        elif Blood_Group == "":
            messagebox.showerror("Error", "Blood Group")
        elif Weight == "":
            messagebox.showerror("Error", "Weight!!")
        elif Height == "":
            messagebox.showerror("Error", "Height!!")
        elif Occupation == "":
            messagebox.showerror("Error", "Your Occupation?")
        elif Marital_Status == "":
            messagebox.showerror("Error", "Your Marital Status?")
        else:
            messagebox.showinfo("sucessfull!")
        connect_reg = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            database= "project"
        )

        my_cursor = connect_reg.cursor()

        text = "INSERT INTO views VALUES ('', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
        done = text.format(First_Name, Middle_Name, Last_Name, Gender, Year_Born, Current_Year, Complexion, State_of_Origin, Nationality, Religion, Father_Name, Mother_Name, Genotype, Blood_Group, Weight, Height, Occupation, Marital_Status)

        my_cursor.execute(done)
        connect_reg.commit()
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)
        entry_7.delete(0, END)
        entry_8.delete(0, END)
        entry_9.delete(0, END)
        entry_10.delete(0, END)
        entry_11.delete(0, END)
        entry_12.delete(0, END)
        entry_13.delete(0, END)
        entry_14.delete(0, END)
        entry_15.delete(0, END)
        entry_16.delete(0, END)
        entry_17.delete(0, END)
        entry_18.delete(0, END)
        messagebox.showinfo("Profile Noted")

def List_of_users():
    List_of_users = Tk()
    List_of_users.geometry("1500x1500")
    List_of_users.title("project views")
    List_of_users.configure(bg="grey")

    connect = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )
    new_cursor = connect.cursor()
    query = "SELECT * FROM views"
    new_cursor.execute(query)
    Users = new_cursor.fetchall()
    
    id = Label(List_of_users, text="ID", width=0, font=(BOLD, 10)).grid(row=0, column=0)
    First_Name = Label(List_of_users, text="First Name", width=10, font=(BOLD, 10)).grid(row=0, column=1)
    Middle_Name = Label(List_of_users, text="Middle Name", width=10, font=(BOLD, 10)).grid(row=0, column=2)
    Last_Name = Label(List_of_users, text="Last Name", width=10, font=(BOLD, 10)).grid(row=0, column=3)
    Gender = Label(List_of_users, text="Gender", width=5, font=(BOLD, 10)).grid(row=0, column=4)
    Year_Born = Label(List_of_users, text="Year-B", width=8, font=(BOLD, 10)).grid(row=0, column=6)
    Current_Year = Label(List_of_users, text="C-Year", width=8, font=(BOLD,10)).grid(row=0, column=7)
    Complexion = Label(List_of_users, text="Complexion", width=8, font=(BOLD, 10)).grid(row=0, column=8)
    State_of_Origin = Label(List_of_users, text="S-O", width=10, font=(BOLD, 10)).grid(row=0, column=9)
    Nationality = Label(List_of_users, text="nationality", width=10, font=(BOLD, 10)).grid(row=0, column=10)
    Religion = Label(List_of_users, text="Religion", width=10, font=(BOLD, 10)).grid(row=0, column=11)
    Father_Name = Label(List_of_users, text="F-N", width=10, font=(BOLD, 10)).grid(row=0, column=12)
    Mother_Name = Label(List_of_users, text="M-N", width=10, font=(BOLD, 10)).grid(row=0, column=13)
    Genotype = Label(List_of_users, text="G-T", width=5, font=(BOLD, 10)).grid(row=0, column=14)
    Blood_Group = Label(List_of_users, text="B-G", width=5, font=(BOLD, 10)).grid(row=0, column=15)
    Weight = Label(List_of_users, text="weight", width=5, font=(BOLD, 10)).grid(row=0, column=16)
    Height = Label(List_of_users, text="height", width=5, font=(BOLD, 10)).grid(row=0, column=17)
    Occupation = Label(List_of_users, text="O-P", width=6, font=(BOLD, 10)).grid(row=0, column=18)
    Marital_Status = Label(List_of_users, text="M-S", width=6, font=(BOLD, 10)).grid(row=0, column=19)
    Edit = Label(List_of_users, text="Edit", width=5, font=(BOLD, 10)).grid(row=0, column=20)
    Delete = Label(List_of_users, text="Delete", width=5, font=(BOLD, 10)).grid(row=0, column=21)
    
    row_count = 1
    column_count = 0

    for h in Users:
        id = Label(List_of_users, text=h[0], width=0, font=(BOLD, 10)).grid(row=row_count, column=column_count)
        First_Name = Label(List_of_users, text=h[1], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 1)
        Middle_Name = Label(List_of_users, text=h[2], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 2)
        Last_Name = Label(List_of_users, text=h[3], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 3)
        Gender = Label(List_of_users, text=h[4], width=5, font=(BOLD, 10)).grid(row=row_count, column=column_count + 4)
        Year_Born = Label(List_of_users, text=h[5], width=8, font=(BOLD, 10)).grid(row=row_count, column=column_count + 6)
        Current_Year = Label(List_of_users, text=h[6], width=8, font=(BOLD,10)).grid(row=row_count, column=column_count + 7)
        Complexion = Label(List_of_users, text=h[7], width=8, font=(BOLD, 10)).grid(row=row_count, column=column_count + 8)
        State_of_Origin = Label(List_of_users, text=h[8], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 9)
        Nationality = Label(List_of_users, text=h[9], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 10)
        Religion = Label(List_of_users, text=h[10], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 11)
        Father_Name = Label(List_of_users, text=h[11], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 12)
        Mother_Name = Label(List_of_users, text=h[12], width=10, font=(BOLD, 10)).grid(row=row_count, column=column_count + 13)
        Genotype = Label(List_of_users, text=h[13], width=5, font=(BOLD, 10)).grid(row=row_count, column=column_count + 14)
        Blood_Group = Label(List_of_users, text=h[14], width=5, font=(BOLD, 10)).grid(row=row_count, column=column_count + 15)
        Weight = Label(List_of_users, text=h[15], width=5, font=(BOLD, 10)).grid(row=row_count, column=column_count + 16)
        Height = Label(List_of_users, text=h[16], width=5, font=(BOLD, 10)).grid(row=row_count, column=column_count + 17)
        Occupation = Label(List_of_users, text=h[17], width=6, font=(BOLD, 10)).grid(row=row_count, column=column_count + 18)
        Marital_Status = Label(List_of_users, text=h[18], width=6, font=(BOLD, 10)).grid(row=row_count, column=column_count + 19)
        Edit = Button(List_of_users, text="Edit", width=5, font=(BOLD, 10), command=lambda id=h[0]: edit(id), background="ORANGE").grid(row=row_count, column=column_count + 20)
        Delete = Button(List_of_users, text="Delete", width=5, font=(BOLD, 10), command=lambda id=h[0]: delete(id), background="GREEN").grid(row=row_count, column=column_count + 21)

        row_count += 1
        connect.commit()

def edit(id):
    edit = Tk()
    edit.geometry("1500x1500")
    edit.title("Edit")
    edit.configure(bg="grey")

    connect_edit = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )
    
    cursor_new = connect_edit.cursor()
    new_query = "SELECT * FROM views WHERE ID={}"
    new_text=new_query.format(id)
    cursor_new.execute(new_text)
    new_user = cursor_new.fetchall()
    print(new_user)

    def save():
        connect_save = pymysql.connect(
            host="localhost", 
            user="root", 
            password="", 
            database="project"
            )
        save_cursor = connect_save.cursor()
        save_query = "update views set First_Name=%s, Middle_Name=%s, Last_Name=%s, Gender=%s, Year_Born=%s, Current_Year=%s, Complexion=%s, State_of_Origin=%s, Nationality=%s, Religion=%s, Father_Name=%s, Mother_Name=%s, Genotype=%s, Blood_Group=%s, Weight=%s, Height=%s, Occupation=%s, Marital_Status=%s where id=%s"
        id = label.get()
        First_Name = label_1.get()
        Middle_Name = label_2.get()
        Last_Name = label_3.get()
        Gender = label_4.get()
        Year_Born = label_5.get()
        Current_Year = label_6.get()
        Complexion = label_7.get()
        State_of_Origin = label_8.get()
        Nationality = label_9.get()
        Religion = label_10.get()
        Father_Name = label_11.get()
        Mother_Name = label_12.get()
        Genotype = label_13.get()
        Blood_Group = label_14.get()
        Weight = label_15.get()
        Height = label_16.get()
        Occupation = label_17.get()
        Marital_Status = label_18.get()
        

        input=(First_Name, Middle_Name, Last_Name, Gender, Year_Born, Current_Year, Complexion, State_of_Origin, Nationality, Religion, Father_Name, Mother_Name, Genotype, Blood_Group, Weight, Height, Occupation, Marital_Status, id)
        save_cursor.execute(save_query, input)
        connect_save.commit()
        edit.destroy()

    lab = Label(edit, text="User Update", font=(BOLD, 15), fg="#404040", bg="RED")
    lab.place(x=100, y=20)

    id = Label(edit, text="ID", width=0, font=(BOLD, 10))
    id.place(x=80, y=80)
    label = Entry(edit, width=5)
    label.place(x=100, y=80)
    label.insert(0, new_user[0][0])
    
    First_Name = Label(edit, text="First Name", width=10, font=(BOLD, 10), bg="ORANGE")
    First_Name.place(x=300, y=80)
    label_1 = Entry(edit, width=20)
    label_1.place(x=400, y=80)
    label_1.insert(0, new_user[0][1])

    Middle_Name = Label(edit, text="Middle Name", width=10, font=(BOLD, 10), bg="BLUE")
    Middle_Name.place(x=600, y=80)
    label_2 = Entry(edit, width=20)
    label_2.place(x=700, y=80)
    label_2.insert(0, new_user[0][2])

    Last_Name = Label(edit, text="Last Name", width=10, font=(BOLD, 10), bg="YELLOW")
    Last_Name.place(x=900, y=80)
    label_3 = Entry(edit, width=20)
    label_3.place(x=1000, y=80)
    label_3.insert(0, new_user[0][3])

    Gender = Label(edit, text="Gender", width=5, font=(BOLD, 10), bg="GREEN")
    Gender.place(x=70, y=180)
    label_4 = Entry(edit, width=10)
    label_4.place(x=140, y=180)
    label_4.insert(0, new_user[0][4])

    Year_Born = Label(edit, text="Year Born", width=8, font=(BOLD, 10), bg="PURPLE")
    Year_Born.place(x=300, y=180)
    label_5 = Entry(edit, width=10)
    label_5.place(x=400, y=180)
    label_5.insert(0, new_user[0][5])

    Current_Year = Label(edit, text="Current Year", width=10, font=(BOLD, 10), bg="CYAN")
    Current_Year.place(x=600, y=180)
    label_6 = Entry(edit, width=10)
    label_6.place(x=700, y=180)
    label_6.insert(0, new_user[0][6])

    Complexion = Label(edit, text="Complexion", width=10, font=(BOLD, 10), bg="RED")
    Complexion.place(x=900, y=180)
    label_7 = Entry(edit, width=10)
    label_7.place(x=1000, y=180)
    label_7.insert(0, new_user[0][7])

    State_of_Origin = Label(edit, text="State of Origin", width=10, font=(BOLD, 10), bg="INDIGO")
    State_of_Origin.place(x=80, y=280)
    label_8 = Entry(edit, width=10)
    label_8.place(x=180, y=280)
    label_8.insert(0, new_user[0][8])

    Nationality = Label(edit, text="Nationality", width=10, font=(BOLD, 10), bg="VIOLET")
    Nationality.place(x=300, y=280)
    label_9 = Entry(edit, width=10)
    label_9.place(x=400, y=280)
    label_9.insert(0, new_user[0][9])

    Religion = Label(edit, text="Religion", width=10, font=(BOLD, 10), bg="ORANGE")
    Religion.place(x=600, y=280)
    label_10 = Entry(edit, width=20)
    label_10.place(x=700, y=280)
    label_10.insert(0, new_user[0][10])

    Father_Name = Label(edit, text="Father's Name", width=10, font=(BOLD, 10), bg="BLUE")
    Father_Name.place(x=900, y=280)
    label_11 = Entry(edit, width=20)
    label_11.place(x=1000, y=280)
    label_11.insert(0, new_user[0][11])

    Mother_Name = Label(edit, text="Mother's Name", width=10, font=(BOLD, 10), bg="YELLOW")
    Mother_Name.place(x=80, y=380)
    label_12 = Entry(edit, width=20)
    label_12.place(x=180, y=380)
    label_12.insert(0, new_user[0][12])

    Genotype = Label(edit, text="Genotype", width=8, font=(BOLD, 10), bg="GREEN")
    Genotype.place(x=420, y=380)
    label_13 = Entry(edit, width=8)
    label_13.place(x=500, y=380)
    label_13.insert(0, new_user[0][13])

    Blood_Group = Label(edit, text="Blood Group", width=8, font=(BOLD, 10), bg="WHITE")
    Blood_Group.place(x=700, y=380)
    label_14 = Entry(edit, width=8)
    label_14.place(x=800, y=380)
    label_14.insert(0, new_user[0][14])

    Weight = Label(edit, text="Weight", width=8, font=(BOLD, 10), bg="RED")
    Weight.place(x=1000, y=380)
    label_15 = Entry(edit, width=5)
    label_15.place(x=1100, y=380)
    label_15.insert(0, new_user[0][15])

    Height = Label(edit, text="Height", width=8, font=(BOLD, 10), bg="BLUE")
    Height.place(x=80, y=460)
    label_16 = Entry(edit, width=5)
    label_16.place(x=180, y=460)
    label_16.insert(0, new_user[0][16])

    Occupation = Label(edit, text="Occupation", width=10, font=(BOLD, 10), bg="YELLOW")
    Occupation.place(x=400, y=460)
    label_17 = Entry(edit, width=20)
    label_17.place(x=500, y=460)
    label_17.insert(0, new_user[0][17])

    Marital_Status = Label(edit, text="Marital Status", width=10, font=(BOLD, 10), bg="BROWN")
    Marital_Status.place(x=700, y=460)
    label_18 = Entry(edit, width=15)
    label_18.place(x=800, y=460)
    label_18.insert("end", new_user[0][18])

    save_click = Button(edit, text="SAVE", padx=10, pady=5, command=save, background="blue", foreground="white", width=20)
    save_click.place(x=200, y=530)

def search():
    y= messagebox.askquestion("Search a User?")
    if y == 'yes':
        connect_search = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="project"
        )

        cur = connect_search.cursor()
        sql = "SELECT * FROM views where Middle_Name='%s'"%Middle_Name.get()
        cur.execute(sql)
        result=cur.fetchone()
        First_Name.set(result[1])
        Last_Name.set(result[3])
        Gender.set(result[4])
        Year_Born.set(result[5])
        Current_Year.set(result[6])
        Complexion.set(result[7])
        State_of_Origin.set(result[8])
        Nationality.set(result[9])
        Religion.set(result[10])
        Father_Name.set(result[11])

        
        Mother_Name.set(result[12])
        Genotype.set(result[13])
        Blood_Group.set(result[14])
        Weight.set(result[15])
        Height.set(result[16])
        Occupation.set(result[17])
        Marital_Status.set(result[18])
        entry_1.configure(state='disabled')
        entry_3.configure(state='disabled')
        entry_4.configure(state='disabled')
        entry_5.configure(state='disabled')
        entry_6.configure(state='disabled')
        entry_7.configure(state='disabled')
        entry_8.configure(state='disabled')
        entry_9.configure(state='disabled')
        entry_10.configure(state='disabled')
        entry_11.configure(state='disabled')
        entry_12.configure(state='disabled')
        entry_13.configure(state='disabled')
        entry_14.configure(state='disabled')
        entry_15.configure(state='disabled')
        entry_16.configure(state='disabled')
        entry_17.configure(state='disabled')
        entry_18.configure(state='disabled')
        connect_search.close()

    else:
        messagebox.showinfo('profile search ended...')
        clear()

def clear():
    First_Name.set('')
    Middle_Name.set('')
    Last_Name.set('')
    Gender.set('')
    Year_Born.set('')
    Current_Year.set('')
    Complexion.set('')
    State_of_Origin.set('')
    Nationality.set('')
    Religion.set('')
    Father_Name.set('')
    Mother_Name.set('')
    Genotype.set('')
    Blood_Group.set('')
    Weight.set('')
    Height.set('')
    Occupation.set('')
    Marital_Status.set('')
    entry_1.configure(state='normal')
    entry_3.configure(state='normal')
    entry_4.configure(state='normal')
    entry_5.configure(state='normal')
    entry_6.configure(state='normal')
    entry_7.configure(state='normal')
    entry_8.configure(state='normal')
    entry_9.configure(state='normal')
    entry_10.configure(state='normal')
    entry_11.configure(state='normal')
    entry_12.configure(state='normal')
    entry_13.configure(state='normal')
    entry_14.configure(state='normal')
    entry_15.configure(state='normal')
    entry_16.configure(state='normal')
    entry_17.configure(state='normal')
    entry_18.configure(state='normal')

      


label = Label(window, text="Your Profile", font=(BOLD, 20), foreground="red")
label.place(x=400, y=10)

First_Name = Label(window, text="First Name", font=(BOLD, 10), foreground="#151515")
First_Name.place(x=100, y=80)
First_Name = StringVar()
entry_1 = Entry(window, textvariable=First_Name, font=(BOLD, 12), width=20)
entry_1.place(x=200, y=80)


Middle_Name = Label(window, text="Middle Name", font=(BOLD, 10), foreground="#202020")
Middle_Name.place(x=500, y=80)
Middle_Name = StringVar()
entry_2 = Entry(window, textvariable=Middle_Name, font=(BOLD, 12), width=20)
entry_2.place(x=600, y=80)

Last_Name = Label(window, text="Last Name", font=(BOLD, 10), foreground="#162030")
Last_Name.place(x=900, y=80)
Last_Name = StringVar()
entry_3 = Entry(window, textvariable=Last_Name, font=(BOLD, 12), width=20)
entry_3.place(x=1000, y=80)

Gender = Label(window, text="Gender", font=(BOLD, 10), foreground="#201420")
Gender.place(x=100, y=180)
Gender = StringVar()
entry_4 = Entry(window, textvariable=Gender, font=(BOLD, 12), width=10)
entry_4.place(x=200, y=180)

Year_Born = Label(window, text="Year Born", font=(BOLD, 10), foreground="#151515")
Year_Born.place(x=500, y=180)
Year_Born = StringVar()
entry_5 = Entry(window, textvariable=Year_Born, font=(BOLD, 12), width=10)
entry_5.place(x=600, y=180)

Current_Year = Label(window, text="Current Year", font=(BOLD, 10), foreground="#151515")
Current_Year.place(x=900, y=180)
Current_Year = StringVar()
entry_6 = Entry(window, textvariable=Current_Year, font=(BOLD, 12), width=10)
entry_6.place(x=1000, y=180)

Complexion = Label(window, text="Your Complexion", font=(BOLD, 10), foreground="#151515")
Complexion.place(x=80, y=280)
Complexion = StringVar()
entry_7 = Entry(window, textvariable=Complexion, font=(BOLD, 12), width=15)
entry_7.place(x=200, y=280)

State_of_Origin = Label(window, text="State of Origin", font=(BOLD, 10), foreground="#202020")
State_of_Origin.place(x=80, y=370)
State_of_Origin = StringVar()
entry_8 = Entry(window, textvariable=State_of_Origin, font=(BOLD, 12), width=18)
entry_8.place(x=200, y=370)

Nationality = Label(window, text="Nationality", font=(BOLD, 10), foreground="#202020")
Nationality.place(x=80, y=460)
Nationality = StringVar()
entry_9 = Entry(window, textvariable=Nationality, font=(BOLD, 12), width=17)
entry_9.place(x=200, y=460)

Religion = Label(window, text="Religion", font=(BOLD, 10), foreground="#202020")
Religion.place(x=500, y=460)
Religion = StringVar()
entry_10 = Entry(window, textvariable=Religion, font=(BOLD, 12), width=20)
entry_10.place(x=600, y=460)

Father_Name = Label(window, text="Father's Name", font=(BOLD, 10), foreground="RED")
Father_Name.place(x=500, y=370)
Father_Name = StringVar()
entry_11 = Entry(window, textvariable=Father_Name, font=(BOLD, 12), width=25)
entry_11.place(x=600, y=370)

Mother_Name = Label(window, text="Mother's Name", font=(BOLD, 10), foreground="BLUE")
Mother_Name.place(x=900, y=370)
Mother_Name = StringVar()
entry_12 = Entry(window, textvariable=Mother_Name, font=(BOLD, 12), width=25)
entry_12.place(x=1000, y=370)

Genotype = Label(window, text="Genotype", font=(BOLD, 10), foreground="#100101")
Genotype.place(x=500, y=280)
Genotype = StringVar()
entry_13 = Entry(window, textvariable=Genotype, font=(BOLD, 12), width=9)
entry_13.place(x=600, y=280)

Blood_Group = Label(window, text="Blood Group", font=(BOLD, 10), foreground="#251020")
Blood_Group.place(x=900, y=280)
Blood_Group = StringVar()
entry_14 = Entry(window, textvariable=Blood_Group, font=(BOLD, 12), width=9)
entry_14.place(x=1000, y=280)

Weight = Label(window, text="Your Weight", font=(BOLD, 10), foreground="#343434")
Weight.place(x=80, y=530)
Weight = StringVar()
entry_15 = Entry(window, textvariable=Weight, font=(BOLD, 12), width=8)
entry_15.place(x=200, y=530)

Height = Label(window, text="Your Height", font=(BOLD, 10), foreground="#303030")
Height.place(x=500, y=530)
Height = StringVar()
entry_16 = Entry(window, textvariable=Height, font=(BOLD, 12), width=8)
entry_16.place(x=600, y=530)

Occupation = Label(window, text="Your Occupation", font=(BOLD, 10), foreground="#500404")
Occupation.place(x=900, y=530)
Occupation = StringVar()
entry_17 = Entry(window, textvariable=Occupation, font=(BOLD, 12), width=15)
entry_17.place(x=1020, y=530)

Marital_Status= Label(window, text="Marital Status", font=(BOLD, 10), foreground="#151515")
Marital_Status.place(x=900, y=460)
Marital_Status = StringVar()
entry_18 = Entry(window, textvariable=Marital_Status, font=(BOLD, 12), width=10)
entry_18.place(x=1000, y=460)


button_1 = Button(window, text="SUBMIT", foreground="#404040", background="BLUE", font=(BOLD, 12), command = Register)
button_1.place(x=100, y=600)
button_2 = Button(window, text="Users List", command=List_of_users, foreground="#203040", background="WHITE", font=(BOLD, 12)).place(x=300, y=600)
button_3 = Button(window, text="Search", command=search, foreground="#202040", background="RED", font=(BOLD, 12)).place(x=500, y=600)
button_4 = Button(window, text="Clear", command=clear, foreground="#505050", background="WHITE", font=(BOLD, 12)).place(x=700, y=600)
     

window.mainloop()