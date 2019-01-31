# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:35:45 2019

@author: SKourav
"""

#CSV to xl conversion 

from openpyxl import Workbook
wb = Workbook()
ws = wb.active

cityList = []
count = 1

with open ("sample1.csv","r") as fobj:
    for line in fobj:
        line = line.strip()
        LineList = line.split(",")
        ws.append(LineList)
        
wb.save("CSVtoExcel.xlsx")
print("Sucsessfully converted to excel")