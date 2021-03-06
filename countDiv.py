def solution(A, B, K):
    # write your code in Python 3.6
    b = B // K
    if A > 0:
        a = (A - 1) // K
    else:
        a = 0
        b += 1
    return b - a

print(solution(6,11,2))
print(solution(11,345,17))


