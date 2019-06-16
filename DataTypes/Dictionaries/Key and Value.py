
# Dictionary Method : Key and Value

'''

to print only Keys or only Values

'''

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

print(d1.keys())
print("")

print(d1.values())

'''
o/p -
4 1424025815152 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

dict_keys(['course', 'type', 'lectures', 'students'])

dict_values(['Python', 'online', 35, 10])

'''