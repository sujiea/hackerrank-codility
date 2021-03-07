def substrCount(n, s):
    arr = []
    pre = s[0:1]
    pointer = 0
    count = n
    for i, v in enumerate(s):
        if i and pre == v:
            arr[pointer - 1][1] += 1
        else:
            pre = v
            pointer += 1
            arr.append([v, 1])

    for i in range(len(arr)):
        count += (arr[i][1] * (arr[i][1] - 1)) // 2

    for i in range(1, len(arr) - 1):
        if arr[i-1][0] == arr[i + 1][0] and arr[i][1] == 1:
            count += min(arr[i-1][1], arr[i + 1][1])
    return count


print(substrCount(4, "aaaa"))
print(substrCount(5, "asasd"))
print(substrCount(7, "asasdaa"))
print(substrCount(6, "aaabbc"))












