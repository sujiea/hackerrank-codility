def jumpingOnClouds(c):
    len_c = len(c)
    count = 0
    i = 0
    while i < len_c:
        if i < len_c - 2:
            if c[i+2] == 0:
                i += 2
                count += 1
            elif c[i+1] == 0:
                i += 1
                count += 1
            else:
                return -1
        elif i == len_c - 2:
            if c[i+1] == 0:
                i += 1
                count += 1
        else:
            i += 1
    return count



print(jumpingOnClouds([0,1,0,0,0,1,0]))

print(jumpingOnClouds([0,1,1,0,0,1,0]))

