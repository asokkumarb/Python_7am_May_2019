class Animal:
   def __init__(self, name=''):
      self.name = name

   def talk1(self):
      #pass  # Empty
      print(self.name,"Welcome to Animal World")


class Cat(Animal):
   def talk2(self):
      print (self.name,"Meow!")


class Dog(Cat,Animal):
   def talk(self):
      print (self.name, "Woof!")

a = Dog()
a.talk()
a.talk1()
a.talk2()
