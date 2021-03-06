def solution(A):
    n = len(A)
    m = max(A)
    B = [0] * max(n, m)
    for i in range(n):
        if A[i] > 0:
            B[A[i] - 1] = 1

    for j in range(n):
        if B[j] == 0:
            return j+1
    return n+1

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1000,1,-2,1000]))
print(solution([0]))
