"""
nested if statements

When you want to check for another condition after a condition resolves to true.

In such a situation, you can use the nested if construct.

if..elif..else

Syntax : 

if expression1:
    statements
    
    if expression:
        statements
    else:
        statements

elif expression:
    statements
    
    if expression:
        statements
    elif expression:
        statements
    else:
        statements

else:
    statements

#!/usr/bin/python
mac_os = 100

if mac_os < 200:
   print("Expression value is less than 200")
   if mac_os == 150:
      print("Which is 150")
   elif mac_os == 100:
      print ("Which is 100")
   elif mac_os == 50:
      print("Which is 50")
elif mac_os < 50:
   print("Expression value is less than 50")
else:
   print("Could not find true expression")

print("Good bye!")

#!/usr/bin/python

x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))
 # 5 > 6
if x > y:
    if x > z:
        maximum = x
    else:
        maximum = z
else:
    #  6 > 4
    if y > z:
        maximum = y
    else:
        maximum = z

print("The maximam value is: " + str(maximum))
"""




x = float(input("1st Number: "))
y = float(input("2nd Number: "))
z = float(input("3rd Number: "))

if x < y:
    if x < z:
        minimum = x
    else:
        minimum = z
else:
    if y < z:
        minimum = y
    else:
        minimum = z

print("The minimum value is: " + str(minimum))
