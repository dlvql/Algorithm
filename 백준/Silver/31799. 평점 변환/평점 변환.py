n = int(input())
s = input().replace('0', '').replace('C', '8').replace('B', '5').replace('A', '2')

ans = []

for idx, v in enumerate(list(s)):
  if v in ['2', '5', '8']:
    ans.append(int(v))
  else:
    if v == '-':
      ans[-1] += 1
    else:
      ans[-1] -= 1

s = []

for idx, v in enumerate(ans):
  if v > 6:
    s.append('B')
  elif v > 4:
    if idx == 0 or ans[idx - 1] > 6:
      s.append('D')
    else:
      s.append('B')
  elif v > 2:
    if idx == 0 or ans[idx - 1] > 4:
      s.append('P')
    else:
      s.append('D')
  elif v == 2:
    if idx == 0 or ans[idx - 1] > 2:
      s.append('E')
    else:
      s.append('P')
  else:
    s.append('E')

print("".join(s))