from collections import OrderedDict
def icecreamParlor(m, arr):
    dist = {}
    for i in range(len(arr)):
        if arr[i] < m:
            if m - arr[i] in dist:
                return [dist[m-arr[i]]+1, i + 1]
            dist[arr[i]] = i
    return []

print(icecreamParlor(4, [1, 4, 5, 3, 2]))
print(icecreamParlor(4, [2, 2, 4, 3]))