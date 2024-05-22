import sys

while True:
  n = sys.stdin.readline().rstrip()
  if n == '0':
    break
  while len(n) > 1:
    n = str(sum(map(int, list(n))))
  sys.stdout.write(n + '\n')