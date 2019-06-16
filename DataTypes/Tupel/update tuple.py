
# Tuple can not be updated as it is immutable but can possible to add two tuple

tup1 = (103,102,101)

tup2 = ('a','b','c')

# tup1[2] = 100
# TypeError: 'tuple' object does not support item assignment

print (tup1)
print (tup2)
print("")

tup3 = tup1 + tup2
print (tup3)

'''
o/p -

(103, 102, 101)
('a', 'b', 'c')

(103, 102, 101, 'a', 'b', 'c')

'''

