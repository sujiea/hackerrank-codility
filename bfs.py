from collections import deque
def bfs(n, m, edges, s):
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)

    result_dict = {s: 0}
    queue = deque([s])
    visited = [s]
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if i not in visited:
                result_dict[i] = result_dict[current] + 6
                queue.append(i)
                visited.append(i)
    result = []
    for node in range(1, n + 1):
        if s != node:
            result.append(result_dict.get(node, -1))
    return result