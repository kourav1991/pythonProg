# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:02:14 2019

@author: SKourav
"""

pass1 = str( input("Enter password :"))
match = 0

alist = ["$","#","@"]
         
if len(pass1) < 6 :
    print("invalid password length is less then 6 char")
elif len(pass1) > 12 :
    print("invalid paswword length is more then 12 char")
else :
    for var in alist :
        if var in pass1:
           match =  match + 1

if match > 0 :
    print("valid pass")
else :
    print("invalid pass")
        