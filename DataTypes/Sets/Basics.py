"""
A set is an unorderd collection without duplicates

when printed, iterated upon, or converted into a sequence, it's elements will appear in an arbitrary, implementation-dependent order.

"""

a = set()

print(a, type(a), id(a))

#abc = set(('a','b','a','b'))

abc = set(['a','b','a','b'])

print(abc,type(abc),id(abc))

adict = set({1:10,2:15})

print(adict,type(adict),id(adict))