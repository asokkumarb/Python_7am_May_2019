import cgi
import cgitb

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