import sys

n = int(sys.stdin.readline().rstrip())
arr = list(sorted(map(int, sys.stdin.readline().rstrip().split())))
dArr = dict(zip(arr, [0 for _ in arr]))
cArr = list()
m = 0

for i in arr:
  dArr[i] += 1

sys.stdout.write(str(max(dArr.values())))