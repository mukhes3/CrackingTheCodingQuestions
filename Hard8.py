# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 20:57:17 2017

@author: Sumit
"""

def GenSortingProblem(Arr):
    
    A = []
    B = []
    I = []
    D = {}
    
    for i in range(0,len(Arr)):
        
        A += [Arr[i][0]]
        B += [Arr[i][1]]
        
        D[Arr[i][0]] = i
        
    As = sorted(A) #uses O(nlogn) time 
                
               
    for i in range(0,len(Arr)):
        I += [D[As[i]]]
        
    L = []
    
    for i in range(0,len(Arr)-1):
        
        if B[I[i]]<=B[I[i+1]]:
            L += Arr[I[i]]
            
    if B[I[len(Arr)-1]] >= B[I[len(Arr)-2]]:
        L += Arr[I[len(Arr)-1]]
        
    return L

X = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
print (GenSortingProblem(X))
        
    