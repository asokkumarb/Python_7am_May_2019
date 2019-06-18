"""
# Declaring the variables
a = input("Enter number1: ")
b = input("Enter number2: ")
c = int(a) / int(b)

# Accessing them in print function
print("Division is: ",c)

a = input("Enter Number : ")
b = input("Enter Number : ")

try:
    c = int(a) / int(b)
except Exception as e:
    print(f'Exception Occured: {e}')
    c = None

print(c)

a = input("Enter Number : ")
b = input("Enter Number : ")

try:
    c = int(a) / int(b)
except ZeroDivisionError as e:
    print(f'Division by Zero Exception: {e}')
    #c = None

#print(c)
"""

# Declaring the variables
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
finally:
    print("Executing Finally Clause")

print("Division is: ",c)




