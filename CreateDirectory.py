# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:44:40 2019

@author: SKourav
"""
i = 1
import os
for val in range(1,101) :
    os.mkdir("dir" + str(i))
    i = i + 1
print (os.listdir())
        