# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:48:32 2019

@author: SKourav
"""

name = input ("Enter any string : ")
alpha = 0
digit = 0

for item in name :
    if item.isalpha():
        alpha = alpha +1
    if item.isdigit():
        digit = digit + 1

print("No of alphabet is : ", alpha)

print("No of digit is : ", digit)