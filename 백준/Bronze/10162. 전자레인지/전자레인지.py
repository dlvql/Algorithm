t = int(input())

arr = [300, 60, 10]
ans = []

if(t % 10 != 0):
  print(-1)
else:
  for i in arr:
    ans.append(t // i)
    t %= i
  print(*ans)