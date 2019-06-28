# Importing Modules and Classes from a Module
from tkinter import *
from tkinter import messagebox

# Creating a Variable
top = Tk()

top.geometry("500x500")

# Create a Function

def helloCallBack():
    msg = messagebox.showinfo("HOME","Welcome to Python GUI World")

B = Button(top, text="CLICK TO LOGIN", command=helloCallBack)

B.place(x=10,y=10)

top.mainloop()


