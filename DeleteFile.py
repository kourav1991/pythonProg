# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:01:50 2019

@author: SKourav
"""

import os

'''
Remove file from folder
'''
#
#for file in os.listdir() :
#    if file.endswith(".txt"):
#        print(file)
#        os.remove(file)


#Remove folder empty

#os.rmdir("C:/Users/skourav/Desktop/pythonprog/dir59")

for val in range (61,101):
    os.rmdir("dir" + str(val))
    print ("dir" + str(val))
