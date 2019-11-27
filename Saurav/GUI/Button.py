from tkinter import *

from tkinter import messagebox

top=Tk()

top.geometry("500x500")

def hellcallback():
    msg=messagebox.showinfo("HOME","Welcome To Python World")

B=Button(top,text="CLICK HERE TO LOGIN",command=hellcallback)
B.place(x=50,y=50)
top.mainloop()