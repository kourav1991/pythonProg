# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:04:31 2019

@author: SKourav
"""

fobj = open("300119.log", "r")

#Reading the output in list 

print (fobj.readlines())
fobj.close()    