import pymysql

host="pythondb.ccivfec6o9a5.ap-south-1.rds.amazonaws.com"
port=3306
dbname="pythondb"
user="pythondb"
password="pythondb"
conn = pymysql.connect(host,user=user,port=port,passwd=password,db=dbname)


import pyMySQL

# Open database connection
db = pyMySQL.connect("pythondb.ccivfec6o9a5.ap-south-1.rds.amazonaws.com","pythondb","pythondb")
#db = MySQLdb.connect("localhost","root","redhat","linux" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()

"""
#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("pythondb.ccivfec6o9a5.ap-south-1.rds.amazonaws.com","pythondb","pythondb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()

"""