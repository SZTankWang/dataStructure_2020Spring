# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:51:17 2020

@author: Tank
"""

def rev2(A,i):
    if i == len(A)//2:
        return A
    else:
        previous = rev2(A,i+1)
        previous[i],previous[len(A)-1-i] = previous[len(A)-1-i],A[i]
        return previous
        
        
        
print(rev2([1,2,3,4],0))