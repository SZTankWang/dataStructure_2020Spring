# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:44:51 2020

@author: Tank
"""

def m_times_n(m,n):
    if n == 0:
        return 0
    else:
        previous = m_times_n(m,n-1)
        initial = m 
        return previous + initial
        
    
print(m_times_n(9,7))