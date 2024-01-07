n, cases = map(int, input().split())
arr = [(i + 1) for i in range(n)]

for a in range(cases):
    i, j = map(lambda x: int(x) - 1, input().split())
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

print(*arr)