import sys
from collections import Counter

n = int(sys.stdin.readline())
nArr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))

cnt = Counter(nArr)

for i in mArr:
  sys.stdout.write(f'{cnt[i]} ')