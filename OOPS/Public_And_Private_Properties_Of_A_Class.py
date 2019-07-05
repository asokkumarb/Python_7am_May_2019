class P:
    def __init__(self, name, alias):
        self.name = name                # Public Class property
        self.__alias = alias            # Private Class Property

    def who(self):                      # Public Class Method
        print("Name : ", self.name)
        print("Alias: ", self.__alias)

    def __foo(self):                    # Private Class Method
        print("This is a Private Method!")

    def foo(self):
        print("This is a Public Method")
        self.__foo()

a = P('Guido','Rossum')

a.who()
a._P__foo()
a.foo()
