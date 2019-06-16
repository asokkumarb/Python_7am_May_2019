
# Dictionaries Method : fromkeys ()

'''

Returns a dictionary with the specified keys and values

tuple or list to dictionary with value

'''

l1 = ['element1','element2','element3',8414]

t1 = ('member1','member2','member3',4148)

d1 = dict.fromkeys(l1) # list to dict
print(d1)

d2 = dict.fromkeys(t1) # list to tuple
print(d2)

d1 = dict.fromkeys(l1,10)  # inserting value on dict variable
d2 = dict.fromkeys(t1,11)  # inserting value on dict variable

print("")
print (d1,d2)

# amending value of key

d1['element2'] = 15
d2['member2'] = 16
print ("")
print(d1,d2)

print("")
d1.update(d2)
print(d1)

'''
o/p -
{'element1': None, 'element2': None, 'element3': None, 8414: None}
{'member1': None, 'member2': None, 'member3': None, 4148: None}

{'element1': 10, 'element2': 10, 'element3': 10, 8414: 10} {'member1': 11, 'member2': 11, 'member3': 11, 4148: 11}

{'element1': 10, 'element2': 15, 'element3': 10, 8414: 10} {'member1': 11, 'member2': 16, 'member3': 11, 4148: 11}

{'element1': 10, 'element2': 15, 'element3': 10, 8414: 10, 'member1': 11, 'member2': 16, 'member3': 11, 4148: 11}
'''

