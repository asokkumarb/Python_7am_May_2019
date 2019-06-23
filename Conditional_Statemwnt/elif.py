"""
elif statement
The elif statement allows you to check multiple expressions for TRUE and Execute a block
of code as soon as one of the conditions evaluates to TRUE.

Syntax :
if expression:
    statement(s)
elif expression:
    statement(s)
elif expression:
    statement(s)
else:
    statement(s)
"""

# !/usr/bin/python

fee = int(input("Enter Fee : "))

if fee == 20:
    message = "if block - Condition is true"

elif fee == 10:
    message = "elif block - Condition is True"

elif fee == 13:
    message = "2nd elif block - Condition is True"

else:
    message = "This is Else Block and Condition is False"

print(message)