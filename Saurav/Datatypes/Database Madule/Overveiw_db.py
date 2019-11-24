
import mysql.connector

db= mysql.connect("hostname/ip:port","pythondb","password","schema" )

cursor=db.cursor()

cursor.execute("select * from emp where emp_name is like '%saura%' ")

data= cursor.fetchone()

print(f'empolye name is :{data}')

db.close()