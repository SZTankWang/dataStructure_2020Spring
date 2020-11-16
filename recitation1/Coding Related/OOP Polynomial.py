# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:22:38 2020

@author: Tank
"""

import copy
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
    
    def __len__(self):
        return len(self.coeffs)
    
    def __setitem__(self,j,value):
        self.coeffs[j] = value
    
    def __getitem__(self,j):
        return self.coeffs[j]
    
    def __iadd__(self,other):
        gap = max(len(self),len(other)) - min(len(self),len(other))
        
        if len(self) > len(other):
            new_array = copy.deepcopy(self)
            result = Polynomial(new_array)
            for i in range(len(other)):
                result[i+gap] += other[i]
            
        if len(self) < len(other):
            new_array = copy.deepcopy(other)
            result = Polynomial(new_array)
            for i in range(len(self)):
                result[i+gap] += self[i]
            
        if len(self) == len(other):
            result = [0]*len(self)
            for i in range(len(self)):
                result[i] = self[i] + other[i]
        
        return result

    def evaluate_at(self,value):
        poly = 0
        order = 1
        for i in self.coeffs:
            poly += i* (value**(len(self.coeffs)-order))
            order += 1
        return poly


    def __str__(self):
        poly = ''
        order = 1
        for i in self.coeffs:
            if order == len(self.coeffs):
                poly += str(i)
                return poly
            else:	
                poly += str(i)+'x^'+str(len(self.coeffs)-order)+ '+'
                order += 1

def main():
	# 1x^4 + 2x^3 + 3x^2 + 4x + 5
	coeffs = [1,2,3,4,5]
	poly = Polynomial(coeffs)
	print(poly.evaluate_at(2))   # 57
	print(poly.evaluate_at(3))   # 179
	print(poly)	 # Outputs: 1x^4 + 2x^3 + 3x^2 + 4x^1 + 5

	# 4x^3 + 6x^2 + 8x^1 + 10
	coeffs = [4,6,8,10]
	poly2 = Polynomial(coeffs)
	print(poly2)	 # Outputs: 4x^3 + 6x^2 + 8x^1 + 10
	poly += poly2
	print(poly)

main()
