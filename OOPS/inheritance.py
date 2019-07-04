class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()

"""
class A:

    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):

    def g(self):
        return 'B'

_a = A()

print(_a.f(),_a.g())

_a1 = B()

print(_a1.g(),_a1.f())

"""