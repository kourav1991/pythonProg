# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:44:44 2019

@author: SKourav
"""
import time
import os

timestr = time.strftime("%Y%m%d-%H%M%S")
fileName = "EvenNo" + timestr + ".txt"
fileObj = open("EvenNo" + timestr + ".txt","w")

for num in range(300,501,2):
    if os.path.exists(fileName):
        print ("file is already exist")
        break
    else :
        fileObj.write(str(num)+"\n")
        print ("file created")
        
    
    
fileObj.close();