""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database python10")
cursor.execute("show databases")
for x in cursor:
    print(x)
cursor.execute("use python10")
cursor.execute("create table python10 (department_no INT PRIMARY KEY ,department_name VARCHAR(50))")
cursor.execute("show tables")
print("Number of tables in database :")
for x in cursor:
    print("\t",x)
s="insert into department values(%s,%s)"
t=(1,"tamil")
cursor.execute(s,t)
connection.commit() """

import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database py")
cursor.execute("show databases")
for x in cursor:
    print(x)
cursor.execute("use py")
