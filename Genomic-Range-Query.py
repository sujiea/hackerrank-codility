def solution(S, P, Q):
    # write your code in Python 3.6
    n = len(P)
    result = [0] * n
    for i in range(n):
        sub_str = S[P[i]:Q[i] + 1]
        if "A" in sub_str:
            result[i] = 1
        elif "C" in sub_str:
            result[i] = 2
        elif "G" in sub_str:
            result[i] = 3
        else:
            result[i] = 4
    return result

print(solution(6,11,2))
print(solution(11,345,17))


