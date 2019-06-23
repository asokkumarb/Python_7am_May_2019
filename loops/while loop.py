"""
Loops in Python:
1. While
&
2. For

while expression:  # True and it will execute until the false condition
    statement(2)
"""
print("Example 1")
var1 = 1
while var1 <= 10:
    print("I am While Loop", var1, sep=" ")
    var1 = var1 + 1
print("")
print("We are out of the while block")

print("---------------------------------------------------")
print("Example 2")

passWord = ""

while passWord != "redhat":
    passWord = input("Please enter the password: ")

    if passWord == "redhat":
        print("Correct password")

    elif passWord == "admin@123":
        print("It was previously used password")

    elif passWord == "Redhat@123":
        print("This is your recent changed password")

    else:
        print("Incorrect Password- try again")