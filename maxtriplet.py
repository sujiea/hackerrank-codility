# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max1 = -1001
    max2 = -1001
    max3 = -1001
    min1 = 1001
    min2 = 1001
    for i in range(len(A)):
        if A[i] > max1:
            max3 = max2
            max2 = max1
            max1 = A[i]
        elif A[i] > max2:
            max3 = max2
            max2 = A[i]
        elif A[i] > max3:
            max3 = A[i]

        if A[i] < min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]
    return max(max1 * max2 * max3, min1 * min2 * max1)


print(solution([-3,1,2,-2,5,6]))
print(solution([-1,2,3]))
print(solution([-1000,-2,3,4,5]))


