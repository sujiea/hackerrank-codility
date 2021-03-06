def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        if q[i] > i + 3:
            print("Too chaotic")
            return
        for j in range(max(q[i]-2, 0), i):
            if q[j] > q[i]:
                count += 1
    print(count)

minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
minimumBribes([2, 1, 5, 3, 4])


