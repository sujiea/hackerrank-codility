# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    count = 0
    sum = 0
    for i in range(len(A)):
        if sum >= K:
            sum = 0
            count += 1
        sum += A[i]
    return K


