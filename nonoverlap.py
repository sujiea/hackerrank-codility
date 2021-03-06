# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    last_end = -1
    count = 0
    for i in range(len(A)):
        if A[i] > last_end:
            last_end = B[i]
            count += 1
    return count


