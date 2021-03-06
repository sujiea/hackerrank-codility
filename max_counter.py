# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    result = [0] * N
    start = 0
    max_num = 0
    for i in range(len(A)):
        if A[i] > N:
            start = max_num
        else:
            if start > result[A[i]-1]:
                result[A[i]-1] = start + 1
            else:
                result[A[i]-1] += 1
            if result[A[i] - 1] > max_num:
                max_num = result[A[i] - 1]
    if start > 0:
        for j in range(N):
            if result[j] < start:
                result[j] = start
    return result

print(solution(5,[3,4,4,6,1,4,4]))
print(solution(5,[]))
print(solution(5,[1,6]))
print(solution(5,[3,3]))








