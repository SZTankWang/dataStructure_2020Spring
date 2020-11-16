# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:32:34 2020

@author: Tank
"""

def in_somewhere(lissy,value):
    if isinstance(lissy,list) == False:
        return False
    else:
        if value in lissy:
            return True
        else:
            ans = []
            for each in lissy:
                ans.append(in_somewhere(each,value))
            return True in ans


lissy = [[1,2],3,[4,5,6],7]
print(in_somewhere(lissy,4))