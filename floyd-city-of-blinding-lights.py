import math
import os
import random
import re

import sys
# Complete the bfs function below.

with open("testcase.txt", "rt") as f:
    road_nodes, road_edges = map(int, f.readline().split())

    dist = [[None for x in range(road_nodes)] for y in range(road_nodes)]
    for i in range(road_nodes):
        dist[i][i] = 0

    for i in range(road_edges):
        road_from, road_to, road_weight = map(int, f.readline().split())
        dist[road_from - 1][road_to - 1] = road_weight

    for k in range(road_nodes):
        tk = dist[k]
        for i in range(road_nodes):
            if dist[i][k] is not None:
                ti = dist[i]
                for j in range(road_nodes):
                    if tk[j] is not None and (ti[j] is None or ti[j] > ti[k] + tk[j]):
                        dist[i][j] = ti[k] + tk[j]

    q = f.readline()

    out = ""
    for q_itr in range(int(q)):
        xy = f.readline().split()
        x = int(xy[0])
        y = int(xy[1])
        if dist[x - 1][y - 1] is None:
            out = out + "-1\n"
        else:
            out = out + str(dist[x - 1][y - 1]) + "\n"
    print(out)