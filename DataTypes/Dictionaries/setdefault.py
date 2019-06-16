


# Dictionaries Method : setdefaults()

'''

Returns a dictionary with the specified keys and values

'''



d1 = {'course':'Python','type':'online','lectures':35,'students':10}

print(len(d1),id(d1),type(d1),dict(enumerate(d1)))
print("")

print (d1.setdefault('type',None))
print (d1.setdefault('month','May'))

print (d1)