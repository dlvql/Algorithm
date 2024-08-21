n = int(input())
m, k = map(int, input().split())
a = list(sorted(map(int, input().split()), reverse=True))

cnt = 0
s = 0
for i in a:
  s += i
  cnt += 1
  if s >= m * k:
    break

if s < m * k:
  cnt = "STRESS"

print(cnt)