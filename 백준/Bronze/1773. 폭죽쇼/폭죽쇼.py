n, c = map(int, input().split())

s = set()

for i in range(n):
  p = int(input())
  p_bomb = [s for s in range(0, c + 1, p)]
  s.update(p_bomb)

print(len(s) - 1)