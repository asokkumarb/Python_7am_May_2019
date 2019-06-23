
# DataTypr : Sets

'''
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
'''

a = set() # empty set

print(len(a),type(a),id(a),set(enumerate(a)))

abc = set(('a','b','a','b'))
print (abc,type(abc),id(abc))

abc_list1 = set(['100','101','102','100'])
print(abc_list1,id(abc_list1),set(enumerate(abc_list1))) # unindex

abc_dict1 = set({'course':'Python','type':'online','lectures':35,'students':10})
print(abc_dict1,id(abc_dict1),type(abc_dict1),set(enumerate(abc_dict1)))

'''
o/p -
0 <class 'set'> 1378250468936 set()
{'b', 'a'} <class 'set'> 1378250553160
{'100', '101', '102'} 1378250554504 {(0, '100'), (1, '101'), (2, '102')}
{'type', 'lectures', 'course', 'students'} 1378250554056 <class 'set'> {(1, 'lectures'), (2, 'course'), (3, 'students'), (0, 'type')}
'''