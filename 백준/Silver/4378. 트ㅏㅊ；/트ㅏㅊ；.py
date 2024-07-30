import sys

s = "".join(sys.stdin.readlines())

q = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

ans = ''

for i in s:
  if i in q:
    ans += q[q.index(i) - 1]
  else:
    ans += i

print(ans)