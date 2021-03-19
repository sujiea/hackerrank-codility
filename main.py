visited = [[0 for x in range(10)] for y in range(10)]

def connectedCell(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                num = dfs(matrix, i, j)
                if result < num:
                    result = num
    return result


def check(i, j, m, n):
    if 0 <= i <= m - 1 and 0 <= j <= n - 1:
        return True
    else:
        return False

def dfs(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])
    visited[i][j] = 1
    cur = 1

    arr_x = [-1, 0, 1, -1, 1, -1, 0, 1]
    arr_y = [-1, -1, -1, 0, 0, 1, 1, 1]

    for k in range(8):
        x = i + arr_x[k]
        y = j + arr_y[k]
        if check(x, y, m, n) and visited[x][y] == 0 and matrix[x][y] == 1:
            cur += dfs(matrix, x, y)
    return cur



print(connectedCell([[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(connectedCell([[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]))
















