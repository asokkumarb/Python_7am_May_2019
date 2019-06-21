import os

try:
    file = open("abc.txt")
    print(file.read())
    print(file.tell())
    print(file.seek(0))
    print(file.readline())
    print(file.tell())
    print(file.seek(0))
    print(file.readlines())
    print(file.tell())
    print(file.seek(0))
finally:
    file.close()