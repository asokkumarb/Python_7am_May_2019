from xml.etree.ElementTree import parse

xmlTree = parse("sample.xml")

for i in xmlTree.findall('firstName'):
    print(i.text)

for i in xmlTree.findall('lastName'):
    print(i.text)

for i in xmlTree.findall('department'):
    print(i.text)