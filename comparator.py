from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def __repr__(self):
        return self

    def comparator(a, b):
        if a._score == b._score:
            return a._name < b._name
        else:
            return a._score > b._score



n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)









