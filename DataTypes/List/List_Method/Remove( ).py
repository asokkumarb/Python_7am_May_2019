
# List Method : Remove()

'''

to remove specific element from list

'''

pydev = ["DevOps","AWS",1985,2019,1985,"devops",2018]

print(list(enumerate(pydev)))
print ("")

pydev.remove(1985)  # will remove first duplicate element and not both or all

print(list(enumerate(pydev)))
print("")

# pydev.remove("india")  - will give error as not in mail list

# remove by element indexing

pydev.remove(pydev[1])
print(list(enumerate(pydev)))
print("")

pydev.remove(pydev[-1])
print(list(enumerate(pydev)))
print("")

onemorelist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list(enumerate(onemorelist)))
print("")

onemorelist.remove(onemorelist[0])
print(list(enumerate(onemorelist)))

'''
0/p -
[(0, 'DevOps'), (1, 'AWS'), (2, 1985), (3, 2019), (4, 1985), (5, 'devops'), (6, 2018)]

[(0, 'DevOps'), (1, 'AWS'), (2, 2019), (3, 1985), (4, 'devops'), (5, 2018)]

[(0, 'DevOps'), (1, 2019), (2, 1985), (3, 'devops'), (4, 2018)]

[(0, 'DevOps'), (1, 2019), (2, 1985), (3, 'devops')]

[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)]

[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20)]
'''
