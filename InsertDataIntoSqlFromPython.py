# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:30:55 2019

@author: SKourav
"""

import pymysql


db = pymysql.connect(host="localhost",port=3306,user="root",passwd="Shiv@123",db="SLB")

#Prepare a cusrsome object using cursoe () method

cursor = db.cursor()

#Drop table is already exist

#cursor.execute("DROP TABLE IF EXISTS EMPLOYEEDETAIL")

#Create table 

sql = "INSERT INTO EMPLOYEEDETAIL (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('ABC','F',26,'M',150000)"

cursor.execute(sql);
db.commit()
print("data inserted")
db.close();