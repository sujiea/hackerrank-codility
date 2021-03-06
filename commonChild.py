# Complete the commonChild function below.
def commonChild(s1, s2):
    n = len(s1)
    matched = [[0]* (5001) for i in range(5001)]
    for i in range(0, n):
        for j in range(0, n):
            if s1[i:i+1] == s2[j:j+1]:
                matched[i+1][j+1] = matched[i][j] +1
            else:
                matched[i+1][j+1] = max(matched[i][j+1], matched[i+1][j])

    return matched[n][n]

print(commonChild("HARRY","SALLY"))

print(commonChild("AA","BB"))

print(commonChild("AAA","AAA"))
print(commonChild("SHINCHAN","NOHARAAA"))





