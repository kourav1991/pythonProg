# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:38:09 2019

@author: SKourav
"""
import pymysql
import datetime
import csv
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="Shiv@123", db="SLB" )
cursor = db.cursor()

def readCSV():
    
    fob = open("sample1.csv","r")
    csv_data = csv.reader(fob)
    for row in csv_data:
        sql = "insert into Realstate (street,city,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],datetime.datetime.now(),row[8],row[9],row[10])
        cursor.execute(sql)
        db.commit()
        db.close()

def insertIntoDB(row):
    try :
        sql = "insert into Realstate (street,city,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],datetime.datetime.now(),row[8],row[9],row[10])
        cursor.execute(sql)
        db.commit()
        db.close()

    except Exception as error:
        print ("exception while inserting value into DB",error)
    else :
        db.close()
    finally :
        print ("This will execute always")

try :
    readCSV()
except Exception as error :
    print ("Exception occure :" , error)

    