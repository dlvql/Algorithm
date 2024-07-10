import sys

n = list(map(int, list(sys.stdin.readline().rstrip())))

if(len(n) >= 3):
  for idx, i in enumerate(n):
    if(i == 0):
      n[idx - 1] *= 10
      n.pop(idx)

sys.stdout.write(str(sum(n)))