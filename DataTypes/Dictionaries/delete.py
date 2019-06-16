
# delete method in Dictionaries

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

# del d1
# print d1 # will give error as dictionary has been deleted by del d1

del d1['lectures']
print (d1)
print("")

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))

'''
o/p -
4 2332219967600 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

{'course': 'Python', 'type': 'online', 'students': 10}

3 2332219967600 <class 'dict'> {0: 'course', 1: 'type', 2: 'students'}
'''


