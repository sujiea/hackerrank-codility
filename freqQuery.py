def freqQuery(queries):
    result = []
    dict_q = {}
    for attr in queries:
        if attr[0] == 1:
            dict_q[attr[1]] = dict_q.get(attr[1], 0) + 1
        elif attr[0] == 2:
            if attr[1] in dict_q and dict_q[attr[1]] > 0:
                dict_q[attr[1]] -= 1
        elif attr[0] == 3:
            if attr[1] in dict_q.values():
                result.append(1)
            else:
                result.append(0)
    return result


def freqQuery2(queries):
    result = []
    dict_q = {}
    dict_c = {}
    for attr in queries:
        if attr[0] == 1:
            dict_q[attr[1]] = dict_q.get(attr[1], 0) + 1
            if dict_q[attr[1]] - 1 in dict_c and dict_c[dict_q[attr[1]] - 1] > 0:
                dict_c[dict_q[attr[1]] - 1] -= 1
            dict_c[dict_q[attr[1]]] = dict_c.get(dict_q[attr[1]], 0) + 1
        elif attr[0] == 2:
            if attr[1] in dict_q and dict_q[attr[1]] > 0:
                dict_c[dict_q[attr[1]]] -= 1
                dict_q[attr[1]] -= 1
                dict_c[dict_q[attr[1]]] = dict_c.get(dict_q[attr[1]], 0) + 1
        elif attr[0] == 3:
            if attr[1] in dict_c and dict_c[attr[1]] > 0:
                result.append(1)
            else:
                result.append(0)
    return result

print(freqQuery([[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[3,10],[1,10000004],[3,5],[2,4],[2,3],[2,6],[1,10000004],[3,10],[3,3],[1,10000004],[1,10000004],[3,10],[3,10],[1,10000004],[1,10000004],[2,7],[1,10000004],[3,7],[3,9],[2,9],[2,8],[3,4],[3,4],[1,10000004]]))

print(freqQuery2([[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[1,10000004],[3,10],[1,10000004],[3,5],[2,4],[2,3],[2,6],[1,10000004],[3,10],[3,3],[1,10000004],[1,10000004],[3,10],[3,10],[1,10000004],[1,10000004],[2,7],[1,10000004],[3,7],[3,9],[2,9],[2,8],[3,4],[3,4],[1,10000004]]))




