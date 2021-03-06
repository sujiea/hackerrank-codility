def rotLeft(a, d):
    len_a = len(a)
    b = [0] * len(a)
    for i in range(d):
        b[len_a - d + i] = a[i]
    for i in range(d, len_a):
        b[i-d] = a[i]
    return b

print(rotLeft([1,2,3,4,5],3))


