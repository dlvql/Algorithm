import sys
s = sys.stdin.readlines()

for i in s:
  h, p = map(int, i.rstrip().split())
  print(f'{round(h / p, 2):.2f}')