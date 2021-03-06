
# Complete the makeAnagram function below.
# Complete the alternatingCharacters function below.
def substrCount(n, s):
    stack = []
    count = 0
    for x in s:
        if len(stack) == 0 or x != stack[len(stack)-1]:
            stack.append(x)
        else:
            count += 1
    return count


print(substrCount(5, "asasd"))
print(substrCount(7, "asasd"))
print(substrCount(4, "aaaa"))











