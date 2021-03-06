
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count_dist = {}
    for i in a:
        count_dist[i] = count_dist.get(i, 0) + 1

    count = 0
    for i in b:
        if i in count_dist and count_dist[i] > 0:
            count_dist[i] -= 1
        else:
            count += 1
    count += sum(count_dist.values())
    return count


print(makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke"))

print(makeAnagram("cde", "dcf"))










