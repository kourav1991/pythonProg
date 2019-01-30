# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:58:48 2019

@author: SKourav
"""

#By default file will be opend in read mode

fobj = open("300119.log","r")

for line in fobj:
    line = line.strip()
    print(line)

fobj.close();