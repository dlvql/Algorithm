import sys

s = list(map(lambda x: x.rstrip(), sys.stdin.readlines()))

ans = int(s[0])

for idx in range(0, len(s) - 2, 2):
  ans = int(eval(f'{ans} {s[idx + 1]} {s[idx + 2]}'))

print(ans)