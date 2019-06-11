# union() Method

a = [1,2,3,4,5]

b = [5,6,7]

print(set(a),set(b))

print(set(a).union(set(b)))

"""
Returns the union of set "a" and the set of elements in iterable with set "b"
"""

# intersection()

"""
Returns the insection of set a and the set of elements in iterable
"""

"""
print(set(a).intersection(b))

# difference()

print("difference method :",set(a).difference(b))

# update()

s = set([1,2,3,4,5])

s.update(set([5,6,7]))

print(s)

# add()

s1 = set([1,2,3,4,5])
s1.add(6)

print("Add Method :",s1)

# remove() and discard()

s2 = set([1,2,3,4,5])

s2.remove(5)

s2.discard(6)

print(s2)

# pop()

s3 = set([1,2,3,4,5])

print(s3.pop())

print(s3)
"""

# issubset()

s = set([2, 9, 7, 1])
print(s.issubset(s))

print(set([2, 9, 7, 1]).issubset(set([1, 7])))
print(set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4])))
print(set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4, 5, 6, 7, 8, 9])))

# issuperset()

s = set([2, 9, 7, 1])
print(s.issuperset(s))

print(set([2, 9, 7, 1]).issuperset(set([1, 7])))

print(set([2, 9, 7, 1]).issuperset(set([1, 2, 3, 4])))

print(set([2, 9, 7, 1]).issuperset(set([1, 2, 3, 4, 5, 6, 7, 8, 9])))

print(set([2, 9, 7, 1]).issuperset([1, 2, 7, 9]))


abc = set('abc')
print(abc)