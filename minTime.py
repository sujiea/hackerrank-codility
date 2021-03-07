def minTime(files, numCores, limit):
    files.sort()
    sum = 0
    processed = 0
    numCoresLeft = numCores
    for i in range(len(files) - 1, -1, -1):
        if processed < limit and files[i] >= numCores and files[i] % numCores == 0:
            processed += 1
            sum += files[i] // numCoresLeft
        else:
            sum += files[i]
    return sum





print(minTime([4,1,3,2,8], 4, 1))
print(minTime([5,1,3], 5, 5))

print(minTime([3,1,5], 1, 5))
print(minTime([130291875,474356040,1,8], 5, 3))














