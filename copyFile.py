# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:26:30 2019

@author: SKourav
"""

import os 
import shutil

for file in os.listdir() :
    if file.endswith(".py") :
        #print (os.getcwd()+ file , os.getcwd() + "/Backup")
        shutil.move(os.getcwd() + "/" + file , os.getcwd() + "/Backup")