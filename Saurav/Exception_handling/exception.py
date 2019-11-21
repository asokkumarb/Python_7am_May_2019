"""
a = int(input("enter the value of a:"))

b = int(input("enter the value of b:"))

try:
    c = a/b
except Exception as d:
    print(f'Exception occurred : {d}')
    c="None"
print(c)

"""
"""
a = input("Enter number1: ")
b = input("Enter number1: ")

try:
    c = int(a) / int(b)
except ZeroDivisionError as e:
    print('Division by Zero Exception')
    c = None
except Exception as e:
    print('Exception type:',type(e).__name__)
    c = None
#finally:
#    print("Executing Finally Clause")

print("Division is: ",c)

"""

import os

#print(os.getcwd())
#print(os.listdir())
#print(os.getpid())

#os.mkdir("new_dir")
print(os.chdir("/Users/g802199/Python_7am_May_2019/Saurav/"))
print(os.getcwd())
