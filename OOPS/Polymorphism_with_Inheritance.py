class Document:
    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError("SubClass Must Implement Abstract Method")

class Pdf(Document):

    def show(self):
        return "Show PDF Contents!"

class Word(Document):

    def show(self):
        return "Show Word Contents!"

documents = [Pdf('Document1'),Word('Document3')]


for i in documents:
    print(i.name + ':' + i.show())
