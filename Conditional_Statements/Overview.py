'''
Decision making is anticipation of conditions occurring while execution of the program
and specifying actions taken to the conditions.

Decision structures evaluate multiple expressions which produce TRUE or FALSE as outcome.


1. simple if   
2. if..else 
3. elif
4. neasted elif


course_name = input('Enter your Course Name : ')

course = 'python'

if course_name == course.lower():
    print("1 - Got a True Expression Value")

print("welcome to Python World")

if course_name.lower() == course.lower(): print("Welcome to Python Course")

# if..else

# Syntax :

if expression:
    statement(s)
else:
    statement(s)
'''

a_value = int(input("Enter a Number Value : "))

if a_value == 100:
    message = "Condition is True"

else:
    message = "Condition is False"


print(message)
