# cd /var/www/html

# vi index.html

<html>
<head>
<title>Code with Keshav Kummari</title>
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

# vi checkbox.py

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('Python'):
    course_python = "You have selected Python Course"
else:
    course_python = "You have not selected any Course"

if form.getvalue('Perl'):
    course_perl = "You have selected PERL Course"
else:
    course_perl = "You have not selected any Course"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Checkbox - CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> CheckBox Python is : %s</h2>" % course_python)
print ("<h2> CheckBox Perl is : %s</h2>" % course_perl)
print ("</body>")
print ("</html>")