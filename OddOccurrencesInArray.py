# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    if len(A) > 0:
        result = A[0]
    else:
        result = None
    for i in range(0, len(A), 2):
        result = A[i]
        if i < len(A) - 1 and A[i] != A[i+1]:
            break
    return result

print(solution([9,3,9,3,7]))
print(solution([]))
print(solution([9]))






