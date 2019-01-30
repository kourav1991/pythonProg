# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:40:18 2019

@author: SKourav
"""

#Opening the file in write mode

fobj = open("customer.txt","w")

fobj.write("python\n")
fobj.write("sshiv\n")
fobj.write(str(100))
fobj.close()