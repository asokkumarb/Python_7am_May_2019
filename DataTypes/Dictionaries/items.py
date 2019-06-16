
# Dictionaries Method : Items

'''

elements will get printed in tuples of dictionaries

'''

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

print(d1.items())

'''
o/p -
4 1773510953072 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

dict_items([('course', 'Python'), ('type', 'online'), ('lectures', 35), ('students', 10)])

'''