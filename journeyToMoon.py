class QUWPC:
    def __init__(self, n):
        self.connected = [i for i in range(n)]
        self.sz = [1] * n

    def root(self, i):
        while self.connected[i] != i:
            i = self.connected[i]
        return i

    def unite(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.sz[i] > self.sz[j]:
            self.connected[j] = i
            self.sz[i] += self.sz[j]
        else:
            self.connected[i] = j
            self.sz[j] += self.sz[i]


def journeyToMoon(n, astronaut):
    quwpc = QUWPC(n)

    for v in astronaut:
        quwpc.unite(v[0], v[1])

    result = 0
    dict = {}
    for i in range(n):
        r = quwpc.root(i)
        dict[r] = dict.get(r, 0) + 1
    sum = 0
    for k in dict.keys():
        result += dict[k] * sum
        sum += dict[k]

    return result


print(journeyToMoon(5, [[0,1],[2,3],[0,4]]))
print(journeyToMoon(2, [[0,1]]))
print(journeyToMoon(4, [[0,2]]))
