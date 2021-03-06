# This is a sample Python script.

# Press the green button in the gutter to run the script.
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    diff = Y - X
    if diff % D == 0:
        return diff // D
    else:
        return int(diff // D) + 1

print(solution(1,5,2))
print(solution(2,3,5))
print(solution(1,9,3))






