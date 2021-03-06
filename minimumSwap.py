def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[arr[i] -1]
            arr[temp - 1] = temp
            count += 1
        else:
            i += 1
    return count

print(minimumSwaps([4,3,1,2]))
print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))



