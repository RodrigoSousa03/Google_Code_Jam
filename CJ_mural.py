# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:18:33 2021

@author: User
"""

n = int(input())

for j in range(n):
    tup = input()
    tup = tup.split(" ")
    X = int(tup[0])
    Y = int(tup[1])
    string = tup[2]
    pre = "?"
    out = 0
    for i in range(0,len(string)):
        if string[i] == "C":
            if pre == "J":
                out += Y
            pre = "C"
        elif string[i] == "J":
            if pre == "C":
                out += X
            pre = "J"
    print(f"Case #{j+1}: {out}")
                
        

# 4
# 2 3 CJ?CC?
# 4 2 CJCJ
# 1 3 C?J
# 2 5 ??J??? 