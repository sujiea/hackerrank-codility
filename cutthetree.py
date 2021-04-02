#!/bin/python3

import math
import os
import random
import re

import sys
# Complete the bfs function below.

def cutTheTree(data, edges): # CORRECTION TO SETUP: data 0-indexed

    T, L, d,D = {a:set() for a in range(1,1+n)}, {1}, 0, [0]*(1+n)
    for a,b in edges : T[a].add(b) ; T[b].add(a) # start symmetric
    while L : # decycle graph T into a tree and calculate depths D
        L1 = set() # becomes all visited nodes at depth level d
        for a in L :
            D[a] = d ; L1 |= T[a]
            for b in T[a] : T[b].remove(a)
        d += 1 ; L = L1
    temp = sorted(range(1, 1 + n), key=lambda x: -D[x])
    for a in temp:#bottom up
        data[a-1] += sum( data[b-1] for b in T[a] ) #find subtotal
    return min(abs(data[0]-2*data[x]) for x in range(1,n) )




f = open("testcase.txt", "r")
n = 10

data = list(map(int, f.readline().rstrip().split()))
edges = []

for _ in range(n - 1):
    edges.append(list(map(int, f.readline().rstrip().split())))


result = cutTheTree(data, edges)
print(result)

