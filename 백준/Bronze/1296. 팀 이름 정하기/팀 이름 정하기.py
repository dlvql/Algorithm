import sys

name = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
ans = []

for i in range(n):
    s = sys.stdin.readline().rstrip()
    now = s + name
    l = now.count('L')
    o = now.count('O')
    v = now.count('V')
    e = now.count('E')
    idx = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
    ans.append((idx, s))

ans.sort(key = lambda x: (-x[0], x[1]))

sys.stdout.write(ans[0][1])