"""
print(dict1,type(dict1),id(dict1),len(dict1),dict(enumerate(dict1)))

dict1['Age'] = 5

print(dict1)

dict1['School'] = 'DP School'

print(dict1)

print(dict1['Name'])

# del dict1
# del dict1['Name']

dict1.clear() # Remove all the entries in a variable called dict1

print(dict1)

print(dict1['Name'])

print(dict1.get('Name'))

print(dict1.get('minnu'))

print(dict1.get('FirstName','Gudio'))

print(dict1.keys())
print(dict1.values())

print(dict1.items())


print(dict1,id(dict1))

newDict = dict1.copy()

print(newDict,id(newDict))


account = ('Name','Address','AccountNumber')

a = dict.fromkeys(account,10)

print(a)
"""
dict1 = {'Name': 'minnu', 'Age': 7, 'Class': 'First'}

print(dict1.setdefault('Age',None))
print(dict1.setdefault('Course','Python'))

dict2 = {'Data':'Raw','id':10}

dict1.update(dict2)

print(dict1)