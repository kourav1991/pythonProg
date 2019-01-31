# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:20:09 2019

@author: SKourav
"""

import os

def HelloOmi(ab):
    print ("Hi " +ab +" Your Folder Created")
    os.playsong(ab)

User1 = input("Enter your Name")

HelloOmi(User1)

