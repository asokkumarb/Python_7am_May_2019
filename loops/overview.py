"""
Loops in Python:

1. While

&

2. For

while expression:  # True and it will execute until the false condition
    statement(2)

var = 1

while var <= 10:
    print("I am While Loop", + var, sep="  ")
    var = var + 1

print("")
print("We are out of the while block")

"""

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
