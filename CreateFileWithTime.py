# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:54:11 2019

@author: SKourav
"""

import os 
import datetime

print(datetime.datetime.today())

open("text" +str( datetime.datetime.today() )+ ".txt",'a').close()
 
