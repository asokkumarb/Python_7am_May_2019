import sys

#file = open("/Users/keshavkummari/abc.txt")

import os

print(os.getcwd())

print(os.uname())

print(os.getpid())

# print(os.listdir("/Users/keshavkummari/Python_7am_May_2019/Exception_Handling"))

#os.mkdir("GuidoVanRossum")

#print(os.listdir("/Users/keshavkummari/Python_7am_May_2019/Exception_Handling"))

print(os.chdir("/Users/keshavkummari/"))

print(os.getcwd())

"""

for i in file:
    try:
        file = open(i, 'r')
    except Exception as e:
        print('Can Not Open', e)
    else:
        print(i, 'has', len(file.readlines()), 'lines')
        file.close()
"""