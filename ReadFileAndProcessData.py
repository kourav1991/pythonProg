# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:20:48 2019

@author: SKourav
"""
cityList = []
count = 0

#with open ("sample1.csv","r") as fobj:
#    for line in fobj:
#        line = line.strip()
#        LineList = line.split(",")
#        for city in cityList :
#            if city == LineList[1]:
#                count = count + 1
#        if count > 0 :
#            count = 0
#        else :
#            cityList.append(LineList[1])
#            count = 0
#        
#print ("Unique Cities")
#print ("----------------\n")
#for city in cityList:
#    print (city)
    
#Second way using Set
    
Unique_City = set()

with open ("sample1.csv","r") as fobj:
    for line in fobj:
        
        line = line.strip()
        LineList = line.split(",")
        Unique_City.add(LineList[1])


print ("Unique Cities")
print ("----------------\n")
for city in Unique_City:
    print (city)
    