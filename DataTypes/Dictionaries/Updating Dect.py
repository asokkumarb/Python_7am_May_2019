
# Method in Dictionaries : updating

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

# updating element 3 (index 2)
print(d1)
d1['lectures'] = 37

print(d1)

# adding element at end of Dictionary

d1['school'] = 'NIT'
print(d1)

# to know value of of key  - call key by print

print(d1['type']) # calling key to print value

'''
o/p -
4 1616194668656 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

{'course': 'Python', 'type': 'online', 'lectures': 35, 'students': 10}
{'course': 'Python', 'type': 'online', 'lectures': 37, 'students': 10}
{'course': 'Python', 'type': 'online', 'lectures': 37, 'students': 10, 'school': 'NIT'}
online



'''