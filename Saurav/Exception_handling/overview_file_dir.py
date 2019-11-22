"""
import os

print(os.getcwd())
print(os.listdir())
#print(os.mkdir("new_dir"))

#print(os.rmdir("new_dir"))

"""
"""
file = open("abc.txt")
print(file.read())
print(file.tell())

print(file.seek(0))
file.close()

"""

"""

file =open("abc.txt", 'r')

#file.write("\n I m from BBSR",)

print(file.read())

"""
"""

try:
    file=open('abc.txt', 'r+')
    print(file.readline())
    print(file.readlines())
finally:
    file.close()
    
"""

"""
with open('abc.txt', 'r') as file:
    print(file.read())
"""

import os

"""
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
"""

"""
import os
import fnmatch

path = "/Users/g802199/Python_7am_May_2019/Saurav/Exception_handling/"
patern = "*.py"

for root,dirs,files in os.walk(path):
    for filename in fnmatch.filter(files,patern):
        print(os.path.join(filename))
        
 """

"""

import os
relevant_path = "/Users/g802199/Python_7am_May_2019/Saurav/Exception_handling/"
included_extensions = ['*py','*mp3']
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]

"""
"""
import os

import fnmatch

import glob

x=fnmatch.filter(os.listdir('.'), '*.py')
y=fnmatch.filter(os.listdir('.'), '*.mp3')
print(x,y)

#fnmatch.filter(os.listdir('/Users/g802199/Python_7am_May_2019/Saurav/Exception_handling/'), '*.py')
"""
import os

import fnmatch

import glob
import re
"""
relevant_path = ("/Users/g802199/Python_7am_May_2019/Saurav/Exception_handling/")
included_extensions = ['*.py', '*.mp3']
file_names = [fn for fn in os.listdir('.')
              if any(fn.endswith(ext) for ext in included_extensions)]
print(file_names)

"""


print(files)
