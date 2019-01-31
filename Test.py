# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 17:16:21 2019

@author: SKourav
"""
import pymysql
import datetime
import csv
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="Shiv@123", db="SLB" )
cursor = db.cursor()

#        
#with open ("sample1.csv","r") as fobj:
#    LineList = []
#    for line in fobj:
#        line = line.strip()
#        LineList = line.split(",")
#        print (''+LineList[0]+'')
#        sql = "insert into Realstate (street,city,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude) values ('{}','{}','{}',{},{},{},'{}',{},{},{},{})". \
#        format(''+LineList[0]+'',''+LineList[1]+'',''+LineList[3]+'',int(LineList[4]),int(LineList[5]),int(LineList[6]),''+LineList[7]+'',LineList[8],int(LineList[9]),float(LineList[10]),float(LineList[11]))
#        cursor.execute(sql)
#        db.commit()
#        db.close()
        

fob = open("sample1.csv","r")
csv_data = csv.reader(fob)
for row in csv_data:
    print (format(row[0]))
    sql = "insert into Realstate (street,city,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],datetime.datetime.now(),row[8],row[9],row[10])
    cursor.execute(sql)
    db.commit()
    db.close()