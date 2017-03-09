# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:44:18 2017

@author: Sumit
"""

def EasySoln(n):
    
    cnt = 0 
    
    for i in range(0,n+1):
        cnt += GetNoTwos(i)
        
    return cnt 

def GetNoTwos(r): 
    
    if r <= 1:
        return 0 
    
    cnt2 = 0 
    c = 1
    
    while(c == 1):
        temp = r%10
        r = int(r/10) 
        
        
        if temp == 2:
            cnt2+=1
        
        if r==0:
            c=0 
    
    return cnt2

print(EasySoln(25))

