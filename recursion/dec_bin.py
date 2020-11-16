# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:30:53 2020

@author: Tank
"""

# 十进制转二进制的方法：除2取余，逆序排列
def change(n):
    result = ''
    if n == 0:    # 输入为0的情况
        return result
    else:
        result = change(n // 2)         # 调用自身
        return result + str(n % 2)
num = int(input("请输入一个十进制的数字："))  # 提示用户输入十进制数，由于input()的返回值是str类型，故需要转化为int类型
print(change(num))