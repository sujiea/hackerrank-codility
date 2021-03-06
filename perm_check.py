def solution(A):
    n = len(A)
    A.sort()
    print(A)
    for i in range(n):
        if A[i] != i+1:
            return False
    return True

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([5]))

