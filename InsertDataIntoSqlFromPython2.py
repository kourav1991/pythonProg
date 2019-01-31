# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:51:45 2019

@author: SKourav
"""

#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="Shiv@123", db="SLB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#       LAST_NAME, AGE, SEX, INCOME) \
#       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#       ('Mac', 'Giridhar', 20, 'M', 20000)

sql = "insert into EMPLOYEEDETAIL (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) values ('{}','{}',{},'{}',{})". \
format('Giri','S',60,'M',10000)

cursor.execute(sql)

db.commit()

db.close()