# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:36:17 2018

@author: ouzarf
"""
import csv

infile = open('budget.csv','r')
for row in csv.reader(infile):
    print(row)

 
infile.close()

