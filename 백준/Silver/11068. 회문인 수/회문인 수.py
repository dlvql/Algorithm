t = int(input())

def solution(n, base):
    s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$"
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, base)
        rev_base += s[mod]
    return rev_base[::-1]

for i in range(t):
  s = int(input())
  ans = 0
  for v in range(2, 65):
    if str(solution(s, v)) == str(solution(s, v))[::-1]:
      ans = 1
  print(ans)