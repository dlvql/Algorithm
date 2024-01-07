n, cases = map(int, input().split())
arr = [(i + 1) for i in range(n)]

for a in range(cases):
    i, j = map(lambda x: int(x) - 1, input().split())
    arr[i:j + 1] = list(reversed(arr[i:j + 1]))

print(*arr)