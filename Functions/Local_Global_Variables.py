#!/usr/bin/python

total = 0 # This is global variable.

# Function definition is here
def sum(arg1,arg2):
   # Add both the parameters and return them."
   total = arg1 + arg2 # Here total is local variable.
   print("Inside the function local total : ", total,id(total),type(total))
   return

# Now you can call sum function
sum(10,20)

print("Outside the function global total : ", total,id(total),type(total))