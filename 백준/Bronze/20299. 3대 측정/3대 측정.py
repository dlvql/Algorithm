n, k, l = map(int, input().split())
teams = []
c = 0

for i in range(n):
  arr = list(map(int, input().split()))
  if (all(map(lambda x: x >= l, arr))) and (sum(arr) >= k):
    teams += arr
    c += 1

print(c)
print(*map(str, teams))