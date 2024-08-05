import sys

sys.setrecursionlimit(10 ** 6)

m = []
visited = []

def solution(maps):
    global m
    m = list(map(lambda x: list(map(int, list(x.replace('X', '0')))), maps))
    global visited
    visited = list(map(lambda x: list(map(lambda x: False, x)), m.copy()))
    ans = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > 0:
                val = dfs(i,j)
                if val == 0:
                    val = -1
                ans.append(val)
    ans.sort()
    ans = list(filter(lambda x: x != -1, ans))
    if not ans:
        ans = [-1]
    return ans

def dfs(x, y):
    v = 0
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]) or visited[x][y] or m[x][y] == 0:
        return 0
    visited[x][y] = True
    v += m[x][y]
    v += dfs(x - 1, y)
    v += dfs(x + 1, y)
    v += dfs(x, y - 1)
    v += dfs(x, y + 1)
    return v