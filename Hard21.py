# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:10:43 2017

@author: Sumit
"""

def VolumeHist(Arr):
    
    M = Arr[0]
    cnt = 0 

    #get the sorted elements 
    A_s = sorted(Arr)
            
    for i in range(1,len(Arr)):
        if M             