
"""
Polymorphism means the ability to take various forms.

It allows us to define methods in the child class with the same name as defined in their parent class.

In such cases, you will have to re-implement methods in the child class

"""

class India():

    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")

    def type(self):
        print("Developing")

class USA():

    def capital(self):
        print("Washington DC")

    def language(self):
        print("English")

    def type(self):
        print("Developed")

obj_india = India()
#obj_india.capital()
#obj_india.language()
#obj_india.type()
obj_usa = USA()
#obj_usa.capital()
#obj_usa.language()
#obj_usa.type()

for i in (obj_india,obj_usa):
    i.capital()
    i.language()
    i.type()
    
