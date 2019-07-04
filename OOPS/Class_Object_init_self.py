class Human:

    def __init__(self, n, o):   # Constructors
        self.name = n           # Properties of Human Class
        self.occupation = o     # Properties of Human Class

    def do_work(self):          # Method of Class
        if self.occupation == "singer":
            print(self.name,"is a Singer")
        elif self.occupation == "actor":
            print(self.name,"is a FilmStar")
        else:
            print(self.name,"is Not Signer nor Actor!")

    def speaks(self):  # Method of Class
        print(self.name,"Says How Are you?")

# Creating an Object
a1 = Human('Joel','Python Programmer')
a1.do_work()
a1.speaks()