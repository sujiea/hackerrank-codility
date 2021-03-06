def countTriplets(arr, r):
    dist = {}
    dist_pair = {}
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] * r in dist_pair:
            count += dist_pair[arr[i] * r]
        if arr[i] * r in dist:
            dist_pair[arr[i]] = dist_pair.get(arr[i], 0) + dist[arr[i] * r]
        dist[arr[i]] = dist.get(arr[i], 0) + 1
    return count

print(countTriplets([1,3,9,9,27,81],3))






