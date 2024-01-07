n, cases = map(int, input().split())
arr = [0 for i in range(n)]

for a in range(cases):
    i, j, k = map(int, input().split())
    for b in range(i, j + 1):
        arr[b - 1] = k

print(*arr)