# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:31:44 2017

@author: Sumit
"""

def RetMax(a,b):
    
    c = bin(a - b)  
    
    if c[0] == '-':
        return b 
    else:
        return a
    
print (RetMax(12,13))

