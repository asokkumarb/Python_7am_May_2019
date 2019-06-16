
# Dictionaries Method : Clear ()

'''
clear will remove all value from dictionary variable
but it will not delete variable
o/p - empty dictionary variable

'''

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

d1.clear()
print(d1) # will print empty dictionary

'''
o/p -
4 2790890702960 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

{}
'''