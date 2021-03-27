# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:44:46 2021

@author: User
"""

n = int(input())

for k in range(1, n+1):
    out = 0
    leng = int(input())
    L = input()
    L = L.split(" ")
    L = list(map(lambda x:int(x), L))
    for i in range (leng-1):
        mn = min(L[i:])
        j = L.index(mn)
        mid = list(reversed(L[i:j+1]))
        L = L[:i] + mid + L[j+1:]
        out += (j - i + 1)
    print(f"Case #{k}: {out}")
    
    
