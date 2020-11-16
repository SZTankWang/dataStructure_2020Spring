# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:05:06 2020

@author: Tank
"""

def move(N,a,b,c):
    count = 0
    if N == 1:
        print(a, '=>', c)
        return 1
    else:
        count += move(N-1,a,c,b)
        count += move(1,a,b,c)
        count += move(N-1,b,a,c)
        return count
        
print(move(4,'a','b','c'))