def isValid(s):
    count_dic = {}
    for i, v in enumerate(s):
        count_dic[v] = count_dic.get(v, 0) + 1

    removed = 0
    bnum = 0
    matched = 0
    for k in count_dic.keys():
        if bnum == 0:
            bnum = count_dic[k]
        elif count_dic[k] == bnum + 1 and removed == 0:
            removed = 1
        elif (count_dic[k] == bnum - 1 or count_dic[k] == 1) and removed == 0:
            removed = 1
            if matched == 0:
                bnum = bnum - 1
        elif count_dic[k] == bnum:
            matched = 1
            continue
        else:
            return "NO"
    return "YES"


print(isValid("ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"))
print(isValid("abcdefghhgfedecba"))
print(isValid("aabbccddeefghi"))












