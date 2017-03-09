# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:47:53 2017

@author: Sumit
"""

def FindLongestBinSubArray(Arr):
    
    l = [0]*len(Arr)
    D = {}
    temp = 0
    #convert letter and numbers to zero and 1 and calculate sum and create dict
    for i in range(0,len(Arr)):
        if hash(Arr[i])!=Arr[i]:
            Arr[i] = 0 
        else:
            Arr[i] = 1
        
        if i==0:
            if Arr[i]==1:
                l[i] = 1
            else:
                l[i] = -1
            
        elif Arr[i]==1:
            l[i] = l[i-1] + 1
        else:
            l[i] = l[i-1] - 1
    
        D[l[i]] = i 

    m = 0 
    
    print(l)
    for i in range(0,len(Arr)):
        t = D[l[i]] - i 
             
        if (l[i] == 0) and (m<=i+1):
            m = i + 1 
        elif t>= m:
            m = t
    
    return m

A = ['a','b',1,2,'c','d',1]

print(FindLongestBinSubArray(A))        
         
     
    