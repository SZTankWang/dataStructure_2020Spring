# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:56:49 2020

@author: Tank
"""

class Flipstack:
    def __init__(self):
        self._data = []
    
    def push(self,e):
        self._data.append(e)
        
    def pop(self):
        return self._data.pop(-1)
    
    def __len__(self):
        return len(self._data)
    
    def flip(self):
        for i in range(len(self._data)//2):
            self._data[i], self._data[len(self._data)-1-i] = self._data[len(self._data)-1-i],self._data[i]
            
    def __str__(self):
        return str(self._data)
                
fs = Flipstack()
for i in range(4):
    fs.push(i)
print(fs)
    
fs.flip()
print(fs)

for i in range(4):
    fs.push(i+10)
    
print(fs)

while len(fs)>0:
    print(fs.pop())
    fs.flip()
print(fs)
            