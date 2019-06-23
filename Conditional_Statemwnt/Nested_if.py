'''
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
'''

print("Example 1")

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

print ("------------------------------------")
print("Example 2 : to find Maximum number from 3 inputs")

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
print("The maximam value is: ",maximum)

print("-------------------------------------------")
print("Example 3 : to find minimum value from 3 inputs")
x1 = float(input("1st Number: "))
y1 = float(input("2nd Number: "))
z1 = float(input("3rd Number: "))

if x1 < y1:
    if x1 < z1:
        minimum = x1
    else:
        minimum = z1
else:
    if y1 < z1:
        minimum = y1
    else:
        minimum = z1

print("The minimum value is: " + str(minimum))
