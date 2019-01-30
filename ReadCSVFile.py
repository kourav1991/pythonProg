# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:12:30 2019

@author: SKourav
"""


fobj = open("sample.csv","r")

for line in fobj:
    line = line.strip();
    print(line)
fobj.close()