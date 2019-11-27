from xml.dom import minidom

doc =minidom.parse("staff.xml")

name = doc.getElementsByTagName("name")[:]

print(name.firstChild.data)



staffs=doc.getElementsByTagName("staff")

for i in staffs:
    sid=i.getAttribute("id")
    nickname=i.getElementsByTagName("nickname")[0]
    salary=i.getElementsByTagName("salary")[0]
    print("id:%s,nickname:%s,salary :%s" %(sid,nickname.firstChild.data,salary.firstChild.data))


