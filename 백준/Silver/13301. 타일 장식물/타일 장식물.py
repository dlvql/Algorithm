import sys

n = int(sys.stdin.readline().rstrip())
arr = [0, 1]
l = 0

for i in range(1, n):
  arr.append(arr[-1] + arr[-2])

s = (arr[-1] * 2 + arr[-2]) * 2

sys.stdout.write(str(s))