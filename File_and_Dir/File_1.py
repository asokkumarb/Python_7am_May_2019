import os

try:
    file = open("abc.txt","r")
    char = {}

    for line in file.readlines():
        for c in line.strip():
            char[c] = char.get(c,0) + 1

    for item in char.items():
        print(item)

finally:
    file.close()