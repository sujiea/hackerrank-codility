# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    return N // max_divide(N, M)

# write your code in Python 3.6
def max_divide(N, M):
    if M == 0:
        return N
    else:
        return max_divide(M, N % M)
