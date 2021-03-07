def luckBalance(k, contests):
    loss = 0
    contests.sort(key=lambda a: a[0])
    lossnum = 0
    for i in range(len(contests)-1, -1, -1):
        curl = contests[i][0]
        if contests[i][1] == 1:
            if lossnum < k:
                lossnum += 1
                loss += curl
            else:
                loss -= curl
        else:
            loss += curl
    return loss

print(luckBalance(5,[[13,1],[10,1],[9,1],[8,1],
[13,1],
[12,1],
[18,1],
[13,1]]))
print(luckBalance(3,[[5,1], [2,1], [1,1], [8,1], [10,0], [5,0]]))













