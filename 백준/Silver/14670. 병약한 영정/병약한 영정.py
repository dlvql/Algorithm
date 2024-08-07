n = int(input())
pills = {}

for i in range(n):
  pill = list(map(int, input().split()))
  pills[pill[0]] = pill[1]

r = int(input())
ss = {}

for i in range(r):
  s = list(map(int, input().split()))
  ans = ''
  for i in s[1:]:
    if i not in pills.keys():
      ans = 'YOU DIED'
      break
    else:
      ans += f'{pills[i]} '
  print(ans.rstrip())
  ss[s[0]] = s[1:]