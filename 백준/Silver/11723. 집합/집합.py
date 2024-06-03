import sys

input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
  regex = input().rstrip()
  if regex == "all":
    s = set(range(21))
    continue
  elif regex == "empty":
    s = set()
    continue
  else:
    op, x = regex.split()
    x = int(x)
    if op == 'add' and x not in s:
      s.add(x)
    elif op == 'remove' and x in s:
      s.remove(x)
    else:
      if op == 'toggle':
        if x not in s:
          s.add(x)
        else:
          s.remove(x)
      elif op == 'check':
        print(int(x in s))