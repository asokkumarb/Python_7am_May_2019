import xml.sax.handler

class EmpHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inDepartment = False
        self.inFirstName = False

    def startElement(self, name, attributes):
        if name == 'department':
            self.inDepartment = True
        elif name == 'firstName':
            self.inFirstName = True

    def characters(self, data):
        if self.inDepartment:
            print(data)
        elif self.inFirstName:
            print(data)

    def endElement(self, name):
        if name == 'department':
            self.inDepartment = False
        elif name == 'firstName':
            self.inFirstName = False

import xml.sax

parser = xml.sax.make_parser()

handler = EmpHandler()

parser.setContentHandler(handler)

parser.parse('sample.xml')