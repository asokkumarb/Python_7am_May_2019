
# Dictionaries Method : Get()

'''


'''

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

print (d1.get('type')) # will print value of key
print (d1.get('online')) # will not print key for value

# can call key directly to print value

print(d1['type'])
# print(d1['online']) -  will give error

# get method with two unknown elements

print (d1.get('teacher','Keshav')) # consider second element as value of 1st element

'''
o/p - 
4 2221393938544 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

online
None
online
Keshav
'''
