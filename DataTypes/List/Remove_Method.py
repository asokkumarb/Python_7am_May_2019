aCoolList = ["superman", "spiderman", 1947,1987,1947,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

print(aCoolList,list(enumerate(aCoolList)))

aCoolList.remove(1947)

print(aCoolList,list(enumerate(aCoolList)))

aCoolList.remove('superman')

print(aCoolList,list(enumerate(aCoolList)))

aCoolList.remove('DevOps')

print(aCoolList,list(enumerate(aCoolList)))