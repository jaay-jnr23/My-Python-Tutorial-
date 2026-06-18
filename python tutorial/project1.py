from tkinter import *
from tkinter.ttk import *
from tkinter.font import BOLD
from time import strftime


window = Tk()
window.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(window, font=(BOLD, 20), background="black", foreground="cyan")
label.pack(anchor='center')

time()

window.mainloop()