# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:27:46 2017

@author: Sumit
"""

def MissingNumber(Arr,N):
    
    D = {}
    
    for i in range(0,len(Arr)):
        
        D[Arr[i]] = 1
         
    
    l = []
    
    for i in range(0,N+1):
        
        temp = D.get(i,False)
        
        if temp == False:
            l += [i]
    
    return l


A = [0,1,2,3,5]
print (MissingNumber(A,5))