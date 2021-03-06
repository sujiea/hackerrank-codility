import re

def solution(S):
    # write your code in Python 3.6
    print(re.search(r"(?!$)a*b*", S).groups(0))
    if re.match(r"(?!$)a*b*", S).span()[1] == len(S):
        return True
    else:
        return False


print(solution("aabbb"))
print(solution("a"))
print(solution("b"))
print(solution("aa"))
print(solution("bb"))
print(solution("abba"))
print(solution("ba"))



