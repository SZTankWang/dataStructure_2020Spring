# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:14:50 2020

@author: Tank
"""

def second_larget_element(lissy):
    maximum = 0
    
    for i in lissy:
        if i > maximum:
            maximum = i
    target = maximum - lissy[0]

    for j in lissy:
        if j == maximum:
            continue
        elif maximum - j < target:
            target = maximum - j
            ans = j
    return ans

lissy = [100,40,3,400,30,50,60,350,70]
print(second_larget_element(lissy))
        
        
        