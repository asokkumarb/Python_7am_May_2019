vi index.html

<html>
<head>
<title>Code With Keshav Kummari</title>
</head>

<body bgcolor="olive">

<h1> Welcome to Python World </h1>

<h2> Select your course option </h2>
<form action="/cgi-bin/checkbox.py" method="GET" target="_blank">
First Name : <input type="" name="FirstName"/>
Last Name  : <input type="" name="LastName"/>
<input type="checkbox" name="Python" value="on" /> Python
<input type="checkbox" name="Perl" value="on" /> Perl
<input type="submit" value="Click Me!" />
</form>

</body>
</html>


[root@dev html]# cat ../cgi-bin/checkbox.py
#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('Python'):
        course_flag = "Learn Python By Doing!"
else:
   course_flag = "Course Was Not Selected"

if form.getvalue('Perl'):
   Perl_flag = "Learn Perl By Doing!"
else:
   Perl_flag = "Course Was Not Selected"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Checkbox - Third CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> You have Selected Python : %s</h2>" % course_flag)
print ("<h2> You have selected Perl : %s</h2>" % Perl_flag)
print ("</body>")
print ("</html>")