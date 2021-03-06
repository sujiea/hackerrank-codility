def sherlockAndAnagrams(s):
    len_s = len(s)
    sub_dic = {}
    for i in range(1, len_s):
        for j in range(0, len_s - i + 1):
            substr = "".join(sorted(s[j:i+j]))
            if substr in sub_dic:
                sub_dic[substr] += 1
            else:
                sub_dic[substr] = 1
    suma = 0
    for i in sub_dic:
        if sub_dic[i] > 1:
            suma += sub_dic[i] * (sub_dic[i] - 1) // 2
    return suma


print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("kkkk"))
print(sherlockAndAnagrams("abba"))
print(sherlockAndAnagrams("abcd"))
print(sherlockAndAnagrams("cdcd"))






