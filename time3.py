# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    first_sum = A[0]
    next_sum = sum(A) - A[0]
    min_diff = abs(next_sum - first_sum)
    for p in range(1, len(A)-1, 1):
        first_sum = first_sum + A[p]
        next_sum = next_sum - A[p]
        if min_diff > abs(first_sum - next_sum):
            min_diff = abs(first_sum - next_sum)
    return min_diff

print(solution([1, 2, 3, -4]))
print(solution([2,100]))
print(solution([-1000, 1000]))






