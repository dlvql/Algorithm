import sys

t = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readlines()))
ans = list()

for i in arr:
  q, i = i // 25, i % 25
  d, i = i // 10, i % 10
  n, i = i // 5, i % 5
  print(f'{q} {d} {n} {i}')
