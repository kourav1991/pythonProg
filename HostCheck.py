# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:02:06 2019

@author: SKourav
"""



import requests

file = open ("Host.txt","r")

for host in file :
    #print (host)
    host = host.strip()
    try :
        r = requests.get(host)
        if r.status_code == 200 :
            print ("Host :",host)
            print ("Status : ", "Available")
    except Exception as e:
        print ("Host : ", host)
        print ("Status : ", "Not avaialble")
        print ("Exception ", e)
        