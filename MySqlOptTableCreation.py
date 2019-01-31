# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:05:29 2019

@author: SKourav
"""

import pymysql

#Opening DB connection
db = pymysql.connect(host="localhost",port=3306,user="root",passwd="Shiv@123",db="SLB")

#Prepare a cusrsome object using cursoe () method

cursor = db.cursor()

#Drop table is already exist

cursor.execute("DROP TABLE IF EXISTS Realstate")

#Create table 

sql = """CREATE TABLE Realstate (
         street VARCHAR(500) NOT NULL,
         city VARCHAR(100),
         state VARCHAR(100),
         beds INT,
         baths INT,
         sq__ft INT,
         type VARCHAR(100),
         sale_date DATETIME,
         price INT,
         latitude FLOAT,
         longitude FLOAT)"""

cursor.execute(sql)

print("table created")

#Discnnect DB

db.close()