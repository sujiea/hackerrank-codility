# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    start = 0
    end = 1
    num = 1
    dup_array = [0] * (M+1)
    dup_array[A[0]] = 1
    while end < len(A):
        if end - start > M:
            break
        else:
            # has duplicates
            if dup_array[A[end]] == 1:
               dup_array[A[start]] = 0
               start += 1
            else:
               dup_array[A[end]] = 1
               end += 1
               num += end - start
        if num > 1000000000:
            num = 1000000000
    return num

print(solution(10,[2,4,1,7,4,9,7,3,5,5,8,7,1]))
print(solution(6,[2,4,5,5,2]))



