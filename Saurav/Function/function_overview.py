
"""

def sum(a, b):
    sum=a+b
    return sum


c = sum(20, 35)
print(c)
"""

"""
def banu(x,y):
    z=x+y
    print(z)
    return


x = int(input("enter the value of X :"))
y = int(input("enter the value of y :"))

banu(x,y)

"""


def info(var1, *var2):
    print(var1)
    for i in var2:
        print(i)
    return


info(10, 20, 30, 40, 50)
