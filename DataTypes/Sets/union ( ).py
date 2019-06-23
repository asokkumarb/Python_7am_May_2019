
# Set Method : union ()

'''
Return a set containing the union of sets
'''

a = [1,2,3,4,5]
b = [5,6,7,8]

print(set(a),set(b))
print(set(a).union(set(b)))

'''
o/p -
{1, 2, 3, 4, 5} {8, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7, 8}
'''