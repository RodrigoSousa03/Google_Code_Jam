# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:41:32 2021

@author: User
"""

import itertools


n = int(input())

for t in range(n):
    tup = input()
    tup = tup.split(" ")
    N = int(tup[0])
    C = int(tup[1])
    lista = []
    for m in range (1, N + 1):
        lista.append(m)
    comb = list(itertools.permutations(lista))
    comb = list(map(lambda x:list(x), comb))
    cost = True
    for p in range(len(comb)):
        ll = comb[p]
        if cost == False:
            break
        out = 0
        L = ll.copy()
        for i in range (N-1):
            mn = min(L[i:])
            j = L.index(mn)
            mid = list(reversed(L[i:j+1]))
            L = L[:i] + mid + L[j+1:]
            out += (j - i + 1)
        if out == C:
            cost = False
            ll = list(map(lambda x: str(x), ll))
            penis = " ".join(ll)
            print(f"Case #{t+1}: {penis}")
            break
    if cost == True:
        print(f"Case #{t+1}: IMPOSSIBLE") 
        
        
    
# 5
# 4 6
# 2 1
# 7 12
# 7 2
# 2 1000    
