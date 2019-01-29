# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:53:22 2019

@author: SKourav
"""

month = input("Enter month: ")

winterlist = ["jan","feb","march"]
summerlist = ["april","may","june"]
rainylist = ["july","august","sep","oct"]

for winter in winterlist :
    if month == winter :
        print("You are in the winter season")
for summer in summerlist :
    if month == summer :
        print("You are in the summer season")
        
for rainy in rainylist :
    if month == rainy :
        print("You are in the rainy season")