
# Dictionaries Method : Copy ()

'''

to copy variable of dictionary to other variable

'''

d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

print(d1,id(d1))

d2 = d1.copy()

print("new variable d2 :",d2,id(d2)) # will be in different memory location

'''
o/p -
4 2125572311152 <class 'dict'> {0: 'course', 1: 'type', 2: 'lectures', 3: 'students'}

{'course': 'Python', 'type': 'online', 'lectures': 35, 'students': 10} 2125572311152
new variable d2 : {'course': 'Python', 'type': 'online', 'lectures': 35, 'students': 10} 2125574957168
'''
