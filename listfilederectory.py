# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:22:07 2019

@author: SKourav
"""

import os

for file in os.listdir() :
    if file.endswith(".txt") or file.endswith(".py"):
        print(file)

#print (os.listdir())

#
#os.chdir("c:/")
#print (os.listdir("c:/"))
#
#print(os.getlogin())
