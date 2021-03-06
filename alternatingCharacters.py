
# Complete the makeAnagram function below.
# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    stack = []
    count = 0
    for x in s:
        if len(stack) == 0 or x != stack[len(stack)-1]:
            stack.append(x)
        else:
            count += 1
    return count


print(alternatingCharacters("AAAA"))
print(alternatingCharacters("BBBBB"))
print(alternatingCharacters("ABABABAB"))
print(alternatingCharacters("BABABA"))
print(alternatingCharacters("AAABBB"))
print(alternatingCharacters("AABBABAB"))











