# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:47:17 2018

@author: ouzarf
"""

class Automobile(object):
    def __init__(self, vin, make, model = ''):
       self.vin = vin 
       self.make = make 
       self.model = model 
    
    def __str__(self):
       return 'vin:%s, %s,  %s' %  (self.vin, self.make, self.model)
    def make_noise(self):
        print ('HEY  Im a %s,  %s' %  ( self.make, self.model))
        
a = Automobile('13500','toyota','pryus')
print a.make, a.model
print a
a.make_noise()