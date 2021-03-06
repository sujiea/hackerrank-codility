def twoStrings(s1, s2):
    s1_dic = {}
    for i in s1:
        s1_dic[i] = 1
    for i in s2:
        if i in s1_dic:
            return "YES"
    return "NO"

print(twoStrings("give me one grand today night", "give one grand today"))





