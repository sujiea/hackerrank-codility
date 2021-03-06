# This is a sample Python script.

# Press the green button in the gutter to run the script.
from math import sqrt

def solution(A):

    peak = [0] * (len(A))
    peak[len(A) - 1] = len(A)
    last_peak = len(A)
    for i in range(len(A) - 2, 0, -1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            last_peak = i
        peak[i] = last_peak
    peak[0] = last_peak

    upper = int(sqrt(len(A))) + 2
    while lower < upper - 1:
        cur_num = int((lower + upper) / 2)
        if can_fit(peak, cur_num):
            lower = cur_num
        else:
            upper = cur_num
    return lower


def can_fit(peak, cur_num):
    peak_num = 1 - cur_num
    for i in range(cur_num):
        if peak_num + cur_num > len(peak) - 1:
            return False
        peak_num = peak[peak_num + cur_num]
    return peak_num < len(peak)


print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))
print(solution([1]))
print(solution([1,5,3]))



