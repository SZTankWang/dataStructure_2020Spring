# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:20:45 2020

@author: Tank
"""

alpha = [1,2,3]
beta = alpha
beta += [4,5]
beta = beta + [6,7]
# =============================================================================
# beta += [6,7]
# =============================================================================
print(alpha)
#difference in __iadd__ and __add__
#shallow copy, += change both, while + won't