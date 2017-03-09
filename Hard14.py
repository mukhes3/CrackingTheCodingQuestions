# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:00:07 2017

@author: Sumit
"""

import heapq

def FindKSmallest(Arr,k):
    
    heap = []
    for i in range(0,k):
        heap+= [-1*Arr[i]]

    heapq.heapify(heap)
    
    for i in range(k,len(Arr)):
        
        temp = -1*heap[0]
        
        if temp>=Arr[i]:
            temp2 = heapq.heappushpop(heap,-1*Arr[i])
    
    l = []       
    for i in range(0,k):
        l += [-1*heap[0]]
        heapq.heappop(heap)
        
    return l


A = [1,2,3,-1,-3,7,9,-9]

print(FindKSmallest(A,3))
    