# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:49:21 2020

@author: Tank
"""

def output_reverse(S):
    if len(S)==1:
        return S
    else:
        previous = output_reverse(S[1:])
        initial = S[0]
        return previous+initial
    
print(output_reverse('haha'))