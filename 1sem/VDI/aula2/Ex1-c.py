# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:35:13 2025

@author: admin
"""

def fatorial(n):
    
    if n==1 or n==0:
        return 1
    
    return n*fatorial(n-1)

num = int(input("Quero o fatorial de -->"))

print(num,"! = ", fatorial(num))
    