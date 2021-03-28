#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
from collections import defaultdict
from heapq import heappop, heappush
# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for (i, j), w in edges.items():
        graph[i].append((j, w))
        graph[j].append((i, w))

    visited = [0] * (n + 1)
    result = [float("inf")] * (n + 1)
    queue = [(0, s)]
    while queue:
        cweight, cnode = heappop(queue)
        if visited[cnode]:
            continue
        visited[cnode] = 1
        for i, w in graph[cnode]:
            if not visited[i] and result[i] > cweight + w:
                result[i] = cweight + w
                heappush(queue, (result[i],i))

    del result[0]
    del result[s-1]
    return [-1 if d == float("inf") else d for d in result]

f = open("testcase.txt", "r")
n = 20
m = 54
edges = dict()

for _ in range(m):
    u, v, w = map(int, f.readline().rstrip().split())
    if (u, v) in edges:
        edges[(u, v)] = min(edges[(u, v)], w)
    elif (v, u) in edges:
        edges[(v, u)] = min(edges[(v, u)], w)
    else:
        edges[(u, v)] = w

s = 17
result = shortestReach(n, edges, s)
print(result)

