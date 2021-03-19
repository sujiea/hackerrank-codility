def icecreamParlor(m, arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] >= m:
            break
        else:
            j = arr.index(m-arr[i])
            if j > i:
                return [i, j]
    return []


print(icecreamParlor(4, [1, 4, 5, 3, 2]))
print(icecreamParlor(4, [2, 2, 4, 3]))