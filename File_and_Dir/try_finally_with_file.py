"""
try:
    statement(s)
finally:
    statement(s)

try:
    file = open("abc1.txt",'r+')
    print(file.readline())
    print(file.readlines())
finally:
    file.close()

"""

# with statement :

with open("abc.txt",'r') as myfile:
    print(myfile.readline())
    print(myfile.readlines())
