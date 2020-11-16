# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:10:19 2020

@author: Tank
"""

def majority_number(lissy):
    memo = {}
    for i in lissy:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i]+=1
    
    count = 0
    for i in memo:
        if memo[i] > count:
            count = memo[i]
            ans = i
    return ans


lissy = [0,1,5,-1,1,1]
print(majority_number(lissy))