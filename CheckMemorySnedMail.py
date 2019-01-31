# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:25:48 2019

@author: SKourav
"""

import psutil
import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)

server.login("kouravshiv527@gmail.com","LearnMore@123")


Virtualdisct = dict (psutil.virtual_memory()._asdict())
Swapdisct = dict (psutil.swap_memory()._asdict())
Diskdict = dict(psutil.disk_usage('c:/')._asdict())

if Virtualdisct["percent"] > 50 :
    msg = "Your virtual memory utilization % is more then 50%" + Virtualdisct
    try:
        server.sendmail("kouravshiv527@gmail.com","skourav@slb.com",msg)
        print ("Mail send to User")
    except Exception as e:
        print ("Error while sending the email notification : ", e)