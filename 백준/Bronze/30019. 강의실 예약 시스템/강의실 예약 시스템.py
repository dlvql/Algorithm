import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
m = lst[-1][-1]

room = [0 for i in range(1, n + 2)]

for i, s, e in lst:
  if(room[i] <= s):
    room[i] = e
    sys.stdout.write("YES\n")
  else:
    sys.stdout.write("NO\n")
