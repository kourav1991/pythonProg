# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:59:58 2019

@author: SKourav
"""

import os
import time

fileName = time.strftime("%d%m%y.log")

if  os.path.exists(fileName):
    print("File Already exist")
else :
            fobj  = open(fileName,"w")
            for file in os.listdir() :
                if os.path.isfile(file):
                    fobj.write(file+"\n")

fobj.close()