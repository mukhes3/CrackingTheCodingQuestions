# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:21:29 2017

@author: Sumit
"""

def aplusb(a, b):

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a


A = 12
B = 24 
print (aplusb(A,B))