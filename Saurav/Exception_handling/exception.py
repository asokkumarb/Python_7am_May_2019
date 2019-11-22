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

#print(os.getcwd())
#print(os.listdir())
#print(os.getpid())

#os.mkdir("new_dir")
"""
print(os.chdir("/Users/g802199/Python_7am_May_2019/Saurav/"))
print(os.getcwd())

x = 15

if x > 5:
    raise Exception(f"x should not be greater than 5 but the current value of x is {x}")
"""

import sys

def platform_check():
    assert ('' in sys.platform), "Function can only run on Windows systems"
    print("Hi, Welcome to Python World")

try:
    platform_check()
except AssertionError as error:
    print(error)
    print("platform_check function was not executed")
else:
    print("Executing the Code")

finally:
    print("i m the final block")

