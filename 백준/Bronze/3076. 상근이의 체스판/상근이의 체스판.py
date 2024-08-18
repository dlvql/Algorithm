r, c = map(int, input().split())
a, b = map(int, input().split())

s = ['X' * b, '.' * b]

for i in range(r):
  arr = ''
  for j in range(c):
    arr += s[(i + j) % 2]
  print("\n".join([arr for _ in range(a)]))