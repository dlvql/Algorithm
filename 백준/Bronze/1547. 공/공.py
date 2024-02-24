cases = int(input())
li = [1, 0, 0]

for i in range(cases):
    n, m = map(int, input().split())
    t = li[n - 1]
    li[n - 1] = li[m- 1]
    li[m - 1] = t

print(li.index(1) + 1)