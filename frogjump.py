# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    first = [0] * X
    for i in range(len(A)):
        if first[A[i] - 1] == 0:
            first[A[i] - 1] = i + 1
    max = 0
    for j in range(0,X,1):
        if first[j] == 0:
            return -1
        if max < first[j]:
            max = first[j]
    return max - 1

print(solution(5,[1,3,1,4,2,3,5,4]))
print(solution(1,[1]))
print(solution(2,[1,1,1,1]))







